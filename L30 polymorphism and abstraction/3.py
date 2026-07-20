class India():
    def capital(self):
        print("New Delhi is the capital of India ")
    def language(self):
        print("Hindi is the most widely spoken laguage in India ")
    def type(self):
        print("India is a developping country ")

class USA():
    def capital(self):
        print("Washigton D.C is the capital of the United States of America")
    def language(self):
        print("English is the primary language of USA")
    def type (self):
        print("USA is a developped country ")
    
obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
  country.capital()
  country.language()
  country.type()

