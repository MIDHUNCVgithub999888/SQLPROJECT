from django import  forms
from.models import Registration,StaffTb
from django.forms import ModelChoiceField
from. import views


sta=[
    ('Select you status','select your status'),
    ('Completed','completed'),
    ('Pending','pending'),
    ('Processing','Processing'),
]



class RegistrationForm(forms.Form):
    Date=forms.DateField(widget=forms.NumberInput(attrs={'type':'date','class':'form-control'}))
    CustomerName=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    AnyDeskId=forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    ApplicationDetails=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    Requirements= forms.CharField(max_length=400, widget=forms.Textarea( attrs={'rows':'2', 'cols': '65'}))
    Status=forms.CharField(widget=forms.Select(choices=sta,attrs={'class':'form-control'}))
    CompletionDate=forms.DateField(widget=forms.NumberInput(attrs={'type':'date','class':'form-control'}))
    Staff=forms.CharField(queryset=StaffTb.objects.all())

class ProfileForm(forms.ModelForm):
  class Meta():
    model=Registration
    fields="__all__"

class StaffForm(forms.Form):
    Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    DateOfBirth = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'}))
    Address = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'rows': '2', 'cols': '65'}))

