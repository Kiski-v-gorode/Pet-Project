from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, patronymic, phone_number, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, patronymic, phone_number, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.create_user(email, first_name, last_name, patronymic, phone_number, password)

        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["last_name", "first_name", "patronymic", "phone_number"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_staff(self):
        return self.is_admin


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    users = models.ForeignKey(CustomUser, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Post(models.Model):
    name = models.CharField(max_length=100)
    comments = GenericRelation(Comment)


class Article(models.Model):
    name = models.CharField(max_length=100)
    comments = GenericRelation(Comment)


class Task(models.Model):
    name = models.CharField(max_length=100)
    comments = GenericRelation(Comment)
