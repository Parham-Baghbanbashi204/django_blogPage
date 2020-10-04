from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # ready method --> put signals here
    def ready(self):
        import users.signals
