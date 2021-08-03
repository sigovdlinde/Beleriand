from django.urls import path
from .views import home_view, first_view, second_view, third_view, fourth_view, post_form_api

urlpatterns = [
    path('', home_view, name='home'),
    path('first/', first_view, name='first'),
    path('second/', second_view, name='second'),
    path('third/', third_view, name='third'),
    path('fourth/', third_view, name='fourth'),
    path('api/post_form/', post_form_api, name="post_form_api"),
]
