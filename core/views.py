from django.shortcuts import render,redirect,get_object_or_404
from .models import ContactMessage, Products
from django.contrib import messages
import base64

# Create your views here.
def home(request):
    if request.user_agent.is_mobile:
        return render(request,'core/mobile_home.html')
        
    else:return render(request, 'core/home.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(name=name,email=email,message=message)
            messages.success(request, 'Your comment has been received. Thank you!')
            return redirect('contact')
        else:
            message.error(request,'Please fill all the fields')
    if request.user_agent.is_mobile:
        template='core/mobile_contact.html'
    else:
        template='core/contact.html'
    return render(request,template)

def shop(request):
    category_list=['laptops','desktops','printers','accessories']
    encoded_category=request.GET.get('category')
    category=None

    if encoded_category:
        try:
            category=base64.b64decode(encoded_category).decode('utf-8')

        except:
            category=None

    products=Products.objects.filter(category=category) if category else Products.objects.all()
    
    if request.user_agent.is_mobile:
        template='core/mobile_shop.html'
    else:
        template='core/shop.html'
    return render(request, template,{
        'products':products,
        'active_category':category,
        "category_list":category_list
    })

def product_details(request,slug):
    product=get_object_or_404(Products,slug=slug)
    if request.user_agent.is_mobile:
        template='core/mobile_product_details.html'
    else:
        template='core/product_details.html'
    return render(request,template,{'product':product})

def about_us(request):
    if request.user_agent.is_mobile:
        return render(request, 'core/mobile_about_us.html')
    else:
        return render(request, 'core/about_us.html')