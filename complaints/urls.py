"""Module for setting url paths"""
from django.urls import path
from complaints import views

urlpatterns = [
    path("my-tickets/", views.previous, name="previous-requests"),
    path("request-unblock/", views.request_unblock, name="unblock-request"),
    path("add-tickets/", views.register_complaint, name="complaint-register"),
    path("handle-tickets/", views.display_complaint, name="complaint-display"),
    path("handle-requests/", views.display_request, name="request-display"),
    path("resolve-tickets/", views.handle_complaint, name="complaint-resolve"),
    path(
        "resolve-unblock-requests/",
        views.handle_unblock_request,
        name="update_request_resolve",
    ),
    path("complaints/cancel/", views.cancel_complaint, name="cancel-complaint"),
    path(
        "unblocks/cancel/", views.cancel_unblock_request, name="cancel-unblock-request"
    ),
]
