import numpy as np
import math


def SupprMin(Tas):
  if len(Tas) == 0:
    return None
  min_val = Tas[0]
  Tas[0], Tas[-1] = Tas[-1], Tas[0]  # On place le dernier elt en tete
  Tas.pop()  # On supprime le dernier elt
  descendre(
      Tas, 0
  )  # On verifie bien que la structure est bien un Tas depuis la racine sinon on fait les
  # modifications necessaires

  return min_val


def Ajout(Tas, elt):
  Tas.append(elt)
  monter(Tas, len(Tas) - 1)  # On verifie bien que la structure est bien un Tas
  # depuis le dernier elt sinon on fait les
  # modifications necessaires
  return Tas


def monter(Tas, pos):
  pere = (pos - 1) // 2
  if Tas[pere] > Tas[pos]:
    Tas[pere], Tas[pos] = Tas[pos], Tas[pere]

    if pere > 0:  # On continue de monter si pere n'est pas la racine du tas
      monter(Tas, pere)


def AjoutsIteratifs(Tas, data):
  if len(data) == 0:
    return Tas

  for i in range(len(data)):
    Ajout(Tas, data[i])

  return Tas


def descendre(Tas, pos):
  pere = pos
  fils_gauche = 2 * pos + 1
  fils_droit = 2 * (pos + 1)

  noeud = []
  if fils_droit < len(Tas):
    noeud = [Tas[pere], Tas[fils_gauche], Tas[fils_droit]]
  elif fils_gauche >= len(Tas):
    return
  else:
    noeud = [Tas[pere], Tas[fils_gauche]]

  min = 0
  if len(noeud) == 2:
    min = 0 if noeud[0] < noeud[1] else 1
  else:
    if noeud[0] < noeud[1] and noeud[0] < noeud[2]:
      min = 0
    elif noeud[1] < noeud[0] and noeud[1] < noeud[2]:
      min = 1
    elif noeud[2] < noeud[0] and noeud[1] > noeud[2]:
      min = 2

  if (min != 0
      ):  # test que le parent est bien l'elt le plus petit, si diff de 0 alors
    # on doit echanger le pere avec son plus petit fils
    index_min = 2 * pos + min
    Tas[pere], Tas[index_min] = Tas[index_min], Tas[pere]

    if (
        (2 * index_min + 1) < len(Tas)
    ):  # si le fils gauche est inferieur a la taille du tableau, on peut continuer
      descendre(Tas, index_min)


def Construction(liste_cle):
  Tas = liste_cle
  for i in range(len(Tas) // 2, 0,
                 -1):  # On part de la base (n total/ 2**h, avec h=0 à la base)
    # pour remonter sur toute la hauteur du tas
    # Etant donne que les derniers noeuds n'ont pas de fils, on peut passer directement à la racine
    # On equilibre puis on monte ce qui revient à aller à l'element précedent dans le tableau
    # Puis on reapplique la fct d'equilibrage jusqu'a ce que le tas soit bien un tasmin
    descendre(Tas, i - 1)
  return Tas


def Union(Tas1, Tas2):
  if len(Tas1) == 0 and len(Tas2) == 0:
    return None

  if Tas1 == []:
    return Tas2
  if Tas2 == []:
    return Tas1

  for i in Tas2:
    Tas1.append(i)

  Construction(Tas1)
  return Tas1


def height(N):

  return math.log(N + 1) // math.log(2)


# Function to find the leaf
# nodes of binary heap
def findLeafNodes(arr, n):

  # Calculate the height of
  # the complete binary tree
  h = height(n)

  arrlist = []

  for i in range(n - 1, -1, -1):
    if (height(i + 1) == h):
      arrlist.append(arr[i])
    elif (height(i + 1) == h - 1 and n <= ((2 * i) + 1)):

      # if the height if h-1,
      # then there should not
      # be any child nodes
      arrlist.append(arr[i])
    else:
      break

  prLeafNodes(arrlist)


# Function to pr the leaf nodes
def prLeafNodes(arrlist):

  for i in range(len(arrlist) - 1, -1, -1):
    print(arrlist[i], end=" ")


def Print(tab):
  for i in range(0, (len(tab) // 2)):
    if (2 * (i + 1) < len(tab) and (2 * i + 1) < len(tab)):
      print(" PARENT : " + str(tab[i]) + " LEFT CHILD : " +
            str(tab[2 * i + 1]) + " RIGHT CHILD : " + str(tab[2 * (i + 1)]))
    elif (2 * (i + 1)) < len(tab):
      print(" PARENT : " + str(tab[i]) + " LEFT CHILD : " +
            str(tab[2 * i + 1]))
    elif (2 * i + 1) < len(tab):
      print(" PARENT : " + str(tab[i]))
