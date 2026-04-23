class Cook:
    def prepare_dish(self):
        self.cutter = Cutter()
        self.cutter.cut_vegetables()
        self.boiler = Boiler()
        self.boiler.boil_vegetables()


class Cutter:
    def cut_vegetables(self):
        print("All vegetables are cut")


class Boiler:
    def boil_vegetables(self):
        print("All vegetables are boiled")


cook = Cook()
cook.prepare_dish()