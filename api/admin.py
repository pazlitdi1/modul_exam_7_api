from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Advisers, Services, Features, Offers, Blog, Clients, Comments, Admin


@admin.register(Advisers)
class AdvisersAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'first_name', 'last_name', 'education', 'seen')
    list_display_links = ('id', 'slug', 'first_name', 'last_name', 'education', 'seen')
    search_fields = ('id', 'first_name', 'lastname')
    ordering = ('id',)
    prepopulated_fields = {"slug": ("first_name",)}


@admin.register(Services)
class ServicesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'title', 'description', 'image', 'seen')
    list_display_links = ('id', 'slug', 'title', 'description', 'image', 'seen')
    search_fields = ('id', 'title', 'description')
    ordering = ('id',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Features)
class FeaturesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'title', 'description', 'logo', 'seen')
    list_display_links = ('id', 'slug', 'title', 'description', 'logo', 'seen')
    search_fields = ('id', 'title', 'description')
    ordering = ('id',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Offers)
class OffersAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'title', 'description', 'image', 'seen')
    list_display_links = ('id', 'slug', 'title', 'description', 'image', 'seen')
    search_fields = ('id', 'title', 'description')
    ordering = ('id',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'title', 'description', 'image', 'seen', 'admin')
    list_display_links = ('id', 'slug', 'title', 'description', 'image', 'seen')
    search_fields = ('id', 'title', 'description')
    ordering = ('id',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Clients)
class ClientsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'first_name', 'last_name', 'nickname', 'seen')
    list_display_links = ('id', 'slug', 'first_name', 'last_name', 'nickname', 'seen')
    search_fields = ('id', 'first_name', 'last_name')
    ordering = ('id',)
    prepopulated_fields = {"slug": ("first_name",)}


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'service', 'comment', 'client')
    list_display_links = ('id', 'service', 'comment', 'client')
    search_fields = ('id', 'client', 'service', 'comment')
    ordering = ('id',)
    prepopulated_fields = {"slug": ("client",)}


@admin.register(Admin)
class AdminAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'first_name', 'last_name', 'username', 'image', 'password', 'seen')
    list_display_links = ('id', 'slug', 'first_name', 'last_name', 'username', 'image', 'seen')
    search_fields = ('id', 'first_name', 'last_name', 'username')
    ordering = ('id',)
    prepopulated_fields = {"slug": ("first_name",)}
