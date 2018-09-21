import django_tables2 as tables
from .models import Competitor


class CompetitorTable(tables.Table):
    class Meta:
        model = Competitor
        template_name = '/register/django_tables2/bootstrap.html'
