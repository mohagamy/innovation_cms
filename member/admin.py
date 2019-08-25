"""Member custom admin."""
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group

from core.utlis import admin_setup
from member.models import Member


class MemberAdmin(ModelAdmin):
    list_display = (
        'id', 'full_name', 'username', 'creation_datetime', 'is_staff',
        'created_by', 'email', 'is_superuser', 'bio', 'start_datetime',
        'end_datetime')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'full_name', 'email')

    def save_model(self, request, obj, form, change):
        """Custom stuff here."""
        data = request.POST
        if not change:
            obj.set_password(data['password'])
        if change:
            old_password = Member.objects.get(id=obj.id).password
            if old_password != data['password']:
                obj.set_password(data['password'])
        obj.save()

admin.site.register(Member, MemberAdmin)
admin.site.unregister(Group)
admin_setup.register(Group)
