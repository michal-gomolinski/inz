from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
#router.register(r'create_rejestry', views.RejestrViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/rejestry',views.getRejestry,name="rejestry"),
    path(r'api/rejestr/<int:pk>',views.getRejestrById,name="rejestrById"),
    path(r'api/create_rejestr',views.postRejestr,name="postRejestr"),
    path(r'', views.index, name='index'),
    path(r'sign-up', views.index, name='index'),
    path(r'sign-in', views.index, name='index'),
    path(r'pets', views.index, name='index'),
    path(r'humans', views.index, name='index'),
    path(r'profile', views.index, name='index'),
]