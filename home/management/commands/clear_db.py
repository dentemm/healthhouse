import os

from django.core.management.base import BaseCommand, CommandError

from home.models.pages import (
  HealthHouseSettings,
  LinkFields,               # abstract
  RelatedLink,              #abstract
  HealthHouseRelatedLink,
  Address,
  Location,
  Partner,
  HomePage,
  HomePageCoverImage,
  ContactPage,
  DiscoveryPage,
  AboutPage,
  BlogIndexPage,
  BlogPage,
  BlogPageGallery,
  PartnerPage,
  AboutPageQuestion
) 

class Command(BaseCommand):

    help = 'Clears database'

    def handle(self, *args, **options):

        HealthHouseSettings.objects.all().delete()
        HealthHouseRelatedLink.objects.all().delete()
        Address.objects.all().delete()
        Location.objects.all().delete()
        Partner.objects.all().delete()
        HomePageCoverImage.objects.all().delete()
        ContactPage.objects.all().delete()
        DiscoveryPage.objects.all().delete()
        AboutPage.objects.all().delete()
        BlogIndexPage.objects.all().delete()
        BlogPage.objects.all().delete()
        BlogPageGallery.objects.all().delete()
        PartnerPage.objects.all().delete()
        AboutPageQuestion.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(os.environ))
