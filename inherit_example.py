class Vehicle:
    
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
class Cost:

    def __init__(self, cost) -> None:
        self.cost = cost

    def get_cost(self):
        return self.cost
    
    
class Car(Vehicle, Cost):
    
    def __init__(self, name, color, model, cost):
        self.model = model
        Vehicle.__init__(self, name, color)
        Cost.__init__(self, cost)
        

    def get_desciription(self):
        return "Auton nimi on " + self.get_name() + ", väriltään " + self.get_color() + " ja malliltaan " + self.model +" ja hinnaltaan " + self.get_cost()

auto = Car("Fiat", "sininen", "Punto", "10 000 euroa")
print(auto.get_desciription())
