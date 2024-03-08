from django.contrib import admin
from django.urls import path, include
from .views import select_role, staff_login, patient_login, admin_login, patient_signup, patient_dash, invoice

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', select_role, name='select_role'),
    path('login/staff/', staff_login, name='staff_login'),
    path('login/patient/', patient_login, name='patient_login'),
    path('login/admin/', admin_login, name='admin_login'),
    path('signup/patient/', patient_signup, name='patient_signup'), 
    path('patientdashboard', patient_dash, name='patient_dash'),
    path('invoice', invoice, name='invoice'),
    

]