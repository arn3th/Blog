from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    """Zawiera ustawienia panelu administratora dotyczącego postów."""
    list_display = ('title','slug','author','publish','status') #dodaje kolumny danych
    list_filter = ('status','created','publish','author') #dodaje możliwość filtrowania z prawej strony
    search_fields = ('title','body') #dodaje możliwość wyszukiwania w tytułach i body
    prepopulated_fields = {'slug': ('title',)} #autouzupełnienie slug podczas dodawania postu
    raw_id_fields = ('author',) #dodanie autora po id podczas dodawania postu
    date_hierarchy = 'publish' #Filtrowanie po datach u góry strony
    ordering = ['status', 'publish'] #kolejność
admin.site.register(Post,PostAdmin)
