import lib.sdd_integer.abr as abr
import random


def testABR():
  random_int_list = random.sample(range(1, 25), 10)
  random_int_list.append(random_int_list[0])
  #Racine
  BST = abr.ABR(random_int_list[0])

  #Construction
  BST.construction(random_int_list[1:])
  abr.PrintTree(BST)

  #Recherche
  print("\n")
  print("16 est dans l'arbre : ", BST.recherche(5))
  print("5 est dans l'arbre : ", BST.recherche(5))
  print("10 est dans l'arbre : ", BST.recherche(10))

  print("8000 est dans l'arbre : ", BST.recherche(8000))
  print("1200 est dans l'arbre : ", BST.recherche(1200))
  print("2.5 est dans l'arbre : ", BST.recherche(2.5))
