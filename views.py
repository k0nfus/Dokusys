from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from . models import Klient, Eintrag

class DokuListView(ListView):
    model = Eintrag
    template_name = "list.html"

class DokuKlientListView(ListView):
    model = Klient
    template_name = "klientlist.html"

class DokuDetailView(DetailView):
    model = Eintrag
    template_name = "detail.html"

class DokuKlientDetailView(DetailView):
    model = Klient
    template_name = "klientdetail.html"


class DokuCreateView(CreateView):
    model = Eintrag
    template_name = "new.html"
    fields = ["klient", "datum", "doku", "bild"]

class DokuKlientCreateView(CreateView):
    model = Klient
    template_name = "newclient.html"
    fields = ["name", "vorname", "telefonnummer", "projekt"]

class DokuUpdateView(UpdateView):
    model = Eintrag
    template_name = "edit.html"
    fields = ["klient", "datum", "doku", "bild"]

class DokuKlientUpdateView(UpdateView):
    model = Klient
    template_name = "klientedit.html"
    fields = ["name", "vorname", "telefonnummer", "projekt"]

class DokuDeleteView(DeleteView):
    model = Eintrag
    template_name = "delete.html"
    success_url = reverse_lazy("list")

class DokuKlientDeleteView(DeleteView):
    model = Klient
    template_name = "klientdelete.html"
    success_url = reverse_lazy("listclients")

class StartView(TemplateView):
    template_name = "start.html"

class SearchResultsKlientView(ListView):
    model = Klient
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Klient.objects.filter(
            Q(name__icontains=query) | Q(vorname__icontains=query) | Q(telefonnummer__icontains=query) | Q(projekt__icontains=query)
        )
        return object_list

class SearchResultsEintragView(ListView):
    model = Eintrag
    template_name = "search_result_eintrag.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Eintrag.objects.filter(
            Q(datum__icontains=query) | Q(doku__icontains=query) #scheitert weil klient = foreign_key
        ) or Klient.objects.filter(
            Q(name__icontains=query) | Q(vorname__icontains=query) | Q(telefonnummer__icontains=query) | Q(projekt__icontains=query)
        )
        return object_list