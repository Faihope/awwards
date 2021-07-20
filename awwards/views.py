from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as dj_login
from django.urls import reverse


# Create your views here.
def index(request):


    return render(request,'index.html')

def registeruser(request):
    title = 'Register - awwards'
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('loginpage')
    else:
        form = CreateUserForm
    context = {
            'title':title,
            'form':form,
                        }
    return render(request, 'registration/register.html', context)

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=  request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse('welcome'))
        else:
            messages.info(request,'Username or password is incorrect')
       
    context={}
    return render(request,'registration/login.html',context)