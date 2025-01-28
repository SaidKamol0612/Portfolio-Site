from django.shortcuts import render

from .models import AuthorInfo

def home_view(request):
    return render(request, 'index.html', context={
        'author': AuthorInfo.objects.first(),
    })