#Bkényi Dávid [B]  2023.03.08.


szam_sorozat = [15, 4 , 5, 19, 2]

def dolgozat():
    i = 0
    for szam in szam_sorozat:
        if szam <= i:
            print(f"ez a legkisebb szam: {szam} ")    
        i += 1
dolgozat()