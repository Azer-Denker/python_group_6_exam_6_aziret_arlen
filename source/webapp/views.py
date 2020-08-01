from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed

from webapp.models import Book
from .forms import BookForm


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Book.objects.all()
    else:
        data = Book.objects.filter(status='active')
    return render(request, 'index.html', context={
        'books': data
    })


def book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)

    context = {'book': book}
    return render(request, 'book_view.html', context)


def book_create_view(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, 'book_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = Book.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                status='active'
            )
            return redirect('book_view', pk=book.pk)
        else:
            return render(request, 'book_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        form = BookForm(initial={
            'title': book.title,
            'author': book.author,
            'text': book.text,
            'status': book.status,
        })
        return render(request, 'book_update.html', context={
            'form': form,
            'book': book
        })
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.title = form.cleaned_data['title']
            book.text = form.cleaned_data['text']
            book.author = form.cleaned_data['author']
            book.status = form.cleaned_data['status']
            book.save()
            return redirect('book_view', pk=book.pk)
        else:
            return render(request, 'book_update.html', context={
                'book': book,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'book_delete.html', context={'book': book})
    elif request.method == 'POST':
        book.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
