import random
n = random.randint(1,1000)   
p = -1        
while p != n:      
    p =int(input())      
    if p > n:        
        print("<")      
    elif p < n:         
        print(">")      
    else:         
        print("Вы угадали, это число = " + str(n))
        break