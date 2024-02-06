from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def Index(request):
    return render(request,'app/index.html')
def Login(request):
    if request.method=='POST':
        name=request.POST['name']
        pswd=request.POST['password']
        try:
                 cust=Customer.objects.get(name=name,password=pswd)
                 request.session['customer']=cust.id
                 return redirect('app:dashboard')
        except Customer.DoesNotExist:
                 return render(request,'app/login.html',{'msg':'invalid username or password'})
    return render(request,'app/login.html')
def Signup(request):
    return render(request,'app/signup.html')
def Dashboard(request):
    if 'customer' in request.session:
        return render(request,'app/dashboard.html')
    else:
        return render(request,'app/error.html')
def Cart(request):
    return render(request,'app/cart.html')
def Payment(request):
    return render(request,'app/payment.html')
def Error(request):
    return render(request,'app/error.html')
def logout(request):
     if 'customer' in request.session:
          del request.session['customer']
          return redirect('app:index')