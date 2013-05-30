from django.contrib import admin
from project.models import Continent
from project.models import Language
from project.models import Country
from extraadminfilters.filters import UnionFieldListFilter


class CountryAdmin(admin.ModelAdmin):
    list_display = ['description', 'continent', 'list_languages', ]
    filter_horizontal = ['languages', ]

    # list_filter = ['continent', 'languages', ]
    # multiple_selection_list_filter = ['continent', 'languages', ]

    list_filter = (
        #('continent', UnionFieldListFilter),
        'continent',
        ('languages', UnionFieldListFilter),
    )

    def list_languages(self, instance):
        return ', '.join([language.description for language in instance.languages.all()])
    list_languages.short_description = 'Languages'

admin.site.register(Continent)
admin.site.register(Language)
admin.site.register(Country, CountryAdmin)
