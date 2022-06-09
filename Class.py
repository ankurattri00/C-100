class car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarated")

    def change_gear(self,gear_type):
        print("gear changed")

lamborghini=car("terso","white","lamborghini",550)
print(lamborghini.start())
print(lamborghini.color)
print (lamborghini.company)
print(lamborghini.speed_limit)