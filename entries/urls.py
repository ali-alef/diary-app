from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(login_url="admin:login")(views.EntryListView.as_view()), name='entry-list-view'),
    path('entry/<int:pk>', login_required(login_url="admin:login")(views.EntryDetailView.as_view()), name='entry-detail-view'),
    path('entry/<int:pk>/update', login_required(login_url="admin:login")(views.EntryUpdateView.as_view()), name='entry-update-view'),
    path('create', login_required(login_url="admin:login")(views.EntryCreateView.as_view()), name='entry-create-view'),
    path('entry/<int:pk>/delete', login_required(login_url="admin:login")(views.EntryDeleteView.as_view()), name='entry-delete-view'),
]
