from rest_framework import permissions

from .permission import IsStaffEditorPermission

class PermissionMixins():
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]



