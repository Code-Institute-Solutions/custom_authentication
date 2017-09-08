from django.shortcuts import render


def get_index(request):
    """A view that displays your homepage"""
    return render(request, 'index.html')