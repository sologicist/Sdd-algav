import os
import lib.hachage.md5 as md5
import lib.sdd_bigint.abr_bigint as abr
import lib.sdd_bigint.tasmin_binaire_bigint as tasmin
import lib.sdd_bigint.tasmin_tableau_bigint as tasmintab
import lib.sdd_bigint.file_bigint as filee
import lib.utilitaire as ut
import time
import matplotlib.pyplot as plt


def mots_unique():
  directory_path = 'Shakespeare/'
  liste_total = []
  for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    # Check if the entry is a file (not a subdirectory)
    if os.path.isfile(file_path):
      print(f"Processing file: {filename}")
      with open(file_path, 'r') as file:
        for line in file:
          line = line.strip()
          if line not in liste_total:
            liste_total.append(line)

  return liste_total


def collisions(liste_mots):
  map_md5 = {}
  liste_mots_collision = {}
  for mot in liste_mots:
    hach = md5.md5_to_hex(md5.md5(mot.encode('utf-8')))
    if hach in map_md5:
      map_md5[hach] += 1
      liste_mots_collision[hach].append(mot)
    else:
      map_md5[hach] = 1
      liste_mots_collision[hach] = [mot]
  filtered_map = {
      key: value
      for key, value in liste_mots_collision.items() if len(value) > 1
  }

  # Print the result
  return filtered_map


def ABR_shakespeare(liste_mots):
  #print("Construction de l'arbre")
  abr_shakespeare = abr.ABR(
      md5.md5_to_hex(md5.md5(liste_mots[0].encode('utf-8'))))
  for mot in liste_mots[1:]:
    #print("ajout mot")
    abr_shakespeare.insertion(md5.md5_to_hex(md5.md5(mot.encode('utf-8'))))
  return abr_shakespeare


def tasmin_shakespeare_naive(liste_mots):
  tas = tasmin.TasMin()
  liste_hash = []
  for mot in liste_mots:
    liste_hash.append(md5.md5_to_hex(md5.md5(mot.encode('utf-8'))))
  tas.AjoutsIteratifs(liste_hash)
  return tas


def tasmin_shakespeare(liste_mots):
  tas = tasmin.TasMin()
  liste_hash = []
  for mot in liste_mots:
    liste_hash.append(md5.md5_to_hex(md5.md5(mot.encode('utf-8'))))
  tas.Construction(liste_hash)
  return tas


def file_shakespeare(liste_mots):
  file = filee.File()
  liste_hash = []
  for mot in liste_mots:
    liste_hash.append(md5.md5_to_hex(md5.md5(mot.encode('utf-8'))))
  file.Construction(liste_hash)
  return file


def sddVERSUS_Construction():
  uniq = ut.mots_unique_Shakespeare()
  liste = ut.liste_to_hex(uniq)
  print(len(liste))
  perf = []
  x = ['Tasmin Arbre', 'Tasmin Tableau', 'File']

  av1 = []
  for _ in range(5):
    tmp_liste = liste.copy()
    start_time = time.time()
    tas1 = tasmin.TasMin()
    tas1.Construction(tmp_liste)
    end_time = time.time()
    elapsed_time = end_time - start_time
    av1.append(elapsed_time)
  perf.append(sum(av1) / len(av1))

  av2 = []
  for _ in range(5):
    tmp_listec = liste.copy()
    start_time = time.time()
    tas1 = tasmintab.Construction(tmp_listec)
    end_time = time.time()
    elapsed_time = end_time - start_time
    av2.append(elapsed_time)
  perf.append(sum(av2) / len(av2))

  av3 = []
  for _ in range(5):
    tmp_listef = liste.copy()
    start_time = time.time()
    file1 = filee.File()
    file1.Construction(tmp_listef)
    end_time = time.time()
    elapsed_time = end_time - start_time
    av3.append(elapsed_time)
  perf.append(sum(av3) / len(av3))

  fig = plt.figure(figsize=(10, 5))

  # creating the bar plot
  plt.bar(x, perf, color='blue', width=0.4)

  plt.xlabel("Construction des structures de données")
  plt.ylabel("Temps d'éxécutions (s) sur 5 itérations")
  plt.title("Performances des structures de données sur Shakespeare")
  plt.show()


def sddVERSUS_Union():
  uniq = ut.mots_unique_Shakespeare()
  liste = ut.liste_to_hex(uniq)
  mid = len(liste) // 2
  l1 = liste[:mid]
  l2 = liste[mid:]
  print(len(liste))
  perf = []
  x = ['Tasmin Arbre', 'Tasmin Tableau', 'File']

  av1 = []
  for _ in range(5):
    tmp_liste = l1.copy()
    tmp_liste2 = l2.copy()
    tas1 = tasmin.TasMin()
    tas2 = tasmin.TasMin()
    tas1.Construction(tmp_liste)
    tas2.Construction(tmp_liste2)
    start_time = time.time()
    tas1.Union(tas2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    av1.append(elapsed_time)
  perf.append(sum(av1) / len(av1))

  av2 = []
  for _ in range(5):
    tmp_listec = l1.copy()
    tmp_listec2 = l2.copy()
    tas1 = tasmintab.Construction(tmp_listec)
    tas2 = tasmintab.Construction(tmp_listec2)
    start_time = time.time()
    tasmintab.Union(tas1, tas2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    av2.append(elapsed_time)
  perf.append(sum(av2) / len(av2))

  av3 = []
  for _ in range(5):
    tmp_listef = l1.copy()
    tmp_listef2 = l2.copy()

    file1 = filee.File()
    file2 = filee.File()
    file1.Construction(tmp_listef)
    file2.Construction(tmp_listef2)
    start_time = time.time()
    file1.UnionFile(file2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    av3.append(elapsed_time)
  perf.append(sum(av3) / len(av3))

  fig = plt.figure(figsize=(10, 5))

  # creating the bar plot
  plt.bar(x, perf, color='blue', width=0.4)

  plt.xlabel("Union sur les structures de données")
  plt.ylabel("Temps d'éxécutions (s) sur 5 itérations")
  plt.title("Performances des structures de données sur Shakespeare")
  plt.show()


def sddVERSUS_Ajout():
  uniq = ut.mots_unique_Shakespeare()
  liste = ut.liste_to_hex(uniq)
  print(len(liste))
  perf = []
  x = ['Tasmin Arbre', 'Tasmin Tableau', 'File']

  av1 = []
  for _ in range(20):
    tmp_liste = liste.copy()
    tas1 = tasmin.TasMin()
    item = tmp_liste.pop()
    tas1.Construction(tmp_liste)

    start_time = time.time()
    tas1.Ajout(item)
    end_time = time.time()
    elapsed_time = end_time - start_time
    av1.append(elapsed_time)
  perf.append(sum(av1) / len(av1))

  av2 = []
  for _ in range(20):
    tmp_listec = liste.copy()
    item = tmp_listec.pop()
    tas1 = tasmintab.Construction(tmp_listec)

    start_time = time.time()
    tasmintab.Ajout(tas1, item)
    end_time = time.time()
    elapsed_time = end_time - start_time
    av2.append(elapsed_time)
  perf.append(sum(av2) / len(av2))

  av3 = []
  for _ in range(20):
    tmp_listef = liste.copy()
    file1 = filee.File()
    item = tmp_listef.pop()
    file1.Construction(tmp_listef)
    start_time = time.time()
    file1.Ajout(item)
    end_time = time.time()
    elapsed_time = end_time - start_time
    av3.append(elapsed_time)
  perf.append(sum(av3) / len(av3))

  fig = plt.figure(figsize=(10, 5))

  # creating the bar plot
  plt.bar(x, perf, color='blue', width=0.4)

  plt.xlabel("Ajout dans les structures de données")
  plt.ylabel("Temps d'éxécutions (s) sur 20 itérations")
  plt.title("Performances des structures de données sur Shakespeare")
  plt.show()


def sddVERSUS_SupprMin():
  uniq = ut.mots_unique_Shakespeare()
  liste = ut.liste_to_hex(uniq)
  print(len(liste))
  perf = []
  x = ['Tasmin Arbre', 'Tasmin Tableau', 'File']

  av1 = []
  for _ in range(20):
    tmp_liste = liste.copy()
    tas1 = tasmin.TasMin()
    tas1.Construction(tmp_liste)

    start_time = time.time()
    tas1.SupprMin()
    end_time = time.time()
    elapsed_time = end_time - start_time
    av1.append(elapsed_time)
  perf.append(sum(av1) / len(av1))

  av2 = []
  for _ in range(20):
    tmp_listec = liste.copy()
    tas1 = tasmintab.Construction(tmp_listec)

    start_time = time.time()
    tasmintab.SupprMin(tas1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    av2.append(elapsed_time)
  perf.append(sum(av2) / len(av2))

  av3 = []
  for _ in range(20):
    tmp_listef = liste.copy()
    file1 = filee.File()
    file1.Construction(tmp_listef)
    start_time = time.time()
    file1.SupprMin()
    end_time = time.time()
    elapsed_time = end_time - start_time
    av3.append(elapsed_time)
  perf.append(sum(av3) / len(av3))

  fig = plt.figure(figsize=(10, 5))

  # creating the bar plot
  plt.bar(x, perf, color='blue', width=0.4)

  plt.xlabel("SupprMin sur les structures de données")
  plt.ylabel("Temps d'éxécutions (s) sur 20 itérations")
  plt.title("Performances des structures de données sur Shakespeare")
  plt.show()
