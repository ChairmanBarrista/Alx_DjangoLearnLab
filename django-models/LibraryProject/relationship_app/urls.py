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
        LoginView.as_view(template_name='relationship_app/templates/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/templates/logout.html'),
        name='logout'
    ),

    # Registration (still function-based)
    path('register/', views.register_view, name='register'),

    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
