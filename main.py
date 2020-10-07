import random
choix_aleatoireOrdi=2
VictoireOrdi=0
VictoireJoueur=0
NombreXJoueur=0
NombreOJoueur=0
NombreXOrdi=0
NombreO_Ordi=0
tres = 0
choix_ordi='n'
nbrConsecutifOrdi=0
nbrConsecutifJoueur=0
lastChoiceOrdi='n'
lastChoiceJoueur='n'

for i in range(4) :
  if nbrConsecutifJoueur!=3 or nbrConsecutifOrdi != 3:
      entree_utilisateur = input('Entrer soit X ou O :')
      choix_aleatoireOrdi =random.randint(0,1)
      if choix_aleatoireOrdi==1:
        choix_ordi='X'
      elif choix_aleatoireOrdi==0:
        choix_ordi = 'O'
      else :
        choix_ordi='X'
      if entree_utilisateur == 'E' or  entree_utilisateur =='e' or  entree_utilisateur == 'Exit':
         exit()
      elif choix_ordi == 'X' and entree_utilisateur == 'X':
        if lastChoiceOrdi!='X':
          nbrConsecutifOrdi=0
        lastChoiceOrdi=choix_ordi
        NombreXOrdi+=1
        nbrConsecutifOrdi += 1
        print('{} et {} Vous n\'avez pas le droit de choisir X '.format(entree_utilisateur, choix_ordi))
        nbrConsecutifOrdi+=1
      elif choix_ordi=='X' and entree_utilisateur=='O':
        if lastChoiceOrdi != 'X':
          nbrConsecutifOrdi = 0
        if lastChoiceJoueur!='O' :
          nbrConsecutifJoueur=0
        lastChoiceOrdi = choix_ordi
        NombreXOrdi += 1
        NombreOJoueur+=1
        nbrConsecutifJoueur += 1
        nbrConsecutifOrdi += 1
      elif choix_ordi == 'O' and entree_utilisateur == 'X':
        if lastChoiceOrdi!='O':
          nbrConsecutifOrdi=0
        if lastChoiceJoueur!='X':
          nbrConsecutifJoueur = 0
        lastChoiceOrdi=choix_ordi
        lastChoiceJoueur=entree_utilisateur
        NombreO_Ordi += 1
        NombreXJoueur += 1
        nbrConsecutifJoueur += 1
        nbrConsecutifOrdi += 1
      elif choix_ordi == 'O' and entree_utilisateur == 'O':
        if lastChoiceOrdi != 'O':
          nbrConsecutifOrdi = 0
        if lastChoiceJoueur != 'O':
          nbrConsecutifJoueur = 0
        lastChoiceOrdi = choix_ordi
        lastChoiceJoueur = entree_utilisateur
        NombreO_Ordi += 1
        NombreOJoueur += 1
        nbrConsecutifJoueur += 1
        nbrConsecutifOrdi += 1
        lastChoiceOrdi = choix_ordi
  elif nbrConsecutifJoueur==3 :
    break
  elif nbrConsecutifOrdi==3 :
    break
if nbrConsecutifJoueur>nbrConsecutifOrdi :
  print('Le Joueur Gagne!')
elif nbrConsecutifJoueur<nbrConsecutifOrdi :
  print("L'ordinateur Gagne !")
else :
  print("C'est égalité. !")
print('Joueur a jouer {} X et {} O'.format(NombreXJoueur,NombreOJoueur))
print('Oridi a jouer {} X et {} O'.format(NombreXOrdi,NombreO_Ordi))
# O
