from bootstrap_datepicker.widgets import DatePicker
from django import forms


from .models import Competitor

class CompetitorForm(forms.ModelForm):

    class Meta:
        model = Competitor
        fields = ('firstname', 'lastname','email', 'birth','club','gender')
        date = forms.DateField(
            widget=DatePicker(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True}
            )
        )

