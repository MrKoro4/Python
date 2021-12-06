def corpulence(kg,m):
    imc = (kg/((m)**2))
    if imc <= 16:
        print("Interpétration OMS: maigreur extrême")
        print("Risque de maladie: élvé")
    elif 16.4 <= imc <= 18:   
        print("Interpétration OMS: Insuffisance pondérale")
        print("Risque de maladie: moyen")    
    elif 18.5 <= imc <= 24.9:
        print("Interpétration OMS: Corpluence normal")
        print("Risque de maladie: faible")
    elif 25 <= imc <= 29.9:
        print("Interpétration OMS: Surpoids")
        print("Risque de maladie: moyen")
    elif 30 <= imc <= 34.9:
        print("Interpétration OMS: Obésité")    
        print("Risque de maladie: élevé")
    elif 35 <= imc <= 40:
        print("Interpétration OMS: Obésité sévère") 
        print("Risque de maladie: très élévé")    
    else:
        print("Interpétration OMS: Obésité morbide")    
        print("Risque de maladie: extrêmement élevé")

kg = float(input("kg = "))   
m = float(input("m = "))  
corpulence(kg, m)   
 