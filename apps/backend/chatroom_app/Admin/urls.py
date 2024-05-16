from django.urls import path
from .views import chat
urlpatterns = [
    path("chats/<str:senderd>/<str:reciverd>/", chat, name="chat")
]