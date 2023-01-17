from django import  forms
from django.forms import  ModelForm
from.models import Registration,StaffTb
from django.forms import ModelChoiceField
from. import views




sta=[
    ('Select you status','select your status'),
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Processing','Processing'),
    ('New','New'),
]





class RegistrationForm(forms.Form):
    # Date=forms.DateField(widget=forms.NumberInput(attrs={'type':'date','class':'form-control','placeholder':'12/11/2021'}))
    CustomerName=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    AnyDeskId=forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    ApplicationDetails=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    Requirements= forms.CharField(max_length=400, widget=forms.Textarea( attrs={'rows':'2', 'cols': '65'}))
    Status=forms.CharField(widget=forms.Select(choices=sta,attrs={'class':'form-control'}))
    CompletionDate=forms.DateField(widget=forms.NumberInput(attrs={'type':'date','class':'form-control'}))
    Staff=forms.ModelChoiceField(queryset=StaffTb.objects.all(),required=True, empty_label='Select the Staff',widget=forms.Select(attrs={
      'class': 'form-control select-access-open select2-hidden-accessible'
      }))


class ProfileForm(forms.ModelForm):

    Date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': '12/11/2021'}))
    CustomerName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    AnyDeskId = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ApplicationDetails = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Requirements = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'rows': '2', 'cols': '125'}))
    Status = forms.CharField(widget=forms.Select(choices=sta, attrs={'class': 'form-control'}))
    CompletionDate = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'}))
    Staff=ModelChoiceField(queryset=StaffTb.objects.all(), initial='Munchen', required=True, empty_label='Select the Staff',
                                   widget=forms.Select(attrs={
                                       'class': 'form-control select-access-open select2-hidden-accessible'
                                   }))

    class Meta:
        model = Registration
        fields =('Date','CustomerName','AnyDeskId','ApplicationDetails','Requirements','Status','CompletionDate','Staff')


class StaffForm(forms.Form):
    Name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    DateOfBirth = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'}))
    Address = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'rows': '2', 'cols': '65'}))

