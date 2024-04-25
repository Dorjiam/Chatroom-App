from django.shortcuts import render

def index(request):
    user_info = {
        "avatar_name": "avatar-1.png",
        "username": "Dorjiam",
        "bio": "Senior Developer",
    }
    return render(request, "components/group_navbar.html", user_info)
