from django.urls import path
from api.views import *
from . import views

urlpatterns = [
    # path(
    #     '',
    #     homeapi.as_view(),
    #     name = 'home'
    # )
    path(
        '',
        views.home,
        name = 'home'
    ),
    path(
        'home/',
        views.home,
        name = 'home'
    ),
    path(
        'sign-up/',
        views.sign_up,
        name = 'sign_up'
    ),
    path(
        'create-post/',
        views.create_post,
        name = 'create_post'
    ),
]


