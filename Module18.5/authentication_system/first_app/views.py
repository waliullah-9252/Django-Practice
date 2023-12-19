from django.shortcuts import render,redirect
from .forms import RegisterForm,UpdateUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            sign_up_form = RegisterForm(request.POST)
            if sign_up_form.is_valid():
                messages.success(request, 'Your account has been created successfully')
                sign_up_form.save()
                return redirect('user_login')
        else:
            sign_up_form = RegisterForm()
        return render(request, 'sign_up.html', {'form': sign_up_form , 'type': 'SignUp'})
    else:
        return redirect('user_profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request = request, data = request.POST)
            if login_form.is_valid():
                user_name = login_form.cleaned_data['username']
                user_pass = login_form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_pass)
                if user is not None:
                    messages.success(request, 'Logged In successfully')
                    login(request, user)
                    return redirect('user_profile')
            else:
                messages.warning(request, 'Login Information is Incorrect')
                return redirect('sign_up')
        else:
            login_form = AuthenticationForm()
            return render(request, 'sign_up.html', {'form': login_form, 'type' : 'Login'})
    else:
        return redirect('user_profile')
    
def user_logout(request):
    messages.success(request, 'Logged Out successfully')
    logout(request)
    return redirect('homepage')


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Profile updated successfully')
                form.save()
                return redirect('user_profile')
        else:
            form = UpdateUserForm(instance = request.user)
        return render(request, 'profiles.html', {'form': form})
    else:
        return redirect('user_login')

def user_change_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            update_form = UpdateUserForm(request.POST, instance=request.user)
            if update_form.is_valid():
                messages.success(request, 'Profile updated successfully')
                update_form.save()
                return redirect('user_profile')
        else:
            update_form = UpdateUserForm(instance = request.user)
        return render(request, 'profiles.html', {'form': update_form})
    else:
        return redirect('user_login')


def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass_change = PasswordChangeForm(user= request.user, data = request.POST)
            if pass_change.is_valid():
                messages.success(request, 'Password has been changed successfully')
                pass_change.save()
                update_session_auth_hash(request, pass_change.user)
                return redirect('user_profile')
        else:
            pass_change = PasswordChangeForm(user= request.user)
        return render(request, 'passchange.html', {'form': pass_change})
    else:
        return redirect('user_login')


def password_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass_change = SetPasswordForm(user= request.user, data = request.POST)
            if pass_change.is_valid():
                messages.success(request, 'Password has been changed successfully')
                pass_change.save()
                update_session_auth_hash(request, pass_change.user)
                return redirect('user_profile')
        else:
            pass_change = SetPasswordForm(user= request.user)
        return render(request, 'passchange.html', {'form': pass_change})
    else:
        return redirect('user_login')