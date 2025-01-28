from django.apps import AppConfig


class WalletConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_app.wallet'
    
    def ready(self):
        from core_app import signals
