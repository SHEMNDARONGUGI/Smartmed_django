from django import forms 
from Smart_Healthapp.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        
# class ImageUploadForm(forms.ModelForm):
#     class Meta:
#         model = ImageModel
#         fields = ['image','title','price']
        
