import lib.sdd_bigint.tasmin_binaire_bigint as tas
import lib.utilitaire as ut


def testTasmin():

  #random_int_list = random.sample(range(1, 21), 12)
  samples = ut.prog_list_constr(10,10,0)
  tasmin = tas.TasMin()
  tasmin2 = tas.TasMin()

  print("Construction via AjoutsItératifs()\n")
  tasmin2.AjoutsIteratifs(samples[0])

  print("\n")
  print("Construction du tas via Construction()\n")
  tasmin.Construction(samples[0])

  print("\n")

  tasmin.afficher_arbre(tasmin.racine)
  tasmin2.afficher_arbre(tasmin.racine)

  print("\n")
  print("Alternance de SupprMin() et Ajout()\n")
  tasmin.SupprMin()
  tasmin.afficher_arbre(tasmin.racine)
  tasmin.SupprMin()
  tasmin.afficher_arbre(tasmin.racine)
  tasmin.Ajout("0xdf6943ba6d51464f6b02157933bdd9ad")
  tasmin.Ajout("0xd192acf4c06fe7c7df042f07d290bdd4")
  tasmin.afficher_arbre(tasmin.racine)
  tasmin.SupprMin()
  tasmin.afficher_arbre(tasmin.racine)

  print("\nUnion de tas\n")
  #tasminres = tasmin.Union(tasmin2)
  #tasminres.afficher_arbre(tasminres.racine)
  samples1 = ut.prog_list_constr(5,5,0)
  samples2 = ut.prog_list_constr(5,10,5)
  tasmin1 = tas.TasMin()
  tasmin2 = tas.TasMin()
  tasmin1.Construction(samples1[0])
  tasmin2.Construction(samples2[0])
  tasmin1.afficher_arbre(tasmin1.Union(tasmin2).racine)
