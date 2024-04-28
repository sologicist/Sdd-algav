import lib.sdd_bigint.file_bigint as filebi
import lib.utilitaire as ut


def testFile():
  print("\n Test File\n")
  
  print("\n Construction de la file avec 36 clés\n")
  #random_int_list = random.sample(range(1, 120), 36)
  samples = ut.prog_list_constr(36,36,0)
  F = filebi.File()
  F.Construction(samples[0])
  F.afficheFile()

  print("\n Suppression de tous les éléments de la file\n")
  for _ in range(37):
    F.SupprMin()
  F.afficheFile()

  print("\n Union de deux files de 36 clés\n")
  samples1 = ut.prog_list_constr(36,36,0)
  samples2 = ut.prog_list_constr(36,36,0)
  F1 = filebi.File()
  F2 = filebi.File()
  F1.Construction(samples1[0])
  F2.Construction(samples2[0])
  F1.UnionFile(F2).afficheFile()