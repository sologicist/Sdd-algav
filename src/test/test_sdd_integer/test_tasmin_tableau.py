import lib.sdd_integer.tasmin_tableau as tas
import random
import time


def testTasmin_tab():
  random_int_list = random.sample(range(1, 1000), 200)
  tasmin = []
  #print(random_int_list)

  print("Construction via AjoutsItératifs()\n")
  
 
  start_time = time.time()
  tasmin = tas.AjoutsIteratifs(tasmin, random_int_list)
  #tas.Print(tasmin)
  print("--- %s seconds ---" % (time.time() - start_time))
"""
  print("\n")
  print("Construction du tas via Construction()\n")
  tasmin2 = tas.Construction(random_int_list)
  tas.Print(tasmin2)
  
  print("\n")
  tas.SupprMin(tasmin)
  tas.Print(tasmin)
  print("\n")
  print("\nAlternance de SupprMin() et Ajout()\n")

  print("\nSupression\n")
  tas.SupprMin(tasmin)
  tas.Print(tasmin)

  print("\nSupression\n")
  tas.SupprMin(tasmin)
  tas.Print(tasmin)

  print("\nAjout\n")
  tas.Ajout(tasmin, 87)

  print("\nAjout\n")
  tas.Ajout(tasmin, 78)
  tas.Print(tasmin)

  print("\nSupression\n")
  tas.SupprMin(tasmin)
  tas.Print(tasmin)

  print("\n")
  print("Alternance de SupprMin() et Ajout()\n")
  print("\nSupression\n")
  tas.SupprMin(tasmin2)
  tas.Print(tasmin2)

  print("\nSupression\n")
  tas.SupprMin(tasmin2)
  tas.Print(tasmin2)

  print("\nAjout\n")
  tas.Ajout(tasmin2, 56)
  tas.Print(tasmin2)

  print("\nAjout\n")
  tas.Ajout(tasmin2, 89)
  tas.Print(tasmin2)

  print("\nSupression\n")
  tas.SupprMin(tasmin2)
  tas.Print(tasmin2)

  print("\nUnion de tas\n")
  tasminres = tas.Union(tasmin, tasmin2)
  tas.Print(tasminres)"""
