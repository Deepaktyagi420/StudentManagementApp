from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),  # Login page
    path('logout/', views.user_logout, name='logout'),  # Logout action    
    path('', views.index, name='index'),  # Home page
    path('<int:id>/', views.view_student, name='view_student'),  # View a specific student
    path('add/', views.add, name='add'),  # Add a new student
    path('edit/<int:id>/', views.edit, name='edit'),  # Edit a student
    path('delete/<int:id>/', views.delete, name='delete'),  # Delete a student

]