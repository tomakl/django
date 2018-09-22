from django import forms



from .models import Competitor

class CompetitorForm(forms.ModelForm):

    class Meta:
        model = Competitor
        fields = ('firstname', 'lastname','email', 'birth', 'city','club','gender')
        widgets = {
            'birth': forms.DateInput(attrs={'type': 'date'})
        }

