from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from questions.models import Question

