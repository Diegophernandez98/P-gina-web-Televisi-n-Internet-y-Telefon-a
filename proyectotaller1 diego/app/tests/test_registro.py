from django.test import TestCase
from app.models import *

class UsuarioTestCase(TestCase):
    def setUp(self):
        # Configuración inicial que se ejecutará antes de cada prueba
        self.usuario = Usuario.objects.create(
            rut="20097529-6",
            nombre="Alexander",
            apellido="Hernandez",
            correo="Alexander123@gmail.com",
            numero="39421129",
            comuna="Osorno",
            direccion="Matto Grosso #1260",
            contrasena="Alex123",
            rol_id=1,
            fecha_ingreso="2023-12-10"  # Cambia a tu formato de fecha
        )

    def test_nombre_de_prueba(self):
        # Ejemplo de una prueba
        self.assertEqual(self.usuario.nombre, "Alexander")
        self.assertTrue(self.usuario.rol_id == 1)
