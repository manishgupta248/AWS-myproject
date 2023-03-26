from django import forms
from .models import Notice
from django.contrib.admin.widgets import AdminDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['subject', 'notice_date', 'notice_copy',]
        widgets = {
            'notice_date':DateInput()
        }