from chef import chef,time
class cont_chef(chef):
    def __init__(self,name,vegdish,non_veg,spl_dish):
        super().__init__(name,vegdish,non_veg)
        self.spl_dish=spl_dish

    def special_dish(self):
        time.sleep(2)
        print(f"The {self.spl_dish} is ready")

cont1=cont_chef("Lucy","sambar","fish","grilled chicken")
cont1.special_dish()            