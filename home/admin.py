from django.contrib import admin
from .models import Author
from .models import Article

admin.site.register(Author)
admin.site.register(Article)
