from django.shortcuts import render,get_list_or_404
from django.contrib.auth.models import User
# Create your views here.
def DoctorList(request):

    doctors = get_list_or_404(User)

    return render(request,'doctor/doctor_list.html',{
        'doctors':doctors
    })