"""Core utlis."""
import os
import time
import uuid

from django.contrib.admin.sites import AdminSite


class SetupAdminSite(AdminSite):
    pass

admin_setup = SetupAdminSite(name="admin_setup")


def generate_file(folder_name, filename):
    file_name, file_extension = os.path.splitext(filename)
    filepath = '%s/%s%s%s' % (folder_name, str(time.time())[:5],
                              str(uuid.uuid4()), file_extension)

    return filepath
