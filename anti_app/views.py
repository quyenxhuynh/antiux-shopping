from django.shortcuts import render, redirect
from django.views import generic
from .models import Item
import time as t
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
import random, string
from django.contrib.auth.decorators import login_required

t0 = None
ans = ['Jersey Shacket', 'Vintage Straight High Jeans', 'Long Hoodie', 'Cable-knit Sweater', 'Fine-knit Sweater', 'Flock-print Hoodie', 'Wrapover-back Sweater']

class Cart(generic.ListView):
    # model = Item
    template_name = 'anti_app/cart.html'
    context_object_name = 'cart_list'

    def get_queryset(self):
        return Item.objects.filter(in_cart=True)

def start(request):
    return render(request, 'anti_app/base.html')

def create(request):
    global t0
    t0 = t.time()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            acc = User.objects.get(username=username)
            password = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(16)])
            acc.set_password(password)
            acc.save()
            lol = password
            messages.info(request, "hope you're paying attention... your new password is " + lol)
            return redirect('anti-instructions')
    else:
        form = CreateUserForm()
    return render(request, 'anti_app/create.html', {'form': form})

@login_required
def time(request):
    global t0

    for item in Item.objects.all():
        item.in_cart = False
        item.save()

    context = {'time':t.time() - t0}
    return render(request, 'anti_app/time.html', context)

def test(request):
    return render(request, 'anti_app/test.html')

def instructions(request):
    return render(request, 'anti_app/instructions.html')

def items(request):
    return render(request, 'anti_app/items.html')

def store(request):
    items = Item.objects.all()
    context = {'items': items}

    return render(request, 'anti_app/store.html', context)

def check_cart(request):
    logout(request)
    count = 0
    for item in Item.objects.filter(in_cart=True):
        count += 1
        if item.item_name not in ans:
            messages.info(request, 'Something shouldn\'t be in the cart. Try again!')
            return redirect('anti-cart')
    if count != 7:
        messages.info(request, 'Wrong number of items')
        return redirect('anti-cart')
   
    return redirect('checkout')

def cart(request):
    return render(request, 'anti_app/cart.html')

def checkout(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        log = authenticate(request, username=username, password=password)
        if log is not None:
            login(request, user)
            redirect('anti-time')
        else:
            messages.info(request, 'Oops! Couldn\'t log you in. Try again?')
            redirect('anti-checkout')

    return render(request, 'anti_app/checkout.html')

def empty(request):
    for item in Item.objects.all():
        item.in_cart = False
        item.save()
    return render(request, 'anti_app/cart.html')

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        item = Item.objects.get(item_name = name)
        item.in_cart = True
        item.save()
    return redirect('anti-cart')