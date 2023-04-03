from django.urls import path
from . views import (
    DokuCreateView,
    DokuUpdateView,
    DokuListView,
    DokuDetailView,
    DokuDeleteView,
    DokuKlientCreateView,
    DokuKlientListView,
    DokuKlientDetailView,
    DokuKlientUpdateView,
    DokuKlientDeleteView,
    SearchResultsKlientView,
    SearchResultsEintragView,
    StartView,
    )

urlpatterns = [
    path("new/", DokuCreateView.as_view(), name="new"),
    path("newclient/", DokuKlientCreateView.as_view(), name="newclient"),
    path("edit/<int:pk>", DokuUpdateView.as_view(), name="edit"),
    path("editclient/<int:pk>", DokuKlientUpdateView.as_view(), name="editclient"),
    path("detail/<int:pk>", DokuDetailView.as_view(), name="detail"),
    path("detailclient/<int:pk>", DokuKlientDetailView.as_view(), name="detailclient"),
    path("delete/<int:pk>", DokuDeleteView.as_view(), name="delete"),
    path("deleteclient/<int:pk>", DokuKlientDeleteView.as_view(), name="deleteclient"),
    path("clients/", DokuKlientListView.as_view(), name="listclients"),
    path("entries", DokuListView.as_view(), name="list"),
    path("search/", SearchResultsKlientView.as_view(), name="search_results"),
    path("search_entries/", SearchResultsEintragView.as_view(), name="search_result_eintrag"),
    path("", StartView.as_view(), name="start"),
]
