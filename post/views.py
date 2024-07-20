from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post
from django.urls import reverse, reverse_lazy
from .forms import CRUDFORM
#to secure views :
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy("posts")

  def form_invalid(self, form):
    return self.render_to_response(self.get_context_data(form=form))


#####################################################################################
class PostList(LoginRequiredMixin, ListView):
  model = Post
  context_object_name = 'posts'
  template_name = 'post/list.html'  #post/templates/post/list.html


####################################################################################
class PostDetail(LoginRequiredMixin, DetailView):
  model = Post
  context_object_name = 'post'
  template_name = 'post/detail.html'  #post/templates/post/detail.html


######################################################################################
class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  form_class = CRUDFORM
  template_name = 'post/form.html'  #post/templates/post/create.html

  #succes_url = reverse_lazy('posts') #essa didn't work
  def get_success_url(self):
    return reverse_lazy('posts')

  def form_validation(self, form):
    form.instance.user = self.request.user  #only one time
    return super(PostCreate, self).form_valid(form)


#######################################################################################
class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  form_class = CRUDFORM
  template_name = 'post/form.html'  #post/templates/post/create.html

  #succes_url = reverse_lazy('posts')#essa didn't work
  def get_success_url(self):
    return reverse_lazy('posts')

  def form_validation(self, form):
    return super(PostUpdate, self).form_valid(form)


###################################################################################
class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  template_name = 'post/delete.html'  #post/templates/post/create.html

  def get_success_url(self):
    return reverse_lazy('posts')
