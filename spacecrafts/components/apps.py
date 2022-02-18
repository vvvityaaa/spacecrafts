from django.apps import AppConfig


class ComponentsConfig(AppConfig):
    name = 'spacecrafts.components'

    def ready(self):
        from spacecrafts.components.checks import example_check_main_engine
        from django.core.checks import register
        register(example_check_main_engine)
