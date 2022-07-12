from django.apps import AppConfig


class FakeNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fake_name'
