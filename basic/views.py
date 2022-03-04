
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib import use
from basic.forms import UserForm, UserModelForm


from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(req):
    return render(req, 'temp_for_basic/index.html')

def register(req):

    if req.method == "POST":
        user_form = UserForm(data=req.POST)
        profile_form = UserModelForm(data=req.POST)
        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'dp' in req.FILES:
                profile.dp = req.FILES['dp']
            profile.save()
            return home(req)
        else:
            print("Enter Valid information")

    return render(req, 'temp_for_basic/register.html', {'userform': UserForm, 'modelform': UserModelForm})

def user_login_page(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(username= username, password=password)

        if user:
            if user.is_active:
                login(req, user)
                return home(req)
            else:
                return render(req, 'temp_for_basic/login.html', {'try_again': "Account not active!"})
        else:
            return render(req, 'temp_for_basic/login.html', {'try_again': "Invalid username or password. Try agian!"})
        

    else:
        return render(req, 'temp_for_basic/login.html', {"try_again": ""})

@login_required
def user_logout(req):
    logout(req)
    return home(req)

@login_required
def trash(req):
    return HttpResponse("i guess you're logged in!")