from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def register_seller_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "You have registered successfully!")

            return redirect('seller:seller_login')
        else:
            messages.success(request, "Oops! There was an error registering your account! Please try again")
            return redirect('seller:seller_register')
    else:
        form = SignUpForm()
        return render(request, 'seller_html/seller_register.html', {'form': form})


@login_required
def login_seller_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard_index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In!")
            return redirect('dashboard:dashboard_index')
        else:
            messages.error(request, "There was an error logging in! Please try again.")
            return redirect('seller:seller_login')
    else:
        return render(request, 'seller_html/seller_login.html')


def logout_seller_view(request):
    logout(request)
    messages.success(request, "You have been Logged out! Thanks for stopping by..")
    return redirect('seller:seller_login')
