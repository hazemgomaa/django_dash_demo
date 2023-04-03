from django.shortcuts import render


def display_home(request):
    # hello
    return render(request, "index.html")
