from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'blog'
class TasksConfig(AppConfig):
    name = 'tasks'
