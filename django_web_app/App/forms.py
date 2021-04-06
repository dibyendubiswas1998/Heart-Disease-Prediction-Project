from django import forms
from django.forms import widgets
from .models import Paitent

class PaitentForm(forms.ModelForm):
    class Meta:
        model = Paitent
        fields = ['name', 'sex', 'age', 'chest_pain', 'blood_pressure', 'cholestorol', 'blood_sugar',
                  'electrocardiographic_resulter', 'heart_rate', 'angina', 'st_depression', 
                  'st_segment', 'vessels', 'thallium_test_result']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Your Name'}),
            'age': forms.NumberInput(attrs={'placeholder':'Your Age'}),
            'blood_pressure': forms.NumberInput(attrs={'placeholder':'Your Blood Pressure'}),
            'cholestorol': forms.NumberInput(attrs={'placeholder':'Your Cholestor'}),
            'blood_sugar': forms.NumberInput(attrs={'placeholder':'Your Blood Sugar'}),
            'heart_rate': forms.NumberInput(attrs={'placeholder':'Your Heart Rate'}),
            'st_depression': forms.NumberInput(attrs={'placeholder':'Your St Depression Rate'}),
            'vessels': forms.NumberInput(attrs={'placeholder':'Your Vessels'}),
        }

    def __init__(self, *args, **kwargs):
            super(PaitentForm, self).__init__(*args, **kwargs)
            self.fields['sex'].empty_label = "Select Genger"
            self.fields['chest_pain'].empty_label = "Type Of Chest Pain"
            self.fields['electrocardiographic_resulter'].empty_label = "Electrocardiographic Result"
            self.fields['angina'].empty_label = "Have you angina"
            self.fields['st_segment'].empty_label = "St Segment"
            self.fields['thallium_test_result'].empty_label = "Thallium Test Result"
