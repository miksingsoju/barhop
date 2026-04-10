from django import forms
from .models import Seating, Table


class SeatingForm(forms.ModelForm):
    # quantity lives HERE at class level, NOT inside Meta.fields
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1,
        })
    )

    class Meta:
        model = Seating
        fields = ['seating', 'capacity', 'image']  # no 'quantity' here
        widgets = {
            'seating': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }