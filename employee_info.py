class CEO():
    
    def __init__(self,ad,yas,maas):
        self.ad = ad
        self.yas = yas
        self.maas = maas
        
    def showInfos(self):
        print("Calisanin adi: {} \nCalisanin yasi: {}\nCalisanin maasi: {} TL"
              .format(self.ad,self.yas,self.maas))
        
class Junior(CEO):
    
    def __init__(self,ad,yas,maas):
        super().__init__(ad,yas,maas)
        
    def showInfos(self):
        super().showInfos()
        print("--JUNIOR-- Bu sinif, giris seviyesi yazilimci icindir!")
        
class Mid_Level(CEO):
    
    def __init__(self,ad,yas,maas):
        super().__init__(ad,yas,maas)
        
    def showInfos(self):
        super().showInfos()
        print("--MID LEVEL-- Bu sinif, orta seviye yazilimci icindir!")
        
class Senior(CEO):
    
    def __init__(self,ad,yas,maas):
        super().__init__(ad,yas,maas)
        
    def showInfos(self):
        super().showInfos()
        print("--SENIOR-- Bu sinif, ileri seviye yazilimci icindir!")
