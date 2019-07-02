from django.urls import path
from . import views
from django.contrib.auth import views as django_views
# from .views import TerminListView, TerminListDelete, TerminListCreate, TerminDetailView

urlpatterns = [
    path('terminy/dodaj', views.termin_create_view, name='terminy'),
    path('terminy/', views.termin_list_view, name='termin'),
    path('terminy/<int:pk>/update/', views.termin_edit, name='termin-update'),
    path('terminy/<int:pk>/delete/', views.termin_delete, name='termin-delete'),
    path('register', views.register_view, name='register'),
    path('profile', views.profile, name='profile'),
    path('login', django_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout', django_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]

