from django.dispatch import receiver
from store.signals import order_created

class X:
  pass

@receiver(order_created)
def on_order_created(sender, **kwargs):
    print('sender:', sender)
    print(kwargs['order'])
  
  