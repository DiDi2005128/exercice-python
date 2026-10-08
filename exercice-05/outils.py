def convertir_note(texte):
    return float(texte)

def moyennes(valeurs):
    return sum(valeurs)/len(valeurs)

def mention(note):
    for note in mention:
        if 11.99 > note >= 10:
            print("passable")
        elif 12 < note < 13.99:
            print("assez-bien")
        elif 14 < note < 15.99:
            print("bien")
        elif 16 < note < 17.99:
            print("tres-bien")
        else :
            print("excellent")

