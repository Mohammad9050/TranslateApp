from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)

            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'account/sign_up.html', context)


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context['error']= 'username or password is wrong'
            return render(request, 'account/login.html', context)
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
