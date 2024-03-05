from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Admin, Student, User


class CustomUserAdmin(UserAdmin):
    # 添加或修改想要顯示的欄位
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


# 註冊自定義的 UserAdmin
admin.site.register(User, CustomUserAdmin)

admin.site.register(Admin)
admin.site.register(Student)
