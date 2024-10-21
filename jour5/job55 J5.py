l=[1,2,3,4,5,]
print("la deuxiéme valeur de la liste:",l[1])
def replace(l):
     new_valeur = l[2]+l[4]
     l[3]= new_valeur
     l.pop(3)
     print(l)
     l.insert(3, new_valeur)
     print(l)
   
replace(l)

  
  