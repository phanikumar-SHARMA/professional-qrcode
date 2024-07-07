from django.shortcuts import render, redirect
from .dataqr import generate_QR, display_data
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'intro/index.html')

def generate_qr(request):
    if request.method == 'POST':
        data = [
            request.POST['name'],
            request.POST['age'],
            request.POST['gender'],
            request.POST['address'],
            request.POST['contact'],
            request.POST['fname'],
            request.POST['mname'],
            request.POST['hobbies'],
            request.POST['skills'],
            request.POST['work'],
            request.POST['education'],
        ]
        generate_QR(data)
        pData = display_data(data)
        request.session['pData'] = pData  # Store pData in session
        return HttpResponseRedirect(reverse('qr_display'))  # Redirect to the QR display page

def qr_display(request):
    pData = request.session.get('pData', None)  # Retrieve pData from session
    return render(request, 'intro/qr_display.html', {'pData': pData})
