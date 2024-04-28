import lib.sdd_bigint.file_bigint as filebi
import lib.utilitaire as ut
import matplotlib.pyplot as plt

import time


def test_construction():
  samples = ut.prog_list_constr(20000, 200000, 0)
  y1 = []
  number = []

  for liste in samples:
    number.append(len(liste))
    print(len(liste))

    av1 = []
    for _ in range(5):
      tmp_liste = liste.copy()
      tmp_liste.reverse()
      start_time = time.time()
      file1 = filebi.File()
      file1.Construction(tmp_liste)
      end_time = time.time()
      elapsed_time = end_time - start_time
      av1.append(elapsed_time)
    y1.append(sum(av1) / len(av1))
  return (y1, number)
  plt.plot(number, y1, label="File Construction")
  plt.xlabel("Nombre d'éléments")
  plt.ylabel("Temps d'exécution (s) sur 5 itérations")
  plt.legend()
  plt.show()


def union_file():
  samples1 = ut.prog_list_constr(20000, 200000, 0)
  samples2 = ut.prog_list_constr(20000, 400000, 200000)
  y1 = []
  number = []

  for i in range(len(samples1)):
    number.append(len(samples1[i]))
    print(len(samples1[i]))
    print(len(samples2[i]))

    av1 = []
    for _ in range(5):
      tmp_liste1 = samples1[i].copy()
      tmp_liste2 = samples2[i].copy()
      tmp_liste1.reverse()
      tmp_liste2.reverse()
      file1 = filebi.File()
      file2 = filebi.File()
      file1.Construction(tmp_liste1)
      file2.Construction(tmp_liste2)
      start_time = time.time()
      file1.UnionFile(file2)
      end_time = time.time()
      elapsed_time = end_time - start_time
      av1.append(elapsed_time)
    y1.append(sum(av1) / len(av1))

  return (y1, number)
  plt.plot(number, y1, label="File Union")
  plt.xlabel("Nombre d'éléments")
  plt.ylabel("Temps d'exécution (s) sur 5 itérations")
  plt.legend()
  plt.show()


def supprmin_file():
  samples = ut.prog_list_constr(20000, 200000, 0)
  y1 = []
  number = []

  for liste in samples:
    number.append(len(liste))
    print(len(liste))

    av1 = []
    for _ in range(5):
      tmp_liste = liste.copy()
      tmp_liste.reverse()
      file1 = filebi.File()
      file1.Construction(tmp_liste)
      start_time = time.time()
      file1.SupprMin()
      end_time = time.time()
      elapsed_time = end_time - start_time
      av1.append(elapsed_time)
    y1.append(sum(av1) / len(av1))

  plt.plot(number, y1, label="File Supprmin")
  plt.xlabel("Nombre d'éléments")
  plt.ylabel("Temps d'exécution (s)")
  plt.legend()
  plt.show()

def compa_constr_union(a1,a2):
  plt.title("Complexité File")
  plt.plot(a1[1],a1[0], label="File Construction")
  plt.plot(a2[1],a2[0], label="File Union")
  plt.xlabel("Nombre d'éléments")
  plt.ylabel("Temps d'exécution (s)")