from django.apps import AppConfig


class OphixDbEnginePostgresConfig(AppConfig):
    name = "ophix_dbengine_postgres"
    verbose_name = "Ophix PostgreSQL Driver"
    default_auto_field = "django.db.models.BigAutoField"
