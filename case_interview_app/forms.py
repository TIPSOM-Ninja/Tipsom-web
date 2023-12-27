# case_interview_app/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import VictimProfile, Interviewer, SuspectedTrafficker

class DateInput(forms.DateInput):
    input_type = 'date'

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.ChoiceField):
                field.widget.attrs.update({'class': 'form-select'})
            elif isinstance(field, forms.DateField):
                field.widget = DateInput()

class VictimSearchForm(BaseForm):
    class Meta:
        model = VictimProfile
        fields = ['victim_identifier','citizenship','gender','interview_country','interview_date','identification_number']
        labels = {
            'victim_identifier': _('Victim Identifier'),
            'citizenship': _('Citizenship'),
            'interview_date': _('Interview Date'),
            # Add labels for other fields as needed
        }

class InterviewerSearchForm(BaseForm):
    class Meta:
        model = Interviewer
        fields = ['country','data_entry_purpose','first_name','last_name','organization','email_address']
        labels = {
            'country': _('Country'),
            'data_entry_purpose': _('Data Entry Purpose'),
            
            # Add labels for other fields as needed
        }

class TraffickerSearchForm(BaseForm):
    class Meta:
        model = SuspectedTrafficker
        fields = ['victim','first_name','last_name','dob','gender','race','citizenship','id_number','date_of_arrest','traffick_from_country','traffick_to_country']
        labels = {
            'victim': _('Victim'),
            'first_name': _('First Name'),
            'date_of_arrest': _('Date of Arrest'),
            # Add labels for other fields as needed
        }