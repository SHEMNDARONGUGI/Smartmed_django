
from django.contrib import admin
from django.urls import path
from Smart_Healthapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('index/', views.index, name='index'),
    
    path('myservice/', views.myservice, name='service'),
    
    path('starter/', views.starter, name='start'),
    
    path('about/', views.about, name='about'),
    
    path('doctors/', views.doctors, name='doctors'),
    
    path('appointment/', views.appointment, name='appointment'),
    
    path('contact/', views.contact, name='contact'),
    
    path('show/', views.show, name='show'),
    
    path('showcontact/', views.showcontact, name='showcontact'),
    
    path('delete/<int:id>/', views.delete, name='delete'),
    
    path('edit/<int:id>/', views.edit, name='edit'),
    
    

    path('update/<int:id>/', views.update, name='update'),  # This will match '/update/8/'
    path('update/<int:id>', views.update, name='update_no_slash'),  # This will match '/update/8' without a slash


    
    path('', views.register, name='register'),
    
    path('login/', views.login, name='login'),
    
    # path('uploadimage/', views.upload_image, name='upload'),
    
    # path('showimage/', views.show_image, name='image'),
    
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
  
    
]
