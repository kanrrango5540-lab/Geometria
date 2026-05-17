import math

def volume_box(length, width, height):
    volume_box = length * width * height
    return volume_box
"""
calcula el volumen de una caja
length: la longitud de la caja
width: el ancho de la caja
height: la altura de la caja
return: el volumen de la caja
"""

def volume_cone(radius, height):
    volume_cone= (1/3) * math.pi * radius ** 2 * height
    return volume_cone
"""
calcula el volumen de un cono
radius: el radio de la base del cono
height: la altura del cono
return: el volumen del cono
"""

def volume_sphere(radius):
    volume_sphere = (4/3) * math.pi * radius ** 3
    return volume_sphere
"""
calcula el volumen de una esfera
radius: el radio de la esfera
return: el volumen de la esfera
"""
