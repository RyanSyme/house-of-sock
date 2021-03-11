from django.shortcuts import render


def index(request):
    """
        View returns index page
    """
    return render(request, 'home/index.html')
