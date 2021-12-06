line = 5
width = 9
for i in range(line) :
    for j in range(width) :
        
        if i == 0 :
            if j == round(width/2) :
                print("*", end='')
                continue
            
        if i == 1 :
            if j == round(width/2)-1 or j == round(width/2)+1 :
                print("*", end='')
                continue
            
        if i == 2 :
            if j == round(width/2) or j == round(width/2)-2 or j == round(width/2)+2 :
                print("*", end='')
                continue
            
        if i == 3 :
            if j == round(width/2)-1 or j == round(width/2)+1 or j == round(width/2)-3 or j == round(width/2)+3 :
                print("*", end='')
                continue
            
        if i == 4 :
            if j == round(width/2) or j == round(width/2)+2 or j == round(width/2)-2 or j == round(width/2)+4 or j == round(width/2)-4 :
                print("*", end='')
                continue
            
        print('.', end='')
                
    print('\n', end='')
