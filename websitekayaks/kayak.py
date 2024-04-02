class Kayak:
    def __init__(self, brand, material, length):
        self.brand = brand
        self.material = material
        self.length = length
    def styles(self):
        print("Kayak class styles method")
    def activities(self):
        print("Kayak class activities method")
    def water_types(self):
        pass
    def features(self):
        print("Kayak class features method")

class PaddleKayak(Kayak):
    def __init__(self, model, capacity, style, activity):
        self.model = model
        self.capacity = capacity
        self.style = style
        self.activity = activity
    def available_colors(self):
        print("PaddleKayak subclass available_colors method")
        