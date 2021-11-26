import io, csv, pandas as pd

from typing import Any

from django.conf import settings
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

from utils.file_utils import FileManager
from visualization.forms import DataForm

# instantiate classes
file_manager = FileManager()
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
            user_file = request.FILES['file']
            # check file type
            file_type = file_manager.check_file_type(user_file)
            if file_type in settings.DATA_FORMAT_FOR_INTERPRETATION:
                read_file = file_manager.read_file_by_file_extension(user_file)
                if read_file is not None:
                    i = 0
                    for col in read_file.columns:
                        columns.append({col, i})
                        i += 1
                else:
                    print('from view, file not supported')

        else:
            print(form.errors.values())
        context['columns'] = columns
        return render(request, 'visualization/data.html', context)
