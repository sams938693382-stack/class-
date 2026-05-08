class mashina:
    def __init__(self, rang, madel, nomi):
        self.rang = rang
        self.madel = madel
        self.nomi = nomi
    def get_info(self):
        data= f"{self.rang} rangli {self.madel.title()} {self.nomi}"
        return data


# car1 = mashina("qora", "Gentra", "Cobalt")
# car2 = mashina("oq", "Malibu", "Spark")
# print(car1.get_info())

class mashina_salon(mashina):
    def __init__(self,rang,madel,nomi,salon_nomi,salon_manzili):
        super().__init__(rang,madel,nomi)
        self.snomi = salon_nomi
        self.smanzili = salon_manzili
    def get_info(self):
        return f"{super().get_info()} {self.snomi} salonida {self.smanzili} manzilida sotuvda"


asalon = mashina_salon("qora", "Gentra", "Cobalt", "Avto Lider", "Toshkent" )
print(asalon.get_info())

