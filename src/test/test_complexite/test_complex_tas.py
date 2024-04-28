import lib.sdd_bigint.tasmin_binaire_bigint as tasabr
import lib.sdd_bigint.tasmin_tableau_bigint as tastab
import lib.utilitaire as ut
import matplotlib.pyplot as plt

import time


def test_tas_arbre():
  samples = ut.prog_list_constr(20000, 200000, 0)
  print(len(samples))
  y1 = []
  y2 = []

  number = []
  for liste in samples:
    number.append(len(liste))
    print(len(liste))
    av1 = []
    for _ in range(5):
      tmp_liste = liste
      start_time = time.time()
      tas1 = tasabr.TasMin()
      tas1.AjoutsIteratifs(tmp_liste)
      end_time = time.time()
      elapsed_time = end_time - start_time
      av1.append(elapsed_time)
    y1.append(sum(av1) / len(av1))

    av2 = []
    for _ in range(5):
      tmp_liste = liste
      start_time = time.time()
      tas1 = tasabr.TasMin()
      tas1.Construction(liste)
      end_time = time.time()
      elapsed_time = end_time - start_time
      av2.append(elapsed_time)
    y2.append(sum(av2) / len(av2))

  """fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

  ax1.plot(number, y1, label='complexité')
  ax1.set_title('Ajouts Iteratifs tasmin arbre')
  ax1.set_ylabel('temps (s) sur 5 itérations')
  ax2.plot(number, y2, label='complexité')
  ax2.set_title('Construction tasmin arbre')
  ax2.set_ylabel('temps (s) sur 5 itérations')"""

  plt.title("Complexité tasmin arbre")
  plt.plot(number, y1, label='complexité Ajouts Iteratifs')
  plt.plot(number, y2, label='complexité Construction')
  plt.xlabel("Nombre d'éléments")
  plt.ylabel('temps (s) sur 5 itérations')

  # Adding a legend
  plt.legend()

  # Display the graph
  plt.tight_layout()

  # Show the plots
  plt.show()


def test_tas_tab():
  samples = ut.prog_list_constr(20000, 200000, 0)
  print(len(samples))
  y3 = []
  y4 = []
  number = []
  for liste in samples:
    number.append(len(liste))
    print(len(liste))
    liste.reverse()

    av3 = []
    for _ in range(5):
      tmp_liste = liste
      start_time = time.time()
      tas1 = []
      tas1 = tastab.AjoutsIteratifs(tas1, tmp_liste)
      end_time = time.time()
      elapsed_time = end_time - start_time
      av3.append(elapsed_time)
    y3.append(sum(av3) / len(av3))

    av4 = []
    for _ in range(5):
      tmp_listec = liste
      start_time = time.time()
      tas1 = tastab.Construction(tmp_listec)
      end_time = time.time()
      elapsed_time = end_time - start_time
      av4.append(elapsed_time)
    y4.append(sum(av4) / len(av4))

  fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

  """ax1.plot(number, y3, label='complexité')
  ax1.set_title('Ajouts Iteratifs tasmin tableau')
  ax1.set_ylabel('temps (s) sur 5 itérations')
  ax2.plot(number, y4, label='complexité')
  ax2.set_title('Construction tasmin tableau')
  ax2.set_ylabel('temps (s) sur 5 itérations')"""

  plt.title("Complexité tasmin tableau")
  plt.plot(number, y3, label='complexité Ajouts Iteratifs')
  plt.plot(number, y4, label='complexité Construction')
  plt.xlabel("Nombre d'éléments")
  plt.ylabel('temps (s) sur 5 itérations')
  # Adding a legend
  plt.legend()

  # Display the graph
  plt.tight_layout()

  # Show the plots
  plt.show()


def union_tas():
  samples1 = ut.prog_list_constr(20000, 200000, 0)
  samples2 = ut.prog_list_constr(20000, 400000, 200000)
  y1 = []
  y2 = []
  number = []
  for i in range(len(samples1)):
    print(len(samples1[i]))
    print(len(samples2[i]))
    number.append(len(samples1[i]))

    av1 = []
    for j in range(5):
      tmp_liste1 = samples1[i].copy()
      tmp_liste2 = samples2[i].copy()
      tas1 = tasabr.TasMin()
      tas2 = tasabr.TasMin()
      tas1.Construction(tmp_liste1)
      tas2.Construction(tmp_liste2)
      start_time = time.time()
      tas1.Union(tas2)
      end_time = time.time()
      elapsed_time = end_time - start_time
      av1.append(elapsed_time)
    y1.append(sum(av1) / len(av1))

    av2 = []
    for j in range(5):
      tmp_liste1 = samples1[i].copy()
      tmp_liste2 = samples2[i].copy()
      tmp_liste1.reverse()
      tmp_liste2.reverse()
      tas1 = tastab.Construction(tmp_liste1)
      tas2 = tastab.Construction(tmp_liste2)
      start_time = time.time()
      tastab.Union(tas1, tas2)
      end_time = time.time()
      elapsed_time = end_time - start_time
      av2.append(elapsed_time)
    y2.append(sum(av2) / len(av2))

  """fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

  ax1.plot(number, y1, label='complexité')
  ax1.set_title('Union arbre')
  ax2.plot(number, y2, label='complexité')
  ax2.set_title('Union tableau')"""

  plt.title("Complexité Union")
  plt.plot(number, y1, label='Union arbre')
  plt.plot(number, y2, label='Union tableau')
  plt.xlabel("Nombre d'éléments")
  plt.ylabel('temps (s) sur 5 itérations')

  # Adding a legend
  plt.legend()

  # Display the graph
  plt.tight_layout()

  # Show the plots
  plt.show()


def supprmin_tas():
  samples = ut.prog_list_constr(20000, 240000, 0)
  y1 = []
  y2 = []
  number = []

  for liste in samples:
    print(len(liste))
    number.append(len(liste))
    liste.reverse()

    av1 = []
    for _ in range(5):
      tmp_liste = liste
      tas1 = tasabr.TasMin()
      tas1.Construction(tmp_liste)
      start_time = time.time()
      tas1.SupprMin()
      end_time = time.time()
      elapse_time = end_time - start_time
      av1.append(elapse_time)
    y1.append(sum(av1) / len(av1))

    av2 = []
    for _ in range(5):
      tmp_liste = liste
      tas1 = tastab.Construction(tmp_liste)
      start_time = time.time()
      tastab.SupprMin(tas1)
      end_time = time.time()
      elapse_time = end_time - start_time
      av2.append(elapse_time)
    y2.append(sum(av2) / len(av2))

  """fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

  ax1.plot(number, y1, label='complexité')
  ax1.set_title('Supprmin arbre')
  ax2.plot(number, y2, label='complexité')
  ax2.set_title('Supprmin tableau')"""

  plt.title("Complexité Supprmin")
  plt.plot(number, y1, label='Supprmin arbre')
  plt.plot(number, y2, label='Supprmin tableau')
  plt.xlabel("Nombre d'éléments")
  plt.ylabel('temps (s) sur 5 itérations')

  # Adding a legend
  plt.legend()

  # Display the graph
  plt.tight_layout()

  # Show the plots
  plt.show()
