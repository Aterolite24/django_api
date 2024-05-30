from api.models import Note
from tastypie.resources import ModelResource

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'