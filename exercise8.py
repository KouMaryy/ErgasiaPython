import random

scale = []
Numbers = []
s = 0
for i in range (-30,31) :
    scale.append(i)
Numbers = random.sample(scale,30)
flag = False
for i in range (28) :
    for j in range (i+1,29):
        for k in range (j+1,30):
            s = s + Numbers[i] + Numbers[j] + Numbers[k]
            if s == 0 :
                flag = True
                print ( "Συνδυασμός" , Numbers[i] , "+" , Numbers[j] , "+" , Numbers[k] )
            s = 0
if flag == False :
    print ( " Δεν υπάρχουν τέτοιες τριάδες" )

            
