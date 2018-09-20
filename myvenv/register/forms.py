from django import forms

from .models import Competitor

class CompetitorForm(forms.ModelForm):

    class Meta:
        model = Competitor
        fields = ('firstname', 'lastname','birth','club','gender')
