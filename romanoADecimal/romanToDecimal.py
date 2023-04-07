import unittest 

def roman_to_decimal(roman):
    total=0
    for letter in roman:
        if letter=='I':
            total+=1
        elif letter=='V':
            if 0<total<=1:
                total=-1
            total+=5 
        elif letter=='X':
            if 0<total<=1:
                total=-1
            total+=10
        elif letter=='L':
            if 0<total<=10:
                total=-10
            total+=50    
        elif letter=='C':
            if 0<total<=10:
                total=-10
            total+=100
        elif letter=='D':
            if 0<total<=100:
                total=-100
            total+=500    
        elif letter=='M':
            if 0<total<=100:
                total=-100
            total +=1000                
    return total        
            
            
               

