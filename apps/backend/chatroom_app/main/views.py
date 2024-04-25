from django.shortcuts import render

def index(request):
    user_info = {
        "avatar_name": "avatar-1.png",
        "username": "Dorjiam",
        "bio": "Senior Developer",
        "num": [1, 2, 3, 4],
    }
    return render(request, "components/group_navbar.html", user_info)
