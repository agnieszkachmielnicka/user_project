from django.urls import path
from accounts.views import UserCreateView, UserListView, UserDetailedView, UserUpdateView, UserDeleteView, generate_csv

app_name = 'accounts'

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name="create_user"),
    path('user_list/', UserListView.as_view(), name="user_list"),
    path('users/<pk>/', UserDetailedView.as_view(), name="user_detail"),
    path('update/<pk>/', UserUpdateView.as_view(), name="user_update"),
    path('delete/<pk>/', UserDeleteView.as_view(), name="user_delete"),
    path('user_list/generate_csv/', generate_csv, name="generate_csv")
]
