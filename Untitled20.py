#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Animal:
    def __init__(self,name):
       self.name = name
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__()
        self.breed = breed
    def showme(self):
        print(f"{self.breed}:")
        
dog1 = Dog("havv")
dog1.showme()

        


# In[19]:


class Kisi:
    def __init__(self,isim,yas):
        self.isim = isim
        self.yas = yas
    def showme(self):
        print(f"{self.isim}:{self.yas}")
class Student(Kisi):
    def __init__(self,isim,yas,number):
        super().__init__(isim,yas)
        
        self.number = number      
    def showme(self):
        super().showme()
        print(f":{self.number}")
        
ogr1 = Student("azat",23,12345)

ogr1.showme()


# In[20]:


class Animal:
    def speak(self):
        print("hayvanların sesleri vardır")
        
class Dog(Animal):
    def speak(self):
        print("kopekler havlar")
class Kedi(Animal):
    def speak(self):
        print("Kediler miavlar")
        
dog = Dog()
kedi = Kedi()

dog.speak()
kedi.speak()


# In[30]:


class GenelCalisan:
    def __init__(self,name ,salary,departman):
        self.name = name
        self.salary = salary
        self.departman = departman
    def bilgi(self):
        print(f"{self.name} : {self.salary} : {self.departman}")
class Mudur(GenelCalisan):
     def __init__(self,name,salary,departman,team_size,butce12 = 1000000):
        super().__init__(name,salary,departman)
        self.team_size = team_size
        self.butce12 = butce12
        
     def bilgi(self):
        super().bilgi()
        print(f"ekip sayısı :{self.team_size} ")
        
class Yonetici(Mudur):
    def __init__(self,name,salary,departman,team_size,butce12):
         super().__init__(name,salary,departman,team_size)
         
         
            
         
    def bilgi(self):
        super().bilgi()
        print(f"butce :{self.butce} ")
        
calisan1 = GenelCalisan("azat",56000,"software developer")
mudur = Mudur("ali",56000,"software developer",23)

yonetici = Yonetici("ali2",56000,"software developer",23,120000)

calisan1.bilgi()
mudur.bilgi()
yonetici.bilgi()


# In[ ]:




