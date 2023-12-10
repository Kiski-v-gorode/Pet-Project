from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import CustomUser, Comment, Post, Article, Task


# Register your models here.


class UserCreationForm(forms.ModelForm):
    """Форма для создания новых пользователей. Включает все необходимые поля, а также повторяющийся пароль."""
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "patronymic", "phone_number"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    """
    Форма для обновления пользователей.
    Включает все поля пользователя, но заменяет поле пароля на отключенное поле отображения хэша пароля администратора.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "patronymic",
                  "phone_number", "password", "is_active", "is_admin"]


class UserAdmin(BaseUserAdmin):
    # Формы для добавления и изменения экземпляров пользователей
    form = UserChangeForm
    add_form = UserCreationForm

    """
    Поля, которые будут использоваться при отображении модели пользователя. 
    Они переопределяют определения в базовом UserAdmin, которые ссылаются на определенные поля в auth.User.
    """

    list_display = ["email", "first_name", "last_name", "patronymic", "is_admin"]
    list_filter = ["is_admin"]

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name", "patronymic", "phone_number"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    """
    add_fieldsets не является стандартным атрибутом ModelAdmin. 
    UserAdmin переопределяет get_fieldsets, чтобы использовать этот атрибут при создании пользователя.
    """

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "first_name", "last_name", "patronymic", "phone_number", "password1", "password2"]
            }
        )
    ]

    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["content_object", "content", "users"]