from django.urls import path
from management.views import (
    UserView,
    OpenPack,
    RegisterView)


urlpatterns = [
    path("user/<int:pk>/", UserView.as_view({"get": "retrieve"})),
    path("user/register/", RegisterView.as_view({"post": "create"})),
    path("user/open/", OpenPack.as_view({"put": "update"})),

]