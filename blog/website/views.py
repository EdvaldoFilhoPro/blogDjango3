from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def hello_blog(request):
    lista = ['Django', 'python', 'Git', 'Html',
     'Banco de dados', 'Linux', 'Nginx', 'Uwsgi'
     ]
    data = {'name': 'Curso de Django 3', 'lista_tecnologia': lista}
    return render(request, 'index.html', data)
