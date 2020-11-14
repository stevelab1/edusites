from django.apps import AppConfig


class MoodboardConfig(AppConfig):
    name = 'moodboard'


    def ready(self):
        # import signal handlers
        import moodboard.signals


