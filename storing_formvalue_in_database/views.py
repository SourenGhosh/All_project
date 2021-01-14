from django.shortcuts import render
from django.shortcuts import render
from .forms import book_form
from django.http import HttpResponse
# Create your views here.
def add_book(request):
    if request.method == 'POST':
        form = book_form(request.POST)
        if form.is_valid():
            form.save() # this will save Car info to database
            return HttpResponse("book added to book_shelf")
    else:          #display empty form
        form = book_form()
        return render(request, 'storing_formvalue_in_database/add_book.html', {'form': form})

#CAN BE ACCESSED THROUGH http://127.0.0.1:8000/storing_formvalue_in_database/addbook/
        
