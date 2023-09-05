from django.contrib import admin
from .models import Form

# customizes form list display in admin form section
class FormAdmin(admin.ModelAdmin):
    list_display = ("first", "last", "occupation")
    search_fields = ("first", "last", "occupation")
    list_filter = ("date", "occupation")
    ordering = ("-first", )
    readonly_fields = ("email", )

admin.site.register(Form, FormAdmin)
