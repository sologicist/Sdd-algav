import lib.sdd_bigint.abr_bigint as abr
import lib.utilitaire as ut


def testABR():
  #échantillon de 10 clés 128 bits
  samples = ut.prog_list_constr(10,10,0)
  print("\nDébut Test ABR\n")
  #Racine
  BST = abr.ABR(samples[0][0])

  #Construction
  BST.construction(samples[0][1:])
  abr.PrintTree(BST)

  #Recherche
  print("\n")
  print("0x6d53011d6d3bf32007e9e3bb25214bae est dans l'arbre : ", BST.recherche("0x6d53011d6d3bf32007e9e3bb25214bae"))
  print("0x23eaa4d91967caa1ec5100f90840ab80 est dans l'arbre : ", BST.recherche("0x23eaa4d91967caa1ec5100f90840ab80"))
  print("0x74dcac53c344762ece6a27308831c29 est dans l'arbre : ", BST.recherche("0x74dcac53c344762ece6a27308831c29"))