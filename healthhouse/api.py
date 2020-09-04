from datetime import date, datetime
from dateutil.relativedelta import relativedelta

from django.utils.timezone import make_aware

from wagtail.images import get_image_model
from wagtail.images.api.v2.serializers import ImageSerializer
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.serializers import BaseSerializer
from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api.v2.filters import FieldsFilter, OrderingFilter, SearchFilter
from wagtail.api.v2.utils import get_full_url

from rest_framework.fields import Field

from home.models.snippets import CalendarItem

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

class ImageDownloadURLField(Field):
    
    def get_attribute(self, instance):
        return instance

    def to_representation(self, image):
        return image.file.url

class CustomImageSerializer(ImageSerializer):
    download_url = ImageDownloadURLField(read_only=True)

class CustomImagesAPIEndpoint(BaseAPIViewSet):
    base_serializer_class = CustomImageSerializer
    filter_backends = [FieldsFilter, OrderingFilter, SearchFilter]
    body_fields = BaseAPIViewSet.body_fields + ['title', 'download_url']
    meta_fields = BaseAPIViewSet.meta_fields + ['tags']
    meta_fields.remove('type')
    meta_fields.remove('detail_url')
    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['title', 'tags', 'download_url']
    nested_default_fields = BaseAPIViewSet.nested_default_fields + ['title']
    name = 'images'
    model = get_image_model()

class CalendarItemAPIEndpoint(BaseAPIViewSet):

  model = CalendarItem
  listing_default_fields = BaseAPIViewSet.listing_default_fields + ['title', 'description', 'date']
  # body_fields = BaseAPIEndpoint.body_fields + ['title']
  meta_fields = BaseAPIViewSet.meta_fields + ['title']

  known_query_parameters = BaseAPIViewSet.known_query_parameters.union([
    'current_month',
  ])
  
  def get_queryset(self):

    current_month = self.request.query_params.get('current_month', None)

    if (current_month):
      try: 
        reference = datetime.strptime(current_month, '%Y-%m-%d')

      except:
        reference = datetime.now()

    else: 
      reference = datetime.now()

    reference = make_aware(reference)

    start = reference - relativedelta(months=3)
    end = reference + relativedelta(months=3)

    return  self.model.objects.filter(date__gte=start, date__lte=end)

api_router.register_endpoint('images', CustomImagesAPIEndpoint)
api_router.register_endpoint('events', CalendarItemAPIEndpoint)

