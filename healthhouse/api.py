from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.endpoints import ImagesAPIEndpoint

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
####### api_router.register_endpoint('images', ImagesAPIEndpoint)


# from wagtail.api.v2.endpoints import BaseAPIEndpoint
# from wagtail.api.v2.serializers import ImageSerializer




# from wagtail.api.v2.filters import FieldsFilter, OrderingFilter, SearchFilter

# from ... import get_image_model
# 
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

from wagtail.images import get_image_model
from wagtail.api.v2.serializers import RelatedField, DetailUrlField, TypeField, TagsField
from wagtail.api.v2.endpoints import BaseAPIEndpoint
from wagtail.api.v2.filters import FieldsFilter, OrderingFilter, SearchFilter

from collections import OrderedDict
from rest_framework import serializers
from taggit.managers import _TaggableManager

class CustomBaseSerializer(serializers.ModelSerializer):
    # Add StreamField to serializer_field_mapping
    serializer_field_mapping = serializers.ModelSerializer.serializer_field_mapping.copy()

    serializer_related_field = RelatedField

    # Meta fields
    type = TypeField(read_only=True)
    detail_url = DetailUrlField(read_only=True)

    def to_representation(self, instance):
        data = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        # Split meta fields from core fields
        meta_fields = [field for field in fields if field.field_name in self.meta_fields]
        fields = [field for field in fields if field.field_name not in self.meta_fields]

        # Make sure id is always first. This will be filled in later
        if 'id' in [field.field_name for field in fields]:
            data['id'] = None

        # Serialise meta fields
        meta = OrderedDict()
        for field in meta_fields:

            print('----')
            print(field)

            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is None:
                # We skip `to_representation` for `None` values so that
                # fields do not have to explicitly deal with that case.
                meta[field.field_name] = None
            else:
                meta[field.field_name] = field.to_representation(attribute)

        if meta:
            data['meta'] = meta

        # Serialise core fields
        for field in fields:

            print

            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is None:
                # We skip `to_representation` for `None` values so that
                # fields do not have to explicitly deal with that case.
                data[field.field_name] = None
            else:
                data[field.field_name] = field.to_representation(attribute)

        return data

    def build_property_field(self, field_name, model_class):
        # TaggableManager is not a Django field so it gets treated as a property
        field = getattr(model_class, field_name)
        if isinstance(field, _TaggableManager):
            return TagsField, {}

        return super().build_property_field(field_name, model_class)

    def build_relational_field(self, field_name, relation_info):
        field_class, field_kwargs = super().build_relational_field(field_name, relation_info)
        field_kwargs['serializer_class'] = self.child_serializer_classes[field_name]
        return field_class, field_kwargs

class CustomImagesAPIEndpoint(BaseAPIEndpoint):
    base_serializer_class = CustomBaseSerializer
    filter_backends = [FieldsFilter, OrderingFilter, SearchFilter]
    body_fields = BaseAPIEndpoint.body_fields + ['title', 'width', 'height']
    meta_fields = BaseAPIEndpoint.meta_fields + ['tags']
    listing_default_fields = BaseAPIEndpoint.listing_default_fields + ['title', 'tags']
    nested_default_fields = BaseAPIEndpoint.nested_default_fields + ['title']
    name = 'images'
    model = get_image_model()

api_router.register_endpoint('images', CustomImagesAPIEndpoint)
