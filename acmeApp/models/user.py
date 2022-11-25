from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password 
from .sede import Sede

#se crean los usuarios en el sistema de utenticacion 
class UserManager(BaseUserManager): 
    
    #crea usuario lo guarda en la BD y retorna el usuario
    def create_user(self, username, password=None): 
        
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username) 
        user.set_password(password)
        user.save(using=self._db) 
        return user

    #crea un usuario administrador 
    def create_superuser(self, username, password):
        
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#modelo de user 
class User(AbstractBaseUser, PermissionsMixin): #herencia multiple 
    
    #Creacion de atributos para las tablas de la BD
    id = models.CharField (max_length = 10, primary_key= True, unique=True, null=False)
    username = models.CharField('Username',unique=True, max_length = 20,null=False) 
    password = models.CharField('Password', max_length = 256,null=False)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE,null=False)

    #crear usuario 
    def save(self, **kwargs): 
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN' 
        self.password = make_password(self.password, some_salt) 
        super().save(**kwargs) 

    objects = UserManager() 
    USERNAME_FIELD = 'username' 
