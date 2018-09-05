from django.urls import path
from .views import post_list,post_detail,index,about,contact,thankYou

app_name='blog'
urlpatterns = [
# post views
path('', post_list, name='index'),
path('index', post_list, name='index'),
path('about', about, name='about'),
path('contact', contact, name='contact'),
path('contact/ThankYou', thankYou, name='thankYou'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/about',about,name='about'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/contact',contact,name='contact'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/index',post_list,name='index'),
]
