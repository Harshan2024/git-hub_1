import time

class chef:    
    def __init__(self,Name,veg_dish,non_veg_dish,):
        self.Name=Name
        self.veg_dish=veg_dish
        self.non_veg_dish=non_veg_dish

    def vegdish(self):
        time.sleep(3)
        print(f"The {self.veg_dish} is ready")

    def non_veg(self):
        time.sleep(5)
        print(f"The {self.non_veg_dish} is ready!")

# c1=chef("Harshan","Ghee rice","chicken noddle")
# c2=chef("Dixon","panner rice","mutton rice")
# c1.vegdish()
# c2.non_veg()

        