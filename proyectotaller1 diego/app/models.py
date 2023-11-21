from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=20, null=False)

class Usuario(models.Model):
    rut = models.CharField(max_length=12, unique=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=15, null=False)
    comuna = models.CharField(max_length=20, null=False)
    direccion = models.CharField(max_length=100, null=False)
    contrasena = models.CharField(max_length=50, default='123', null=False)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=False, blank=True, default=9999999)

class Tipo_Servicio(models.Model):
    nombre = models.CharField(max_length=15, null=False)

class Plan_Internet(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    velocidad = models.IntegerField(null=False)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    tiempo_contrato = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=255, default='default')

class Plan_Television(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    canales_SD = models.IntegerField(null=False)
    canales_HD = models.IntegerField(null=False)
    canales_adicionales = models.CharField(max_length=255, null=True)
    tiempo_contrato = models.IntegerField(null=False)
    tipo_television = models.CharField(max_length=50, blank=True, null=False)
    descripcion = models.CharField(max_length=255, default='default')

class Plan_Telefonia(models.Model):
    nombre = models.CharField(max_length=25, null=False)
    gigas = models.IntegerField(null=False)
    minutos = models.IntegerField()
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    tipo_telefonia = models.CharField(max_length=50, blank=True, null=False)
    tiempo_contrato = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=255, default='default')

class Suscripcion(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('suspendido', 'Suspendido'),
    ]
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    fecha_iniciacion = models.DateField(null=False)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, null=False)

class Descuento(models.Model):
    nombre = models.IntegerField(null=False)

class Boleta(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, default=9999999)
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE, null=False)
    fecha_emision = models.DateField(null=False)
    fecha_vencimiento = models.DateField(null=False)
    detalles = models.CharField(max_length=255, null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    valor_con_descuento = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=9999999)
    descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE, null=False, default=9999999)
    plan_telefonia = models.ForeignKey(Plan_Telefonia, on_delete=models.CASCADE, null=True)
    plan_television = models.ForeignKey(Plan_Television, on_delete=models.CASCADE, null=True)
    plan_internet = models.ForeignKey(Plan_Internet, on_delete=models.CASCADE, null=True)

class Comentario(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    texto = models.TextField(null=False)
    fecha = models.DateField(null=False)
