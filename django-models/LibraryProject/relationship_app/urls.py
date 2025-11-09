#from django.urls import path
#from .views import list_books
#from . import views

#urlpatterns = [
#    path('logout/', views.logout_view, name='logout'),
#    path('register/', views.register_view, name='register'),
#]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Class-based authentication views
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),

    # Registration (still function-based)
    path('register/', views.register_view, name='register'),
]
