from django.test import TestCase
from django.db import models
from app.models import Usuario

def calcula_media(lista):
    return sum(lista)/len(lista)

assert(calcula_media([5, 10, 7.5]) == 7.5)
assert(calcula_media([4, 8]) == 6)

# Si se encuentra un error, se levanta el error "AssertionError"
# assert(calcula_media([4, 8]) == 1) 

