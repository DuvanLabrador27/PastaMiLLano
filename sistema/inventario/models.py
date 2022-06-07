from django.db import models
from django.contrib.auth.models import AbstractUser


# MODELOS

#--------------------------------USUARIO------------------------------------------------
class Usuario(AbstractUser):
    #id
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    nivel = models.IntegerField(null=True) #1: Administrador, 2: Cliente (Nivel de acceso)

    @classmethod
    def numeroRegistrados(self):
        return int(self.objects.all().count() )   

    @classmethod
    def numeroUsuarios(self,tipo):
        if tipo == 'administrador':
            return int(self.objects.filter(is_superuser = True).count() )
        elif tipo == 'usuario':
            return int(self.objects.filter(is_superuser = False).count() )




#---------------------------------------------------------------------------------------

 
#-------------------------------PRODUCTO------------------------------------------------
class Producto(models.Model):
    #id
    decisiones =  [('1','Unidad'),('2','Pasa palos')]
    descripcion = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    disponible = models.IntegerField(null=True)
    categoria = models.CharField(max_length=20,choices=decisiones)
    tiene_iva = models.BooleanField(null=True)

    @classmethod
    def numeroRegistrados(self):
        return int(self.objects.all().count() )
   

    @classmethod
    def productosRegistrados(self):
        objetos = self.objects.all().order_by('descripcion')
        return objetos


    @classmethod
    def preciosProductos(self):
        objetos = self.objects.all().order_by('id')
        arreglo = []
        etiqueta = True
        extra = 1

            #El objeto enumerate produce pares que contienen un recuento (desde el inicio, que por defecto es cero) 
            # y un valor generado por el argumento iterable.
        for indice,objeto in enumerate(objetos):
            arreglo.append([])
            if etiqueta:
                arreglo[indice].append(0)
                arreglo[indice].append("------")
                etiqueta = False
                arreglo.append([])

            arreglo[indice + extra].append(objeto.id)
            precio_producto = objeto.precio
            arreglo[indice + extra].append("%d" % (precio_producto) )  

        return arreglo 

    @classmethod
    def productosDisponibles(self):
        objetos = self.objects.all().order_by('id')
        arreglo = []
        etiqueta = True
        extra = 1

        for indice,objeto in enumerate(objetos):
            arreglo.append([])
            if etiqueta:
                arreglo[indice].append(0)
                arreglo[indice].append("------")
                etiqueta = False
                arreglo.append([])

            arreglo[indice + extra].append(objeto.id)
            productos_disponibles = objeto.disponible
            arreglo[indice + extra].append("%d" % (productos_disponibles) )  

        return arreglo 
#---------------------------------------------------------------------------------------


#------------------------------------------CLIENTE--------------------------------------
class Cliente(models.Model):
    #id
    cedula = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=200)
    nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20,null=True)
    correo = models.CharField(max_length=100)
    correo2 = models.CharField(max_length=100,null=True)

    @classmethod
    def numeroRegistrados(self):
        return int(self.objects.all().count() )

    @classmethod
    def cedulasRegistradas(self):
        objetos = self.objects.all().order_by('nombre')
        arreglo = []
        for indice,objeto in enumerate(objetos):
            arreglo.append([])
            arreglo[indice].append(objeto.cedula)
            nombre_cliente = objeto.nombre + " " + objeto.apellido
            arreglo[indice].append("%s. C.I: %s" % (nombre_cliente,self.formatearCedula(objeto.cedula)) )
 
        return arreglo   


    @staticmethod
    def formatearCedula(cedula):
        return format(int(cedula), ',d')        
#-----------------------------------------------------------------------------------------        
   
