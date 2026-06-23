from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('internships/',views.internships,name='internships'),
    path('applications/',views.applications,name='applications'),
    path('logout/',views.logout,name='logout'),
    path('apply/<int:id>/', views.apply_internship, name='apply'),
]