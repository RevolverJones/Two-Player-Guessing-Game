def gploop():
    import os
    a = int(input("Enter Random Number:"))
    os.system('cls'if os.name == 'nt' else 'clear')
    i = 0
    pont = 800
    list = []
    for i in range(3):


        while True:
                b = int(input('enter guess : '))    
                d = True
                c = 0      
                if b == a :
                        print('you win!!!' + "Your Points : " + str(pont))
                        list.append(pont)
                        print(f"Your Points: {list}")
                        break
                        
                if a != b:  
                        i += 1  
                pont = pont - 100          
                if b > a:
                        print('lower')
                elif b < a:
                        print('upper')
                elif a != b :
                        print('ridi')   
                if i == 8:
                        print(f"You Lost, You Got {pont} ponts!")
                        list.append(pont)
                        print(f"Your Points: {list}")
                        break
                
        print(sum(list))
