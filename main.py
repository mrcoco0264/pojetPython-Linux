choix_ordi='Doit etre X ou O'
#X, O
entree_utilisateur=input("Entrer soit X ou O :")
print(entree_utilisateur)
if entree_utilisateur=="exit" or "E" or "e":
    print("Vous etes ici")
    exit();
elif choix_ordi=="X" and entree_utilisateur=="O":
    print('{} et { }'.format(entree_utilisateur,choix_ordi))
