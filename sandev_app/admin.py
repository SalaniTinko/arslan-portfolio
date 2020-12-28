

from django.contrib import admin
from .models import Contact, ProjectDetail,ClientFeedback
admin.site.site_header = "Muhammad Arslan Toor"
admin.site.site_title = "Muhammad Arslan Toor"
admin.site.index_title = "Muhammad Arslan Toor"


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "email", "subject", "message")
    search_fields = ('name', "email", )
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ("name",)
    list_display_links = ['name']
admin.site.register(Contact,ContactAdmin)

class ProjectDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', "cover_image", "project_category", "project_client", "project_date", "project_url")
    search_fields = ('project_name', "project_client", )
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ("project_name",)
    list_display_links = ['project_name']
admin.site.register(ProjectDetail,ProjectDetailAdmin)


class ClientFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "Country", "feedback", "image")
    search_fields = ('name', "Country",)
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ("Country",)
    list_display_links = ['name', 'id', ]
admin.site.register(ClientFeedback,ClientFeedbackAdmin)

