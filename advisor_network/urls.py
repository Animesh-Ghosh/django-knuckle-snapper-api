from django.urls import path
from . import views

urlpatterns = [
    path("advisor/", views.list_advisors, name="list-advisors"),
    path("advisor/<int:advisor_id>/", views.book_call, name="book-call"),
    path("advisor/booking/", views.list_booked_calls, name="list-booked-calls"),
]
