from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import extendeduser

# Create your views here.
def register(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['surname']
        uname = request.POST['username']
        phnum = request.POST['phone']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        dob = request.POST['dob']
        gender = request.POST['gender']

        if pwd1 == pwd2:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username has already been taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This e-mail is already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, username=uname, email=email, password=pwd1)
                user.save()
                newextendeduser = extendeduser(phone_num=phnum, date_of_birth=dob, gender=gender, user=user)
                newextendeduser.save()
                messages.info(request, 'successfully registered')
                return redirect('home')
        else:
            messages.info(request, 'Not matching passwords')
            return redirect('register')
    else:
        return render(request, 'login.html')

def logout(request):
    return render(request, 'login.html')