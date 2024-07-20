from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, MyLoginView
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    #pk primary-key
    path('', PostList.as_view(), name='posts'),
    path('login/',MyLoginView.as_view(),name='login'),
    #i didnt override this view in views.py
    path('logout/',LogoutView.as_view(),name='logout'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('create/', PostCreate.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
]
