from django.shortcuts import render


def index(request):
    """
        Viewe returns index page
    """
    return render(request, 'home/index.html')
