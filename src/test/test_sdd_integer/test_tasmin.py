import lib.sdd_integer.tasmin_binaire as tas
import random


def testTasmin():

  random_int_list = random.sample(range(1, 21), 12)
  tasmin = tas.TasMin()
  tasmin2 = tas.TasMin()

  print("Construction via AjoutsItératifs()\n")
  tasmin2.AjoutsIteratifs(random_int_list)

  print("\n")
  print("Construction du tas via Construction()\n")
  tasmin.Construction(random_int_list)

  print("\n")

  tasmin.afficher_arbre(tasmin.racine)
  tasmin2.afficher_arbre(tasmin.racine)

  print("\n")
  print("Alternance de SupprMin() et Ajout()")
  tasmin.SupprMin()
  tasmin.afficher_arbre(tasmin.racine)
  tasmin.SupprMin()
  tasmin.afficher_arbre(tasmin.racine)
  tasmin.Ajout(87)
  tasmin.Ajout(78)
  tasmin.afficher_arbre(tasmin.racine)
  tasmin.SupprMin()
  tasmin.afficher_arbre(tasmin.racine)

  print("\n")
  print("Alternance de SupprMin() et Ajout()")
  tasmin2.SupprMin()
  tasmin2.afficher_arbre(tasmin2.racine)
  tasmin2.SupprMin()
  tasmin2.afficher_arbre(tasmin2.racine)
  tasmin2.Ajout(88)
  tasmin2.afficher_arbre(tasmin2.racine)
  tasmin2.Ajout(56)
  tasmin2.SupprMin()
  tasmin2.afficher_arbre(tasmin2.racine)

  print("Union de tas")
  #tasminres = tasmin.Union(tasmin2)
  #tasminres.afficher_arbre(tasminres.racine)
