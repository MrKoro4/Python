line = 5
width = 9
for i in range(line) :
    for j in range(width) :
        
        #sapin = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        
        if j == round(width/2)-i or j == round(width/2)+i:
            print("*", end='')
            continue
            
        if i == 2 :
            if j == 4 :
                print('*', end='')
                continue
            
        if i == 3 : 
            if j%2 != 0 :
                print('*', end='')
                continue
        
        if i == 4 : 
            if j%2 == 0 :
                print('*', end='')
                continue
            
        print('.', end='')
                
    print('\n', end='')