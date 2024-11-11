from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from clinicalsApp.forms import ClinicalDataForm
from clinicalsApp.models import ClinicalData
from clinicalsApp.models import Patient
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

# Create your views here.
# Class based views to perform CRUD operations on Patient model.
class PatientListView(ListView):
    """ GET method """
    model = Patient


class PatientCreateView(CreateView):
    """ POST method """
    model = Patient
    success_url = reverse_lazy('index')
    fields = {'firstName', 'lastName', 'age'}


class PatientUpdateView(UpdateView):
    """ PATCH method """
    model = Patient
    success_url = reverse_lazy('index')
    fields = {'firstName', 'lastName', 'age'}


class PatientDeleteView(DeleteView):
    """ DELETE method """
    model = Patient
    success_url = reverse_lazy('index')


def addData(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalsApp/clinicaldata_form.html', {'form': form, 'patient': patient})


def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            heightAndWeight = eachEntry.componentValue.split('/')
            if len(heightAndWeight) > 1:
                feetToMeters = float(heightAndWeight[0])*0.4536
                BMI = (float(heightAndWeight[1]))/(feetToMeters*feetToMeters)
                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValue = BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)

    return render(request, 'clinicalsApp/generateReports.html', {'data': responseData})