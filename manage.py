#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def check_admin_school_group():
    import django
    django.setup()
    from django.contrib.auth.models import Group, Permission
    group_name = 'admin-school'
    group, created = Group.objects.get_or_create(name=group_name)
    if not Group.objects.filter(name=group_name).exists():
        Group.objects.create(name=group_name)
        print(f'Successfully created group "{group_name}"')
            # 添加 myapp.view_activity 權限
    try:
        permission = Permission.objects.get(codename='view_activity', content_type__app_label='myapp')
        group.permissions.add(permission)
        print(f'Assigned permission "{permission.name}" to group "{group_name}"')
    except Permission.DoesNotExist:
        print(f'Permission "view_activity" not found in app "myapp"')
    else:
        print(f'Group "{group_name}" already exists')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
        check_admin_school_group()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
