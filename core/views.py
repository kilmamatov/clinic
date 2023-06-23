from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, View, DetailView, UpdateView, CreateView, DeleteView
from core import models
from core import forms
from datetime import datetime, timedelta


class Index(TemplateView):
    template_name = 'core/index.html'


class DoctorList(ListView):
    template_name = 'core/doctor_list.html'
    model = models.Doctor
    context_object_name = 'queryset'


class DoctorDetail(DetailView):
    template_name = 'core/doctor.html'
    model = models.Doctor
    context_object_name = 'doctor'


class AppealsList(ListView):
    template_name = 'core/appeals_list.html'
    model = models.Appeal
    context_object_name = 'queryset'


class AppealDetail(DetailView):
    template_name = 'core/appeal.html'
    model = models.Appeal
    context_object_name = 'appeal'


class AppealDelete(DeleteView):
    model = models.Appeal
    success_url = reverse_lazy('appeals')


class AppealUpdate(UpdateView):
    model = models.Appeal
    form_class = forms.Appeal
    template_name = 'core/appeal_update.html'
    success_url = reverse_lazy('appeals')

    def form_valid(self, form):
        doctor = form.cleaned_data['doctor']
        appeal_date = form.cleaned_data['appeal_date']
        appeal_time = form.cleaned_data['appeal_time']
        start_time = datetime.combine(appeal_date, appeal_time) - timedelta(minutes=14)
        end_time = datetime.combine(appeal_date, appeal_time) + timedelta(minutes=14)
        if models.Appeal.objects.filter(
                doctor=doctor,
                appeal_date=appeal_date,
                appeal_time__gte=start_time.time(),
                appeal_time__lte=end_time.time()
        ).exists():
            return render(self.request, 'core/appeal_add.html', {
                'form': form,
                'message': 'Обращение на указанное время уже существует'
            }
                          )
        return super().form_valid(form)


class AppealCreate(CreateView):
    template_name = 'core/appeal_add.html'
    form_class = forms.Appeal
    success_url = reverse_lazy('appeals')

    def form_valid(self, form):
        doctor = form.cleaned_data['doctor']
        appeal_date = form.cleaned_data['appeal_date']
        appeal_time = form.cleaned_data['appeal_time']
        start_time = datetime.combine(appeal_date, appeal_time) - timedelta(minutes=14)
        end_time = datetime.combine(appeal_date, appeal_time) + timedelta(minutes=14)
        if models.Appeal.objects.filter(
                doctor=doctor,
                appeal_date=appeal_date,
                appeal_time__gte=start_time.time(),
                appeal_time__lte=end_time.time()
        ).exists():
            return render(self.request, 'core/appeal_add.html', {
                'form': form,
                'message': 'Обращение на указанное время уже существует'
            }
                          )
        return super().form_valid(form)








