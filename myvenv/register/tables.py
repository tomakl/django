import django_tables2 as tables
from .models import Competitor


class CompetitorTable(tables.Table):
    start_number = tables.Column()
    lastname = tables.Column()
    firstname = tables.Column()
    club = tables.Column()
    payment = tables.Column()
    class Meta:
        template_name = 'django_tables2/bootstrap4.html'
