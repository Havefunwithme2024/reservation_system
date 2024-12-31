from django import forms
from .models import ContactUs, Reservation

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'jackson'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jack@gmail.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'rows': 4
            })
        }
        labels = {
            'name': 'name',
            'email': 'Email Address',
            'message': 'How can we help?'
        }

class ReservationForm(forms.ModelForm):
    comments = forms.Field(required=False, widget = forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Comment(Optional)',
        'rows': '3'
    }))
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'full name'
            }),
            'phone': forms.TextInput(attrs=
                                     {
                                         'type': 'tel',
                                         'class': 'form-control',
                                         'placeholder': 'Phone 085 456 7890'
                                     }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'value': '18:30'


            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Date'
            }),
            'quantity_people': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of people'
            })
        }

