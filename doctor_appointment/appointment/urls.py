from django.urls import path
from appointment.views import *
from django.conf import settings
from django.conf.urls.static import static
from appointment import views


app_name = 'appointment'

urlpatterns = [

    path('doctor/appointment/create', AppointmentCreateView.as_view(), name='doctor-appointment-create'),
    path('doctor/appointment/', AppointmentListView.as_view(), name='doctor-appointment'),
    path('patient/', PatientListView.as_view(), name='patient-list'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)