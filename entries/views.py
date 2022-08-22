from django.views.generic import(
    ListView,
    DetailView,
)
from .models import Entry


class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-date')


class EntryDetailView(DetailView):
    model = Entry
