class Kayak:
    brand = ""
    material = ""
    length = ""
    def __init__(self):
        print("Inicialización de la súper clase")
    def styles(self):
        print("Kayak class styles method")
    def activities(self):
        print("Kayak class activities method")
    def water_types(self):
        pass
    def features(self):
        print("Kayak class features method")

class PaddleKayak(Kayak):
    model = ""
    capacity = ""
    style = ""
    activity = ""
    def __init__(self):
        print("Inicialización de la sub clase")
    def available_colors(self):
        print("PaddleKayak subclass available_colors method")
        