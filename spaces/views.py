from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Workspaces, Bookings
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
import json
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages

# Create your views here.

def search_res(request):
    city = request.POST['search']
    city = city.capitalize()
    res = get_list_or_404(Workspaces,city=city)
    context = {'res':res}
    return render(request,'spaces/search.html',context)

def home(request):
    city = {s.city for s in Workspaces.objects.all()}
    city = list(city)
    city = json.dumps(city)
    return render(request,'spaces/home.html',{'city':city})

def detail(request,pk):
    res = get_object_or_404(Workspaces,id=pk)
    context = {'results':res}
    return render(request,'spaces/detail.html',context)

@login_required
def book(request,pk):
    res = Workspaces.objects.get(id=pk)
    cb = Bookings.objects.filter(user_booked=request.user).filter(booked_space=res)
    c=[]
    for a in cb:
        if a.booking_date > datetime.date.today():
            c.append(a)
    if c:
        return render(request,'spaces/book.html',{'c':c})
    else:
        return render(request,'spaces/book.html',{'res':res})

def booked(request):
    if request.method == "POST":
        book_date = request.POST['booking_date']
        work_id = request.POST['space_id']
        book_date = parse_date(book_date)
        w1 = Workspaces.objects.get(id=work_id)
        b1 = Bookings(booking_date=book_date, booked_space=w1, user_booked = request.user)
        b1.save()
        context = {'res':w1,'date':book_date}
        return render(request,'spaces/booked.html',context)

@login_required
def your_bookings(request):
    b = Bookings.objects.filter(user_booked=request.user).order_by('booking_date')
    curr_date = datetime.datetime.now().date()
    prev_date = []
    next_date = []
    for x in b:
        if x.booking_date <= curr_date:
            prev_date.append(x)
        else:
            next_date.append(x)
    return render(request,'spaces/your_bookings.html',{'res_prev':prev_date,'res_next':next_date})

def delete_booking(request,pk):
    if Bookings.objects.filter(id=pk).delete():
        messages.success(request, "Deleted successfully.")
        return redirect('your_bookings')
    else:
        messages.warning(request, "Error occurred. Please Try Again")
        return redirect('your_bookings')





