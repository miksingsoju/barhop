from django import forms
from .models import Bar, BarImage, Amenity, Event
from django.core.exceptions import ValidationError


class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultiImageField(forms.ImageField):
    widget = MultiFileInput

    def clean(self, data, initial=None):
        if data in self.empty_values:
            if self.required and not initial:
                raise ValidationError(self.error_messages["required"], code="required")
            return []

        if not isinstance(data, (list, tuple)):
            data = [data]
        cleaned_files = []
        for f in data:
            cleaned_files.append(super().clean(f, initial))
        return cleaned_files


class CreateBarForm(forms.ModelForm):
    class Meta: 
        model = Bar
        fields = ['bar_name', 'bar_description', 'bar_start_time', 'bar_end_time', 'bar_address', 'bar_amenities']
        widgets = {
            'bar_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bar_description':forms.TextInput(attrs={'class': 'form-control'}),
            'bar_start_time': forms.TimeInput(format='%H:%M',attrs={'type': 'time', 'class': 'form-control'}),
            'bar_end_time': forms.TimeInput(format='%H:%M',attrs={'type': 'time', 'class': 'form-control'}),
            'bar_address':forms.TextInput(attrs={'class': 'form-control'}),
            'bar_amenities': forms.SelectMultiple(),
        }

    images = MultiImageField(required=False)

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'start_time', 'end_time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
        }
        
UpdateBarImageFormSet = forms.modelformset_factory(
    BarImage,
    fields=('image',),
    extra=0,
    can_delete=True
)
