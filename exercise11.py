import random

Alphabet = [ "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z" ]
Square = []
for i in range (100):
    Square.append([])
for i in range (100):
    for j in range (100):
        Square[i].append(random.choice(Alphabet))
#Παραγωγή τετραγώνου 100*100 
for i in range (100): 
    for j in range (100):
        #print (Square[i][j] , end='')
    #print ()
        
print ("Παρακαλώ φτιάξτε ένα αρχείο κειμένου ( .txt) με 100 λέξεις (παρακαλώ κάθε γραμμή να περιέχει μια μόνο λέξη) και στη συνέχεια  ")
name = input ( "δώστε το όνομα του αρχείου : " )
infile = open (name , 'r' )
family = [line.rstrip() for line in infile]
infile.close()
flag = False
for word in range (100):     
    for i in range (100):
        string=""
        c = 0
        for letter in family[word] :
            j = c
            while j < 100:
                if letter == Square[i][j] :
                    string = string + letter
                    c=j+1
                    break
                else:
                    string=""
                    j = j+1

        if string == family[word]:
            print (family[word])
            flag = True
            break
    for j in range (100):
            string=""
            c = 0
            for letter in family[word] :
                i=c
                while i < 100: 
                    if letter == Square[i][j] :
                        string = string + letter
                        c = i +1
                        break
                    else:
                        string=""
                        i=i+1
            if string == family[word]:
                print (family[word])
                flag = True
                break
if flag == False :
    print ("Δυστυχώς δεν υπάρχει καμία λέξη στο τετράγωνο")
                   


