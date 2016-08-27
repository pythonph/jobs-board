from django import forms

from .models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        exclude = ['creator', 'created', 'updated', 'expiry_date']
