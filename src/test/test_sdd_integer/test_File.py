import lib.sdd_integer.file as f
import random


def testFile():
  print("\n Test File\n")

  print("\n Construction de la file avec 3 éléments\n")
  random_int_list = random.sample(range(1, 120), 36)
  F = f.File()
  F.Construction(random_int_list)
  F.afficheFile()

  for _ in range(37):
    print(F.SupprMin())
  F.afficheFile()
    

  """print("\n Construction de la file avec 12 éléments\n")
  F2 = f.File()
  F2.Construction([1, 2, 3, 4, 5, 12, 23, 8, 9, 14, 11, 21, 55, 45])
  F2.afficheFile()

  random_int_list = random.sample(range(1, 41), 36)
  print("\n Construction de la file avec 36 éléments\n")
  F3 = f.File()
  F3.Construction(random_int_list)
  F3.afficheFile()

  print("\n Supression du min de la file avec 36 éléments\n")
  F3.SupprMin()
  F3.afficheFile()

  print("\n Supression du min de la file avec 35 éléments\n")
  F3.SupprMin()
  F3.afficheFile()

  print("\n Union de la file de 34 éléments et celle de 12 éléments \n")
  F4 = F3.UnionFile(F2)
  F4.afficheFile()"""
