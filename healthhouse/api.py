from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.endpoints import ImagesAPIEndpoint

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('images/test', ImagesAPIEndpoint)


# from wagtail.api.v2.endpoints import BaseAPIEndpoint
# from wagtail.api.v2.serializers import ImageSerializer




# from wagtail.api.v2.filters import FieldsFilter, OrderingFilter, SearchFilter

# from ... import get_image_model
# from .serializers import ImageSerializer


# class ImagesAPIEndpoint(BaseAPIEndpoint):
#     base_serializer_class = ImageSerializer
#     filter_backends = [FieldsFilter, OrderingFilter, SearchFilter]
#     body_fields = BaseAPIEndpoint.body_fields + ['title', 'width', 'height']
#     meta_fields = BaseAPIEndpoint.meta_fields + ['tags']
#     listing_default_fields = BaseAPIEndpoint.listing_default_fields + ['title', 'tags']
#     nested_default_fields = BaseAPIEndpoint.nested_default_fields + ['title']
#     name = 'images'
#     model = get_image_model()

