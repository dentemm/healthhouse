from django.core import serializers
from django.http import JsonResponse
from django.views.generic import ListView

from wagtail.images.models import Image

from braces.views import JSONResponseMixin

class ExpoGallery(ListView):
    
    model = Image

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):

        return Image.objects.filter(tags__name='test')

    def get(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        data = serializers.serialize('json', queryset)

        return JsonResponse(data, status=200, safe=False)
    