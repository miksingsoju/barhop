from django.shortcuts import render

# Create your views here.

def bar_list(request):
    return render(request, 'bars/bar-list.html')
