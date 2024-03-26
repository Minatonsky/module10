from django.contrib import admin
from .models import Tag, Note, Author

# Register your models here.
admin.site.register(Tag)
admin.site.register(Note)
admin.site.register(Author)
