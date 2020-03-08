from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
    )
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from django.utils.translation import ugettext as _

class UserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
     
        password1 = kwargs["password"]
        kwargs.pop("password")
        print(f"senha: {password1}")
        password = make_password(password=password1, salt=None, hasher='pbkdf2_sha256')
        print(f"senha criptografada: {password}")

       
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = False
        user.save(using=self._db)
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    foto = models.FileField(
        verbose_name=_('Foto'),
        upload_to= '',
        help_text=_('Escolha uma imagen')
    )
    nome = models.CharField(
        verbose_name=_('Nome'),
        max_length=50,
        blank=False,
        help_text=_('Inform your name')
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        
        )
    login = models.CharField(
        verbose_name=_('Login'),
        max_length=50,
        blank=False,
        unique=True,
        help_text=_('Inform your login')
    )
   
    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    )
    
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    USERNAME_FIELD = 'login'
    objects = UserManager()

    def __str__(self):
        return self.nome
