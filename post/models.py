from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=255)
  post_type = models.CharField(max_length=255)
  # CharField for littler text
  #TextField for big text
  # null=True, blank=True mean the TextField can be null & blank
  description = models.TextField(null=True, blank=True)
  image = models.ImageField(upload_to='images',
                            blank=True,
                            default='images/no-image.jpg')
  created_at = models.DateTimeField(auto_now=True)
  #when we delete a user , their posts will be deleted
  # User is a django feature and we can override it
  user = models.ForeignKey(User,
                           on_delete=models.CASCADE,
                           null=True,
                           blank=True) 
  def __str__(self):
    return self.title

  class Meta:  #of class Post
    ordering = ['-created_at']  # order posts by created time
### after finishing our model we have to migrations and migrate
### and migrate after updating