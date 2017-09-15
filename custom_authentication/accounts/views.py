from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def index(request):
    """A view that displays the index page"""
    return render(request, 'index.html')


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                next_page = request.GET.get('next', reverse('profile'))
                return redirect(next_page)
            else:
                user_form.add_error(None,
                                    "Your username or password are incorrect")

    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    args.update(csrf(request))
    return render(request, 'register.html', args)
