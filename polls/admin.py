from django.contrib import admin

# Note model is registered here.
# Question and QuestionAdmin were created for learning purpose.

from .models import Note



#Customize the admin page look
class NoteAdmin(admin.ModelAdmin):
    #custom order the fields
    fieldsets = [
        (None, {'fields': ['note_title','note_text']}),

    ]
    #add search functionality
    search_fields = ('note_title', 'note_text')

#register the customization
admin.site.register(Note, NoteAdmin)




