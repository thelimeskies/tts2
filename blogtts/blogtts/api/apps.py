from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogtts.api'

    def ready(self):
        import blogtts.api.signals  # noqa F401