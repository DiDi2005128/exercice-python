from outils import convertir_note, moyennes, mention

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

nb_valide = 0

for note in notes_brutes:
    note_convertie = convertir_note(note)

    if note_convertie is not None:
        nb_valide += 1


print(f"nombre valide", nb_valide)