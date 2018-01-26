from django.db import models
from django.urls import reverse


# Note model that we use in the app

class Note(models.Model):
    note_text = models.CharField(max_length=4000)
    note_title = models.CharField(max_length=200)
    def __str__(self):
        return self.note_text

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('note_edit', kwargs={'pk': self.pk})

