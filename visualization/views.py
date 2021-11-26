import io, csv, pandas as pd

from typing import Any

from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from visualization.forms import DataForm

# Read the data uploaded via csv or excel
class IndexView(View):
    def get_context_data(self):
        context: dict[str, Any] = {}
        return context

    def get(self, request: HttpRequest) -> HttpResponse:
        """Add new action view."""
        context = self.get_context_data()
        return render(request, 'base.html', context)


class DataVisualizationView(View):
    def get_context_data(self):
        context: dict[str, Any] = {}
        context['DataForm'] = DataForm()
        context['action_url'] = reverse('visualization:visuals')
        return context

    def get(self, request: HttpRequest) -> HttpResponse:
        """Add new action view."""
        context = self.get_context_data()
        return render(request, 'visualization/data.html', context)

    def post(self, request: HttpRequest) -> HttpResponse:

        form = DataForm(request.POST, request.FILES)
        columns: list[str] = []
        context = self.get_context_data()
        if form.is_valid():
            files = request.FILES['file']
            reader = pd.read_csv(files)
            for col in reader.columns:
                columns.append(col)
        print(len(columns), '<<<<<<printing columns>>>>')
        context['columns'] = columns
        # return HttpResponseRedirect(reverse('visualization:visual-home'))
        return render(request, 'visualization/data.html', context)
