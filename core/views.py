from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
# class SignupView(views):
#     def get(self, request):
#         # if request.method =="GET":
#         return render(request,'signup.html',)


from django.shortcuts import render, redirect
from .form import RegisterForm
# from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import authenticate, login, logout

class SignupView(View):
    def get(self,request):
        # if response.
        fm = RegisterForm()
        return render(request, 'core/signup.html',{"form":fm})
    def post(self,request):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("login")
        else:
            form = RegisterForm()
        return render(response, "core/signup.html", {"form":fm})

# from django.contrib.auth.forms import AuthenticationForm

# class UsewrLogin(view):
#     def

# def user_login(request):
#     import pdb;pdb.set_trace()
    
#     if request.method == "POST":
#         fm = AuthenticationForm(request=request,data=request.POST)
#         if fm.is_valid():
#             uname = fm.cleaned_data['email']
#             upass = fm.cleaned_data['password']
#             user=authenticate(email=uname, password=upass)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('/profile/')

#     else:

#         fm = AuthenticationForm()
#     return render (request,'core/login.html',{'form':fm})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('home')    
        else:
            message = "Wrong username and password"
        return render(request,'login.html',{'error': message })
    if request.method =="GET":
        return render(request,'login.html')

def user_profile(request):
    return render(request, 'core/profile.html')