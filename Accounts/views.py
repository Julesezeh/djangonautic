from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout

#from django.http import HttpResponse


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('particular:articles')
    else:    
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'ferm':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('particular:articles')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('particular:articles')