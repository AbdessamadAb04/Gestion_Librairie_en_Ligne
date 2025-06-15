from ast import NameConstant
from multiprocessing import context
from django.shortcuts import render,redirect


from .models import product
from .forms import productForm

# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url='/session/')
def home(request):
      pro_data=product.objects.all()[:3]
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  pro_data
            else:
                  pro_data=product.objects.filter(nom =Search)
      
      
      
      countdt = product.objects.count()
      current_user=request.user
      user_id=current_user.id
      print(user_id)
      
      return render(request,"product/home.html",{'prodata':pro_data,'countdt': countdt,'user_id':user_id})
    
from django.urls import reverse

@login_required(login_url='/session/')
def book(request):
      pro_data=product.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  pro_data
            else:
                  
                  pro_data=product.objects.filter(nom =Search)
      
      countdt = product.objects.count()
      return render(request,"product/book.html", {'countdt': countdt, 'prodata': pro_data})

@login_required(login_url='/session/')
def create(request):
      form=productForm
      if request.method == 'POST':
            form=productForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect(reverse('book'))  # 4
      else:
       return render(request,"product/create.html",{'form':form})
       
@login_required(login_url='/session/')
def delete(request,id):
      pro_data=product.objects.get(id=id)
      pro_data.delete()
      return redirect(reverse('book'))

@login_required(login_url='/session/')
def update(request,id):
      pro_data=product.objects.get(id=id)
      form=productForm(instance=pro_data)
      if request.method == 'POST':
            form=productForm(request.POST,instance=pro_data)
            if form.is_valid():
                  form.save()
            return redirect(reverse('book'))  # 4
      else:
       return render(request,"product/update.html",{'form':form})
@login_required(login_url='/session/')
def create(request):
      form=productForm
      if request.method == 'POST':
            form=productForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect(reverse('book'))  # 4
      else:
       return render(request,"product/create.html",{'form':form})
       
@login_required(login_url='/session/')
def delete(request,id):
      pro_data=product.objects.get(id=id)
      pro_data.delete()
      return redirect(reverse('book'))

@login_required(login_url='/session/')
def update(request,id):
      pro_data=product.objects.get(id=id)
      form=productForm(instance=pro_data)
      if request.method == 'POST':
            form=productForm(request.POST,instance=pro_data)
            if form.is_valid():
                  form.save()
            return redirect(reverse('book'))  # 4
      else:
       return render(request,"product/update.html",{'form':form})

