#
#    DjangoPBX
#
#    MIT License
#
#    Copyright (c) 2016 - 2022 Adrian Fretwell <adrian@djangopbx.com>
#
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.
#
#    Contributor(s):
#    Adrian Fretwell <adrian@djangopbx.com>
#

from django.contrib import admin
from django.forms import ModelForm
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from pbx.commonfunctions import DomainFilter, DomainUtils
from pbx.commonwidgets import PlayerAdminFileFieldWidget

from .models import (
    Recording, CallRecording
)
from .listfilters import YearsListFilter, MonthsListFilter, DaysListFilter


class RecordingsAdminForm(ModelForm):

    class Meta:
        model = Recording
        widgets = {
            "filename": PlayerAdminFileFieldWidget(),
        }
        fields = '__all__'



class RecordingsResource(resources.ModelResource):
    class Meta:
        model = Recording
        import_id_fields = ('id', )


class RecordingAdmin(ImportExportModelAdmin):
    resource_class = RecordingsResource
    form = RecordingsAdminForm

    readonly_fields = ['created', 'updated', 'synchronised', 'updated_by']
    fieldsets = [
        (None,               {'fields': ['domain_id', 'name', 'filename', 'description', 'filestore']}),
        ('update Info.',   {'fields': ['created', 'updated', 'synchronised', 'updated_by'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'filename', 'description')
    list_filter = (DomainFilter, 'name')

    ordering = [
        'domain_id',
        'name'
    ]

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user.username
        if not change:
            obj.domain_id = DomainUtils().domain_from_session(request)
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.filename.delete(save=False)
        super().delete_model(request, obj)


class CallRecordingsAdminForm(ModelForm):

    class Meta:
        model = Recording
        widgets = {
            "filename": PlayerAdminFileFieldWidget(),
        }
        fields = '__all__'


class CallRecordingsResource(resources.ModelResource):
    class Meta:
        model = CallRecording
        import_id_fields = ('id', )


class CallRecordingAdmin(ImportExportModelAdmin):
    show_facets = admin.ShowFacets.NEVER
    resource_class = RecordingsResource
    form = CallRecordingsAdminForm

    search_fields = ['description']
    readonly_fields = ['created', 'updated', 'synchronised', 'updated_by']
    fieldsets = [
        (None,               {'fields': ['domain_id', 'name', 'filename', 'year', 'month', 'day', 'description', 'filestore']}),
        ('update Info.',   {'fields': ['created', 'updated', 'synchronised', 'updated_by'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'year', 'month', 'day', 'filename', 'description')
    list_filter = (DomainFilter, YearsListFilter, MonthsListFilter, DaysListFilter)

    ordering = [
        '-created',
        'name'
    ]

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user.username
        if not change:
            obj.domain_id = DomainUtils().domain_from_session(request)
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.filename.delete(save=False)
        super().delete_model(request, obj)


admin.site.register(Recording, RecordingAdmin)
admin.site.register(CallRecording, CallRecordingAdmin)
