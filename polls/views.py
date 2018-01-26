from django.views import generic
from .models import Note
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy


#Signup view for new users
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('note_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    context_object_name = 'latest_notes'

    def get_queryset(self):
        """Return the last five published notes."""
        return Note.objects.order_by('note_text')


class NoteCreate(CreateView):
  model = Note
  success_url = reverse_lazy('note_list')
  fields = ['note_title', 'note_text']

class NoteUpdate(UpdateView):
    model = Note
    success_url = reverse_lazy('note_list')
    fields = ['note_title', 'note_text']

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')













