from django.core.exceptions import ValidationError
from datetime import date
from core import models
from django import forms


class Appeal(forms.ModelForm):
    class Meta:
        model = models.Appeal
        fields = '__all__'
        widgets = {
            'appeal_time': forms.Select(
                choices=[(f'{h:02}:{m:02}', f'{h:02}:{m:02}') for h in range(9, 18) for m in range(0, 60, 15)]),
            'appeal_date': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            )
        }
