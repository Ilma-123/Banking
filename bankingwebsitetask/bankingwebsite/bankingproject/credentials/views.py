from django.http import JsonResponse
from django.contrib.auth import authenticate, login as django_login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Branch, District, Customer
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import get_messages, add_message


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        login_messages = messages.get_messages(request)
        if user is not None:
            django_login(request, user)
            return redirect('newpage')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html', {'login_messages': login_messages})

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['password1']

        if password != confirm_password:
            add_message(request, messages.ERROR, 'Passwords do not match.')
        else:
            if User.objects.filter(username=username).exists():
                add_message(request, messages.ERROR, 'Username already exists.')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                add_message(request, messages.SUCCESS, 'Registration successful. You can now log in.')

                return render(request, 'register.html', {'redirect_delay': True})

    return render(request, 'register.html')


def redirect_register(request):
    return redirect('login')


def newpage(request):
    form_visible = False
    success_message = ''
    form = RegistrationForm()
    districts = District.objects.all()

    if request.method == 'GET' and 'show-form' in request.GET:
        form_visible = True

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = 'Form submission successful!'
            form_visible = False
            form = RegistrationForm()  # Reset the form after successful submission
        else:
            form_visible = True  # Show the form again with errors
            success_message = ''
    # Manually adding the district names
    district_names = ["Ernakulam", "Thrissur", "Kollam", "Kozhikode"]

    context = {
        'form_visible': form_visible,
        'form': form,
        'districts': districts,
        'success_message': success_message,
        'district_names': district_names,
    }

    return render(request, 'newpage.html', context)


def register_customer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact')
        address = request.POST.get('address')
        dob = request.POST.get('DOB')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        if username and email and contact_number and address and dob and age and gender:

            print("saving coustomer")
            customer = Customer(
                username=username,
                password=password,
                email=email,
                contact_number=contact_number,
                address=address,
                dob=dob,
                age=age,
                gender=gender
            )
            customer.save()
            print("coustomer saved")
            messages.add_message(request, messages.SUCCESS, 'Form submission successful!')
            print("succes message")

        else:

            messages.add_message(request, messages.ERROR, 'Form submission failed. Please check the form fields.')
            print("error message")
        districts = District.objects.all()
        context = {
            'form_visible': True,
            'districts': districts,
        }

        return render(request, 'newpage.html', context)


def fetch_branches(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).values('name', 'id')
    return JsonResponse(list(branches), safe=False)


def show_form(request):
    return redirect('newpage')


def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
    return render(request, 'index.html')
