from api.models import note
from tastypie.resources import ModelResource

class noteResource(ModelResource):
    class meta:
        queryset = note.objects.all()
        resource_name = 'note1'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self._meta.queryset)  # Debugging statement