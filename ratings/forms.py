from django import forms
from ratings.models import Rating
from django.forms.widgets import TextInput, NumberInput


class RatingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(RatingForm, self).__init__(*args, **kwargs)

        self.fields['beer_name'].widget = TextInput(attrs={'placeholder': 'Cider Name', 'required': 'true'})
        self.fields['brewer_name'].widget = TextInput(attrs={'placeholder': 'Brewer Name'})
        self.fields['notes'].widget = TextInput(attrs={'placeholder': 'Notes'})
        self.fields['score'].widget = NumberInput(attrs={'min': 1, 'max': 10, 'required': 'true'})

    class Meta:

        model = Rating
        fields = ['beer_name', 'brewer_name', 'notes', 'score',]
