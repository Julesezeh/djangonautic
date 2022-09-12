from django.shortcuts import render
from ass1.forms import Reg
from ass1.models import Member
# Create your views here.
def signup(request):
    formal = Reg()
    if request.method=="POST":
        formal = Reg(request.POST)
        if formal.is_valid():
            formal = formal.save(commit=True)
            print("Sign-Up Complete")
            print("Welcome ")
            return reindex(request)
            

    return render(request,'forms.html',{'form':formal})

def reindex(request):
    return render(request,'homepage.html')


def customers(request, slug):
    customer = Member.objects.get(id=slug)
    return render(request,'customer.html',{'customer':customer})