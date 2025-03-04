from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models import Customer

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    print("sender from user:", sender)
    if kwargs['created']:
      print("sender for customer")
      Customer.objects.create(user=kwargs['instance'])
      
    