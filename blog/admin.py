from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields =  ('created', 'updated')
    #Para que solo se muestren los campos que se necesitan
    list_display = ('title', 'author', 'published', 'lista_categorias')
    #Para dar la prioridad de que columnas debe ordenar
    ordering = ('author', 'published')
    #Para buscar por titulo, autor, categoria
    search_fields = ('title', 'author__username', 'categories__name')
    #Para poder navegar con las fechas
    date_hierarchy = 'published'
    #Para filtrar por un campo
    list_filter = ('author__username', 'categories__name')

    #Para que se muestre el campo de categorias, ya que con categories__name no funciona en list_display
    def lista_categorias(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    lista_categorias.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
