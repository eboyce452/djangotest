from django.conf.urls import url
from app_one import views

app_name = 'app_one'

urlpatterns = [
	url(r'^register/$', views.register, name ='register'),
	url(r'^user_login/$',views.user_login, name = 'user_login')
]