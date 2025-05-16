from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
  print('### - Pre save - ###')
  print(instance)

@receiver(post_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
  print('### - Post save - ###')
  print(instance)
  
@receiver(pre_delete, sender=Car)
def car_pre_save(sender, instance, **kwargs):
  print('### - Pre delete - ###')
  print(instance)

@receiver(post_delete, sender=Car)
def car_pre_save(sender, instance, **kwargs):
  print('### - Post delete - ###')
  print(instance)