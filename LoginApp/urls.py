from django.urls import path
from . import views
app_name = 'login_app'

urlpatterns = [
    path('signup/',view=views.sign_up, name='signup'),
    path('login/',view=views.login_user, name='login'),
    path('logout/',view=views.logout_user, name='logout'),
    path('profile/', view= views.user_profile, name='profile'),
]
