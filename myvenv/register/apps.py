from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class RegisterConfig(AppConfig):
    name = 'register'

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
