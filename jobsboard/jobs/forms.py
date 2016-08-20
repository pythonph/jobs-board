from django import forms

from .models import Job


class JobForm(forms.ModelForm):

    # class Meta:
    #     model = Job
    #     fields = ('title', 'creator',)

    class Meta:
        model = Job
        exclude = ['created', 'updated', 'expiry']
