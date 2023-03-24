from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    table_data = {'header': ['Name', 'Age', 'Country'],
                  'data': [['John', 23, 'USA'],
                           ['Alice', 35, 'France'],
                           ['Bob', 47, 'Germany']]}
    
    return render(request, 'pages/home.html', context=table_data)