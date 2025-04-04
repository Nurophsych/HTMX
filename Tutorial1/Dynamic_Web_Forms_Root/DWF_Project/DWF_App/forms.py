from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'information']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'information': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your information',
                'rows': 4,
                'data-min-length': '10',
                'oninput': 'this.nextElementSibling.textContent = this.value.length + " characters"'
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long")
        return name

    def clean_information(self):
        information = self.cleaned_data.get('information')
        if len(information) < 10:
            raise forms.ValidationError("Information must be at least 10 characters long")
        return information