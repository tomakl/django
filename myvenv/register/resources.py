from import_export import resources
from .models import Competitor

class CompetitorResource(resources.ModelResource):
    class Meta:
        model = Competitor