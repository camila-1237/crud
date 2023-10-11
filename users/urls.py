from django.urls import path
from .views import ListUsersView, CreateUserView, RetrieveUserView, ObtainAuthToken,  CreateTokenView

urlpatterns = [
    path('list/', ListUsersView.as_view()),
    path('create/', CreateUserView.as_view()),
    path('user/', RetrieveUserView()),
    path('token/', CreateTokenView() )
]
