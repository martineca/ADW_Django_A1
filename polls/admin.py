from django.contrib import admin

# Register your models here.

from .models import Choice, Question, Note

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']


class NoteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['note_title','note_text']}),

    ]
    search_fields = ('note_title', 'note_text')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Note, NoteAdmin)




