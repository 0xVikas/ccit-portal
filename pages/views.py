from django.shortcuts import render
from users.permissions import user_is_logged_in_and_active


@user_is_logged_in_and_active
def home(request):
    return render(
        request, "registration/home.html", context={"title": "CCIT Complaint Portal"}
    )


def contact(request):
    return render(
        request, "registration/contact.html", context={"title": "CCIT Contact Us"}
    )


def denied(request):
    return render(request, "registration/denied.html")
