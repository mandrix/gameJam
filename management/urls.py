from django.urls import path
from management.views import (
   UserView,
   OpenPack
)


urlpatterns = [
    path("user/<int:pk>/", UserView.as_view({"get": "retrieve"})),
    path("user/open/", OpenPack.as_view({"put": "update"})),

]