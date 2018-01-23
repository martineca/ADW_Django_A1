from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Note


class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    context_object_name = 'latest_notes'

    def get_queryset(self):
        """Return the last five published notes."""
        return Note.objects.order_by('note_text')







