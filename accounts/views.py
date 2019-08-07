from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form' : form })

def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')