from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    people = [
        {'name': 'John', 'age': 30},
        {'name': 'Paul', 'age': 28},
        {'name': 'George', 'age': 45},
        {'name': 'Ringo', 'age': 67},
        {'name': 'AQ', 'age': 23},
        {'name': 'Farooq', 'age': 24},
    ]
    
    return render(request, "index.html",context={'people': people})

def success_page(request):
    print('*'*10)
    return HttpResponse("<h1>this is a successful page</h1>")