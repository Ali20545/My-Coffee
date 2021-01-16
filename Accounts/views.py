from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.

def signin(request):
    return render(request, 'Accounts/signin.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password'] 
        comfirm_password = request.POST['comfirm_password']

        if password == comfirm_password:
            if User.objects.filter(username='username').exists():
                messages.error(request, 'username  alredy exists!')
                return redirect('signup')
            else:
                if User.objects.filter(email='email').exists():
                    messages.error(request, 'Email alredy exists!')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('signup')
                    user.save()
                    messages.success(request, 'You are registered successfully')
                    return('signin')
        else:
            messages.error(request, 'Password not match')
            return redirect('signup')
    else:
        return render(request, 'Accounts/signup.html')

def logout(reuest):
    return redirect('home')

def profile(request):
    return render(request, 'Accounts/profile.html')