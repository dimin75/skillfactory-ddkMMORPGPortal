from django.apps import AppConfig


class MmorpgbbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mmorpgbb'

    def ready(self):
        import mmorpgbb.signals
