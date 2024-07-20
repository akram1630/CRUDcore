from django.apps import AppConfig


#must be declared on proj/setting.installedapps
class PostConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'post'
