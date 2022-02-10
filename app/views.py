from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def insertPageView(request):
    return render(request, 'app/insert.html')

def insertData(request):
    # data from html to view
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        # Create a Student object
        newuser = Student.objects.create(Firstname=fname, Lastname=lname, Email=email, Contact=contact)        
        # After inserting render showPageView
        return redirect('show')

# show data in table format
def showPageView(request):
    # select * from table
    # fetching all data from student table
    all_data = Student.objects.all()
    return render(request, 'app/show.html', {'key1': all_data})

def editPage(request,pk):
    # fetching data of particular id
    get_data = Student.objects.get(id=pk)
    return render(request, 'app/edit.html', {'key2': get_data})

# update dataView
def updateData(request, pk):
    if request.method == 'POST':
        udata = Student.objects.get(id=pk)
        udata.Firstname = request.POST['fname']
        udata.Lastname = request.POST['lname']
        udata.Email = request.POST['email']
        udata.Contact = request.POST['contact']
        # query to update data
        udata.save()
        return redirect('show')

def deleteData(request, pk):
    d_data = Student.objects.get(id=pk)
    # query to delete data
    d_data.delete()
    return redirect('show')