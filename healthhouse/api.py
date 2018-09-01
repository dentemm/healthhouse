from wagtail.images import get_image_model
from wagtail.images.api.v2.serializers import ImageSerializer
from wagtail.images.api.v2.endpoints import ImagesAPIEndpoint
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.serializers import BaseSerializer
from wagtail.api.v2.endpoints import BaseAPIEndpoint
from wagtail.api.v2.filters import FieldsFilter, OrderingFilter, SearchFilter
from wagtail.api.v2.utils import get_full_url

from rest_framework.fields import Field

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

class ImageDownloadURLField(Field):
    
    def get_attribute(self, instance):
        return instance

    def to_representation(self, image):
        return get_full_url(self.context['request'], image.url)

class CustomImageSerializer(ImageSerializer):
    download_url = ImageDownloadURLField(read_only=True)

class CustomImagesAPIEndpoint(BaseAPIEndpoint):
    base_serializer_class = CustomImageSerializer
    filter_backends = [FieldsFilter, OrderingFilter, SearchFilter]
    body_fields = BaseAPIEndpoint.body_fields + ['title', 'detail_url']
    meta_fields = BaseAPIEndpoint.meta_fields + ['tags']
    meta_fields.remove('type')
    meta_fields.remove('detail_url')
    listing_default_fields = BaseAPIEndpoint.listing_default_fields + ['title', 'tags']
    nested_default_fields = BaseAPIEndpoint.nested_default_fields + ['title']
    name = 'images'
    model = get_image_model()

api_router.register_endpoint('images', CustomImagesAPIEndpoint)
api_router.register_endpoint('test', ImagesAPIEndpoint)

