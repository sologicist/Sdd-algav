import lib.sdd_bigint.tasmin_tableau_bigint as tas
import lib.utilitaire as ut


def testTasmin():

  #random_int_list = random.sample(range(1, 21), 12)
  samples = ut.prog_list_constr(10,10,0)
  tasmin = []
  tasmin2 = []

  print("Construction via AjoutsItératifs()\n")
  tasmin2 = tas.AjoutsIteratifs(tasmin2, samples[0])

  print("\n")
  print("Construction du tas via Construction()\n")
  tasmin = tas.Construction(samples[0])

  print("\n")

  tas.Print(tasmin)
  tas.Print(tasmin2)

  print("\n")
  print("Alternance de SupprMin() et Ajout()\n")
  tas.SupprMin(tasmin)
  tas.Print(tasmin)
  tas.SupprMin(tasmin)
  tas.Print(tasmin)
  tas.Ajout(tasmin, "0xdf6943ba6d51464f6b02157933bdd9ad")
  tas.Ajout(tasmin, "0xd192acf4c06fe7c7df042f07d290bdd4")
  tas.Print(tasmin)
  tas.SupprMin(tasmin)
  tas.Print(tasmin)

  print("\nUnion de tas\n")
  #tasminres = tasmin.Union(tasmin2)
  #tasminres.afficher_arbre(tasminres.racine)
  samples1 = ut.prog_list_constr(5,5,0)
  samples2 = ut.prog_list_constr(5,10,5)
  tasmin1 = []
  tasmin2 = []
  tasmin1 = tas.Construction(samples1[0])
  tasmin2 = tas.Construction(samples2[0])
  tas.Print(tas.Union(tasmin1,tasmin2))