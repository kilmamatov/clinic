from django.db import models
from django.utils import timezone


class Doctor(models.Model):
    name = models.CharField('Имя', max_length=255)
    specialization = models.CharField('Специализация', max_length=255)

    class Meta:
        ordering = ('specialization',)
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        return f'{self.specialization} - {self.name}'


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='Доктор', on_delete=models.CASCADE)
    appointment_date = models.DateField('Дата приема')
    appointment_time = models.TimeField('Время приема')
    patient_name = models.CharField('Имя пациента', max_length=255)
    patient_email = models.EmailField('Почта пациента')
    created_date = models.DateTimeField('Время обращения', auto_now_add=True)

    class Meta:
        ordering = ('created_date',)
        verbose_name = 'Обращение'
        verbose_name_plural = 'Список обращений'

    def __str__(self):
        return f'{self.patient_name} - {self.appointment_date} at {self.appointment_time}'






