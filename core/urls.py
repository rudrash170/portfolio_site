from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('single/', views.single_page, name='single_page'),
    path('about/', views.about, name='about'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('skills/', views.skills, name='skills'),
    path('achievements/', views.achievements, name='achievements'),
    path('contact/', views.contact, name='contact'),
] 