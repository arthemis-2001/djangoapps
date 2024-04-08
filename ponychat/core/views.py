"""
Module containing views for handling HTTP requests and rendering HTML templates.

Functions:
- frontpage(request): Renders the front page HTML template.
- signup(request): Handles user signup and renders a signup form.
"""

from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

# Create your views here.
def frontpage(request):
    """
    Function that renders the front page HTML template.

    Parameters:
    - request: the HTTP request object

    Returns:
    - the rendered front page HTML
    """
    return render(request, "core/frontpage.html")

def signup(request):
    """
    A function that handles user signup. 
    Takes a request object as a parameter. 
    Returns a rendered HTML page with a signup form.
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("frontpage")
    else:
        form = SignUpForm()  
    return render(request, "core/signup.html", {"form": form})
