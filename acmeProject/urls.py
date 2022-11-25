from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from acmeApp import views
from acmeApp.views.login import Login

urlpatterns = [
    path('login/', Login.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    #URLs modelo User
    path('usercreate/', views.UserCreateView.as_view()),#crear un usuario
    path('users/', views.UsersDetailView.as_view()),#obtener todos los usuarios
    path('user/<str:pk>/', views.UserDetailView.as_view()),#crud usuario 
    path('userupdate/<str:pk>/', views.UserUpdateView.as_view()),#actualizar datos completos usuario
    path('user-view/', views.LogUserDetailView.as_view()),#obtener y actualizar datos del usuario logueado

    #URLs modelo Sede
    path('sedecreate/', views.SedeCreateView.as_view()),#crear una sede 
    path('sedes/', views.SedesDetailView.as_view()),#obtener todas las sedes
    path('sede/<int:pk>/', views.SedeDetailView.as_view()),#crud sede
    
    #URLs modelo Proveedor
    path('proveedorcreate/', views.ProveedorCreateView.as_view()),#crear un proveedor
    path('proveedores/', views.ProveedoresDetailView.as_view()),#obtener todos los proveedores
    path('proveedor/<str:pk>/', views.ProveedorDetailView.as_view()),#crud proveedor

    #URLs modelo Producto
    path('productocreate/', views.ProductoCreateView.as_view()),#crear un producto
    path('productos/', views.ProductosDetailView.as_view()),#obtener todos los productos
    path('producto/<int:pk>/', views.ProductoDetailView.as_view()),#crud producto

    #URLs modelo Productoxsede
    path('pxscreate/', views.ProductoxsedeCreateView.as_view()),#agregar un producto en una sede
    path('productosxsede/', views.ProductosxsedeDetailView.as_view()),#obtener todos los productos de una sede
    path('productxsede/<int:pk>/', views.ProductoxsedeView.as_view()),#Get informacion sede
    path('productoxsede/<int:pk>/', views.ProductoxsedeDetailView.as_view()),#crud productoxsede
]

