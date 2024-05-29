from api.models import note
from tastypie.resources import ModelResource

class noteResource(ModelResource):
    class meta:
        queryset = note.objects.all()
        resource_name = 'note1'