from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = 'temtudo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class FiltersView(TemplateView):
    template_name = 'temtudo/filters.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'filters'
        return context