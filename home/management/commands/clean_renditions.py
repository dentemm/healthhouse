import os, shutil
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from wagtail.images.models import Rendition

class Command(BaseCommand):

  def handle(self, *args, **options):
    renditions = Rendition.objects.all()
    self.stdout.write(str(renditions.count())) 


		# if renditions:
		# 	images_root = os.path.join(settings.MEDIA_ROOT, 'images')
		# 	message = ['\n']
		# 	message.append('This will REMOVE ALL IMAGE RENDITION FILES in {}!\n'.format(images_root))
		# 	message.append(
		# 		'Are you sure you want to do this?\n\n'
		# 		"Type 'yes' to continue, or 'no' to cancel: "
		# 	)
		# 	if input(''.join(message)) != 'yes':
		# 		raise CommandError("Remove renditions cancelled.")
		# 	else:
		# 		# doe het
		# 		renditions.delete()
		# 		shutil.rmtree(images_root)
		# 		self.stdout.write('Done')	
		# else:
		# 	self.stdout.write('There are no image renditions')