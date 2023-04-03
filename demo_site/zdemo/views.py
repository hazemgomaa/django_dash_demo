from django.shortcuts import render


def display_home(request):
    # hello again
    return render(request, "index.html")
