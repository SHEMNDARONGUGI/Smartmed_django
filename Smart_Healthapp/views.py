import json

from django.http import HttpResponse
from django.shortcuts import render, redirect


# from Smart_Healthapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from Smart_Healthapp.models import Contact, Appointment, Member
from Smart_Healthapp.forms import AppointmentForm

def index(request):
    if request.method == 'POST':
        if User.objects.filter(
            username = request.POST['username'],
            password = request.POST['password']
            
        ).exists():
            return render(request, 'index.html')
        
        else:
            return render(request, 'login.html')
        
    else:
        return render(request, 'login.html')
            
    

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def myservice(request):
    return render(request, 'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def appointment(request):
    if request.method == 'POST':
        myappointments = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date  = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            Message = request.POST['message']
            
        )
        myappointments.save()
        return redirect('/appointment')
    
    else:
        return render(request, 'appointment.html')

def show(request):
   allappointments = Appointment.objects.all()
   return render(request, 'show.html', {'appointment':allappointments})

def delete(request, id):
    appoint = Appointment.objects.get(id = id)
    appoint.delete()
    return redirect('/show')

def contact(request):
    if request.method == 'POST':
        mycontact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontact.save()
        return redirect('/contact')
    
    else:
         return render(request, 'contact.html')
     
     
def showcontact(request):
   allcontacts = Contact.objects.all()
   return render(request, 'showcontact.html', {'contact':allcontacts})

def edit(request, id):
    editappointment = Appointment.objects.get(id = id)
    return render(request, 'edit.html', {'appointment': editappointment})


def update(request, id):
    updateappointment = Appointment.objects.get(id = id)
    form = AppointmentForm(request.POST,instance = updateappointment)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html')
    
    

        
#     else:
#         return render(request, 'edit.html')

# def update(request, id):
    """
    The function `update` in Python is used to update appointment information based on a given request
    and appointment ID.
    
    :param request: The `request` parameter in the `update` function is typically an object that
    contains information about the current HTTP request. It includes details such as the request
    method (GET, POST, etc.), any data sent with the request (form data, parameters), user session
    information, and more. In Django
    :param id: The `id` parameter in the `update` function is typically used to identify the specific
    object or record that needs to be updated. In this case, it seems like the function is designed to
    update an appointment object with the given `id`. The function retrieves the appointment object
    based on the `id
    """
#     updateinfo = get_object_or_404(Appointment, id=id)
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST, instance=updateinfo)
#         if form.is_valid():
#             form.save()
#             return redirect('show')  # Redirect to your listing or confirmation page
#     else:
#         form = AppointmentForm(instance=updateinfo)
#     return render(request, 'edit.html', {'form': form, 'appointment': updateinfo})

def register(request):
    if request.method == 'POST':
        members = User(
            name = request.POST['name'],
            username = request.POST['username'],
            password =request.POST['password']
        )
        members.save()
        return redirect('/login')
    
    else:
        return render(request, 'register.html')
    

def login(request):
    return render(request, 'login.html')

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/showimage')
#     else:
#         form = ImageUploadForm()
#     return render(request, 'upload_image.html', {'form': form})

# def show_image(request):
#     images = ImageModel.objects.all()
#     return render(request, 'show_image.html', {'images': images})


def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")


        
        



    







