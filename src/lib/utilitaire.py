import os
import random
import lib.hachage.md5 as md5


def hex_to_list(input_string):
  """
  Convertit une chaîne hexadécimale en une liste d'entiers.

  Arguments:
      - input_string (str): Chaîne hexadécimale à convertir.

  Returns:
      list: Une liste de quatre entiers, chacun représentant une partie de huit caractères de la chaîne d'entrée.
  """
  # Définir la taille de chaque partie
  part_size = 8

  # Extraire chaque 8 caracteres à partir de l'input string et la convertir
  parts = [
      int(input_string[i * part_size:(i + 1) * part_size], base=16)
      for i in range(4)
  ]

  return parts


def build_total_list():
  """
  Renvoie la totalité des clés d'un répertoire sous la forme d'une liste de strings

  Arguments:
      - None

  Returns:
      list: Une liste de clés d'un répertoire
  """
  directory_path = 'cles_alea/'
  liste_total = []
  # Loop through each file in the directory
  for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    # Check if the entry is a file (not a subdirectory)
    if os.path.isfile(file_path):
      #print(f"Processing file: {filename}")
      with open(file_path, 'r') as file:
        for line in file:
          line = line.strip()
          liste_total.append(line)
  return liste_total


"""def flatten_to_list_of_lists(input_list, sublist_length):
  return [
      input_list[i:i + sublist_length]
      for i in range(0, len(input_list), sublist_length)
  ]


def list_lists_constr(pas):
  return flatten_to_list_of_lists(build_total_list(), pas)"""


def prog_list_constr(pas, limite, depart):
  """
  Renvoie une liste de listes de longueur croissante à partir d'un indice de départ avec une croissance d'un certain pas vers une limite d'éléments 

  Arguments:
      - pas (int): Croissance des listes
      - limite (int): Nombre d'éléments maximum dans la dernière liste
      - depart (int): Indice de départ du prélèvement
  """
  series_de_listes = []
  liste_depart = build_total_list()[:limite]
  index_depart = depart
  tmp = pas
  while index_depart + pas <= len(liste_depart):
    series_de_listes.append(liste_depart[index_depart:index_depart + pas])
    pas += tmp
  return series_de_listes


def generate_sorted_keys(nb):
  """
  Génère et enregistre des clés hexadécimales triées dans un fichier texte.

  Arguments:
      - nb (int): Nombre maximum de clés à générer.

  Description:
      - La fonction génère des clés hexadécimales triées de 0 à nb-1.
      - Les clés sont enregistrées dans le fichier "keys_sorted.txt".

  Returns: 
      - Ecrit dans le fichier "keys_sorted.txt" ne retourne rien.
"""
  with open("keys_sorted.txt", "w") as f:
    keys = []
    for i in range(2**128):
      if i > nb:
        break
      key = f"{i:032x}"
      keys.append(key)
      f.write(key + "\n")


def mots_unique_Shakespeare():
  """
  Renvoie 
  """
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


def liste_to_hex(liste):
  res = []
  for e in liste:
    res.append(md5.md5_to_hex(md5.md5(e.encode('utf-8'))))
  return res


def mots_Shakespeare():
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
          liste_total.append(line)

  return liste_total
