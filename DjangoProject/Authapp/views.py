from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Authapp.forms import UserForm, UserInfoForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'Authapp/index.html')


def registeration(request):
    registered = False
    userform = UserForm
    userinfoform = UserInfoForm
    if request.method == 'POST':
        userform = UserForm(data=request.POST)
        userinfoform = UserInfoForm(data=request.POST)

        if userform.is_valid() and userinfoform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = userinfoform.save(commit=False)
            profile.user = user
            registered = True

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES['profile_pics']
                profile.save()
    else:
        userform = UserForm()
        userinfoform = UserInfoForm()

    return render(request,'Authapp/registeration.html', {'userform':userform,
                                                         'userinfoform':userinfoform,
                                                         'registered':registered})

def login_page(request):

    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')

        user = authenticate(username=username,password=password)

        if  user:
            login(request,user)

            return HttpResponseRedirect(reverse('index'))
        else:
            print('some tried to hack')
            return HttpResponse('fawk')

    return render(request,'Authapp/login_page.html')



def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
