import datetime

year= int(input('Επιλέξτε ένα έτος (σε μορφη αριθμου): '))
month= int (input('Επιλέξτε έναν μήνα (σε μορφή αριθμού) : '))
if month<1 or month>12:
    print ("ΠΑΡΑΚΑΛΩ ΔΩΣΤΕ ΕΓΚΥΡΟ ΑΡΙΘΜΟ ΜΗΝΑ(1-12) ")
    
day = datetime.date(year,month,1)
start = day.weekday()    
weekdays = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa','Su']
if month == 1 :
    monthname = "January"
elif month == 2 :
    monthname = "February"
elif month == 3 :
    monthname = "March"
elif month == 4 :
    monthname = "April"
elif month==5 :
    monthname = "May"
elif month == 6 :
    monthname = "June"
elif month == 7 :
    monthname = "July"
elif month==8 :
    monthname = "August"
elif month == 9 :
    monthname = "September"
elif month==10 :
    monthname = "October"
elif month == 11 :
    monthname = "November"
elif month==12 :
    monthname = "December"
else :
    print ("Παρακαλώ δώστε έγκυρο αριθμό μήνα (1-12) ")

print('{0} {1}'.format(monthname, year).center(20, ' '))
print(''.join(['{0:<3}'.format(w) for w in weekdays]))
print('{0:<3}'.format('')*start, end='')

for i in range (31):
    if month==2 :
         if (year%4==0 and year%100!=0) or year%400==0 :
             if i+1 ==30 :
                 break
         elif i+1 == 29 :
                 break
    elif month <= 7 :
        if month%2 == 0:
            if i+1 == 31 :
                break
    elif i >= 8 :
        if month%2 != 0:
            if i+1 == 31 :
                break
    print('{0:<3}'.format(i+1), end='')
    start += 1
    if start == 7:
        print()
        start = 0 
