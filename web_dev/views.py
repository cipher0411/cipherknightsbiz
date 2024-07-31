# Inside web_dev/views.py
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm, UserPasswordChangeForm
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .forms import ContactForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Contact,Profile
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
import random
from django.views import View
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone




User = get_user_model()



def index(request):
    return render(request, 'web_dev/index.html')

def about(request):
    return render(request, 'web_dev/about.html')

def dashboard(request):
    return render(request, 'web_dev/dashboard.html')


def contact(request):
    return render(request, 'web_dev/contact.html')

def cookie(request):
    return render(request, 'web_dev/cookie.html')

def design(request):
     return render(request, 'web_dev/design.html')

def request_demo(request):
    # Add your logic here
    return render(request, 'web_dev/demo.html')


def web_development(request):
    return render(request, 'web_dev/web_development.html')

def school_project(request):
    return render(request, 'web_dev/school_project.html')

def sale_of_accessories(request):
    return render(request, 'web_dev/sale_of_accessories.html')

def terms_and_conditions_view(request):
    return render(request, 'web_dev/terms_and_conditions.html')



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return redirect('register')
            user.set_password(password1)
            user.save()
            auth_login(request, user)
            messages.success(request, 'You have successfully created an account and logged in!')
            return redirect('index')  # Redirect to the index page
        else:
            if form.errors.get('email'):
                messages.error(request, 'This email address is already registered.')
    else:
        form = UserRegistrationForm()

    return render(request, 'web_dev/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')
        else:
            messages.error(request, 'Invalid form input.')
    else:
        form = UserLoginForm()
    return render(request, 'web_dev/login.html', {'form': form})



@login_required
def profile(request):
    user = request.user
    return render(request, 'web_dev/profile.html', {'user': user})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        password_form = UserPasswordChangeForm(request.user, request.POST)
        
        if form.is_valid() and password_form.is_valid():
            form.save()
            password_form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        password_form = UserPasswordChangeForm(request.user)
        
    return render(request, 'web_dev/update_profile.html', {'form': form, 'password_form': password_form})



def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('index')







def my_view(request):
    url = reverse('web_dev:index')
    return HttpResponseRedirect(url)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_admin_view(request):
    users = User.objects.all()
    return render(request, 'admin/user_admin.html', {'users': users})


@csrf_protect
def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Here you can add validation logic if needed
        if not first_name or not last_name or not email or not message:
            return render(request, 'web_dev/contact.html', {
                'error': 'All fields except phone are required.',
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'message': message,
            })

        # Save the data to the database
        contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone, message=message)
        contact.save()

        # Redirect back to contact page with a success message
        return render(request, 'web_dev/contact.html', {
            'success_message': 'Thank you for your message. We will get back to you soon.'
        })

    return render(request, 'web_dev/contact.html')



#Forgot Password OTP


class ForgotPasswordView(View):
    def get(self, request):
        # Clear the session if it exists
        if 'email' in request.session:
            del request.session['email']
        return render(request, 'web_dev/forgot_password.html')

    def post(self, request):
        try:
            email = request.POST.get('email')
            user = User.objects.get(email=email)
            profile, created = Profile.objects.get_or_create(user=user)
            
            # Generate OTP and set its expiration time
            otp = random.randint(100000, 999999)
            profile.otp = otp
            profile.otp_created_at = timezone.now()
            profile.save()
            
            # Send OTP via email
            send_mail(
                'Password Reset OTP',
                f'Your OTP for password reset is {otp}. This OTP is valid for 5 minutes.',
                'cipherknights@cipherknights.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, f'OTP sent successfully to {email}.')
            request.session['email'] = email  # Store the email in session for verification
            return redirect('verify_otp')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('forgot_password')
        except Exception as e:
            messages.error(request, f'Failed to send OTP. Error: {e}')
            return redirect('forgot_password')
        
        
        

class VerifyOTPView(View):
    def get(self, request):
        return render(request, 'web_dev/verify_otp.html')

    def post(self, request):
        otp = request.POST.get('otp')
        email = request.session.get('email')
        if not email:
            return redirect('forgot_password')
        try:
            user = User.objects.get(email=email)
            profile = Profile.objects.get(user=user)
            if profile.otp == int(otp) and profile.is_otp_valid():
                # OTP is valid, proceed to reset password
                request.session['otp_verified'] = True  # Mark OTP as verified
                return redirect('reset_password')
            else:
                if not profile.is_otp_valid():
                    messages.error(request, 'OTP has expired. Please request a new OTP.')
                else:
                    messages.error(request, 'Invalid OTP')
                return redirect('verify_otp')
        except User.DoesNotExist:
            messages.error(request, 'User not found.')
            return redirect('forgot_password')







class ResetPasswordView(View):
    def get(self, request):
        # Check if OTP was verified
        if not request.session.get('otp_verified'):
            return redirect('forgot_password')
        return render(request, 'web_dev/reset_password.html')

    def post(self, request):
        email = request.session.get('email')
        if not email:
            return redirect('forgot_password')
        user = User.objects.get(email=email)
        password = request.POST['password']
        user.set_password(password)
        user.save()
        messages.success(request, 'Password reset successful.')
        
        # Clear the session email and otp_verified after successful password reset
        del request.session['email']
        del request.session['otp_verified']
        return redirect('login')

    

    
    
    
