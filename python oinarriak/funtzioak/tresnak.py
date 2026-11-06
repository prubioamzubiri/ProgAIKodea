def nota_baliagarria(nota):

    if nota >= 0 and nota <= 10:
        baliagarria = True
    else:
        baliagarria = False

    return baliagarria

def nota_baliagarriak(notak):
    baliagarriak = True

    for nota in notak:
        if not nota_baliagarria(nota):
            baliagarriak = False
            
        
    if baliagarriak:
        print("valio dute")
    else:
        print("Baten bat, ez du balio")