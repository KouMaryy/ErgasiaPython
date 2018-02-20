import random

Bingonums = [] 
for i in range(80) :
    Bingonums.append(i+1)        
random.shuffle(Bingonums)
Sum = 0
for round in range(1000) :
    #print ("Έναρξη" , round + 1 , "ου γύρου")
    ChoicesList = []
    Shots = []
    for player in range(100): 
        ChoicesList.append(random.sample(Bingonums,5))
        #print ("Οι επιλογές αριθμών του" , player + 1 , "ου παίκτη είναι: " , ChoicesList[player])
    for player in range (100):
        s = 0
        y = []
        for choice in range (5) :
            for i in range (80) :
                if ChoicesList[player][choice] == Bingonums[i] :
                    y.append(i+1)
                    break
        s = max(y)
        Shots.append(s)
    Sum = Sum + min(Shots)
Average = Sum / 1000
print ("Πρέπει να αναγγελθούν " , Average , "αριθμοί κατά ΜΕΣΟ ΟΡΟ ώστε να έχουμε Bingo")



 








        






