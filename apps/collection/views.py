from django.shortcuts import render

def collection_view(request):
    return render(request, 'collection.html')