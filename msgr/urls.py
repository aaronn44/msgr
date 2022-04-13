
from django.urls import path

from . import views


app_name = "msgr"

urlpatterns = [
    path("",
         views.ChatsListView.as_view(),
         name="main"),
    path("users/<int:pk>/",
         views.ProfilePageView.as_view(),
         name="profile_page"),
    path("users/<int:pk>/chat/",
         views.StartChatView.as_view(),
         name="start_chat"),
    path("chats/<int:pk>/",
         views.ChatView.as_view(),
         name="chat"),
]
