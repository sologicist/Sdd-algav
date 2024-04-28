import lib.sdd_bigint.bigint as bi
import math


class NoeudTasMin:

  def __init__(self, cle):
    """
      Description: Constructeur de la classe NoeudTasMin.
      Paramètres:
          - cle: La clé du nœud, représentée par un objet Cle128Bits.
      """
    # Initialisation de la clé, des enfants, du parent, de la taille, de la hauteur, et de la liste last_node
    if isinstance(cle, bi.Cle128Bits):
      self.cle = cle
    else:
      self.cle = bi.Cle128Bits(cle)
    self.gauche = None
    self.droite = None
    self.parent = None
    self.taille = 1  # Initialise la taille à 1 car il s'agit d'un nouveau nœud
    self.hauteur = 0  # Initialise la hauteur à 0 car il s'agit d'une feuille
    self.last_node = []  # Liste des derniers noeuds ajoutés dans l'arbre

  def majhauteur(self):
    """
    Description: Met à jour la hauteur du nœud en fonction de ses enfants.
    """
    # Si le nœud n'a ni enfant gauche ni enfant droit, sa hauteur est 0
    if not self.gauche and not self.droite:
      self.hauteur = 0
    # Sinon, la hauteur est 1 plus la hauteur maximale de ses enfants
    else:
      self.hauteur = 1 + max(0 if not self.gauche else self.gauche.hauteur,
                             0 if not self.droite else self.droite.hauteur)

  def get_hauteur(self):
    """
    Description: Renvoie la hauteur du nœud basée sur la taille.

    Retourne:
        La hauteur du nœud.
    """
    return int(math.log2(self.taille))

  def majNoeud(self):
    """
    Précondition: La fonction est appelée sur un objet de classe représentant un nœud dans un tas binaire.

    Description: Met à jour le nœud en comparant ses clés avec celles de ses enfants.
    La fonction effectue des échanges si nécessaire, met à jour la taille du nœud en fonction de ses enfants,
    et ajuste les parents des enfants.

    Arguments:
        Aucun argument explicite, mais la fonction utilise self.gauche et self.droite.

    Retourne:
        Aucune valeur de retour explicite.
    """
    # Vérifie si le nœud a un enfant gauche
    if self.gauche:
      # Compare les clés du nœud et de l'enfant gauche, et échange si nécessaire
      if self.gauche.cle.inf(self.cle):
        self.cle, self.gauche.cle = self.gauche.cle, self.cle

      # Met à jour la taille du nœud en fonction de l'enfant gauche
      self.taille = 1 + self.gauche.taille
      # Ajuste le parent de l'enfant gauche
      self.gauche.parent = self

    # Vérifie si le nœud a un enfant droit
    if self.droite:
      # Compare les clés du nœud et de l'enfant droit, et échange si nécessaire
      if self.droite.cle.inf(self.cle):
        self.cle, self.droite.cle = self.droite.cle, self.cle

      # Met à jour la taille du nœud en fonction de l'enfant droit
      self.taille += self.droite.taille
      # Ajuste le parent de l'enfant droit
      self.droite.parent = self


class TasMin:

  def __init__(self):
    """
    Description: Constructeur de la classe TasMin.
    """
    # Initialisation de la racine et de la liste last_node

    self.racine = None
    self.last_node = []
    self.liste_feuille = []

  def AjoutsIteratifs(self, liste):
    """
    Précondition: La fonction est appelée sur un objet de classe représentant un tas binaire.

    Description: Ajoute de manière itérative des éléments à partir d'une liste au tas binaire.
    La fonction utilise la méthode Ajout pour chaque élément de la liste.

    Arguments:
        - liste: Liste des éléments à ajouter au tas.

    Retourne:
        Aucune valeur de retour explicite.
    """
    # Itération sur la liste et ajout itératif au tas
    for i in liste:
      self.Ajout(i)

  def Ajout(self, cle):
    """
    Précondition: La fonction est appelée sur un objet de classe représentant un tas binaire.

    Description: Ajoute un élément avec la clé spécifiée au tas binaire.
    La fonction crée un nouveau nœud avec la clé et l'ajoute à l'arbre en utilisant la fonction récursive Rec_Ajout.

    Arguments:
        - cle: Clé de l'élément à ajouter au tas.

    Retourne:
        Aucune valeur de retour explicite.
    """

    nouveau_noeud = NoeudTasMin(cle)

    # Si la racine est vide, le nouveau nœud est la racine
    if not self.racine:
      self.racine = nouveau_noeud
    else:
      self.Rec_Ajout(self.racine, nouveau_noeud)

  def Rec_Ajout(self, parent, nouveau_noeud):
    """
    Précondition: La fonction est appelée sur un objet de classe représentant un tas binaire.
    Le parent est un nœud existant dans le tas.

    Description: Fonction récursive pour ajouter un nœud dans le tas binaire.
    La fonction explore récursivement l'arbre en cherchant un emplacement pour le nouveau_noeud.

    Arguments:
        - parent: Nœud parent où ajouter le nouveau_noeud.
        - nouveau_noeud: Nœud à ajouter au tas.

    Retourne:
        Aucune valeur de retour explicite.
    """

    if not parent.gauche:
      parent.gauche = nouveau_noeud
      # Met à jour la référence du parent pour le nouveau_noeud
      nouveau_noeud.parent = parent
      # Met à jour le champs parent du nouveau noeud
      self.last_node.append(nouveau_noeud)
    elif not parent.droite:
      parent.droite = nouveau_noeud
      # Met à jour la référence du parent pour le nouveau_noeud
      nouveau_noeud.parent = parent
      # # Met à jour le champs parent du nouveau noeud
      self.last_node.append(nouveau_noeud)
    else:
      # Ajoute le nœud à la branche appropriée
      if parent.gauche.get_hauteur() == parent.droite.get_hauteur():
        # Si les hauteurs des branches gauche et droite sont égales
        if parent.gauche.taille == parent.droite.taille:
          # Si les branches gauche et droite ont la même taille, on continue à explorer la gauche
          self.Rec_Ajout(parent.gauche, nouveau_noeud)
        elif parent.gauche.taille % 2 != 0:
          # Si la taille de la branche gauche est impaire, on continue à explorer la droite
          self.Rec_Ajout(parent.droite, nouveau_noeud)
        else:
          # Sinon, on continue à explorer la gauche
          self.Rec_Ajout(parent.gauche, nouveau_noeud)
      else:
        # Si les hauteurs des branches gauche et droite sont différentes
        if parent.gauche.taille % 2 != 0 and parent.gauche.gauche.taille == parent.gauche.droite.taille:
          # Si la taille de la branche gauche est impaire et ses deux sous-branches ont la même taille, on explore la droite
          self.Rec_Ajout(parent.droite, nouveau_noeud)
        else:
          # Sinon, on explore la gauche
          self.Rec_Ajout(parent.gauche, nouveau_noeud)

    # Réorganise le tas après l'ajout
    parent.majNoeud()

  def last_one(self, node):
    """
    Précondition: La fonction est appelée sur un objet de classe représentant un tas binaire.
    Le nœud 'node' est un nœud existant dans le tas.

    Description: Identifie et ajoute le dernier nœud d'une branche du tas binaire à la liste last_node.
    La fonction explore récursivement l'arbre en suivant des règles spécifiques pour déterminer le dernier nœud.

    Arguments:
        - node: Nœud à partir duquel chercher le dernier nœud de la branche.

    Retourne:
        Aucune valeur de retour explicite.
    """
    if not node:
      return

    # Cas où le nœud a un enfant gauche mais pas de fils droit
    if node.gauche and not node.droite:
      self.last_node.append(node.gauche)
      return

    # Cas où le nœud n'a ni fils gauche ni fils droit
    elif not node.droite and not node.gauche:
      self.last_node.append(node)
      return

    # Cas particulier d'un tas avec 3 éléments
    elif node.droite and node.gauche and node.droite.taille == 1 and node.gauche.taille == 1:
      self.last_node.append(node.droite)
      return

    else:
      # Si les fils ont la même taille, on continue à explorer à droite
      if node.gauche and node.droite and node.gauche.taille == node.droite.taille:
        self.last_one(node.droite)

      # Si la branche gauche est pleine et la droite est vide, on explore la gauche forcément
      elif node.gauche.taille == (2**(node.get_hauteur()) -
                                  1) and node.droite.taille == (
                                      2**(node.get_hauteur() - 1) - 1):
        self.last_one(node.gauche)

      # Si la branche gauche est pleine et la droite n'est pas vide, on explore la droite
      elif node.gauche.taille == (
          2**(node.get_hauteur()) -
          1) and node.droite.taille > (2**(node.get_hauteur() - 1) - 1):
        self.last_one(node.droite)

      # Si la branche droite est vide et la gauche n'est pas encore pleine, on explore la gauche
      elif node.gauche.taille < (2**(node.get_hauteur()) -
                                 1) and node.droite.taille == (
                                     2**(node.get_hauteur() - 1) - 1):
        self.last_one(node.gauche)

  def SupprMin(self):
    """
    Précondition: La fonction SupprMin est appelée sur un objet de classe représentant un tas binaire.

    Description: Supprime l'élément de clé minimale d'un tas binaire et maintient la propriété du tas.

    Arguments:
        Aucun argument explicite, mais la fonction utilise self.racine et self.last_node.

    Retourne:
        La clé de l'élément supprimé, ou None si la racine est nulle.
    """
    # Vérifie si la racine est nulle
    if not self.racine:
      return None

    # Cas où la racine n'a pas d'enfants
    if not self.racine.gauche and not self.racine.droite:
      r = self.racine.cle
      self.racine = None
      return r

    # Vérifie si last_node est vide, si oui, appelle last_one pour le remplir
    if len(self.last_node) == 0:
      self.last_one(self.racine)

    # Initialise tmp avec le dernier élément de last_node
    tmp = self.last_node[-1]

    #Parcours de la brranche
    while tmp.parent != self.racine:
      # Diminue la taille des ancêtres du nœud à supprimer
      tmp.parent.taille -= 1
      tmp = tmp.parent

    # Échange avec le dernier élément
    dernier_noeud = self.last_node[-1]

    # Switch des clés entre la racine et le dernier_noeud
    r = self.racine.cle
    self.racine.cle, dernier_noeud.cle = dernier_noeud.cle, self.racine.cle
    self.last_node.pop()

    # Retirer le dernier nœud (anciennement le nœud de clé minimale)
    if dernier_noeud.parent:
      if dernier_noeud.parent.gauche == dernier_noeud:
        dernier_noeud.parent.gauche = None
      else:
        dernier_noeud.parent.droite = None
    else:
      self.racine = None

    # Fait redescendre le premier élément pour maintenir la propriété du tas
    self.descendre(self.racine)
    return r

  def monter(self, noeud):
    """
    Précondition: La fonction monter est appelée sur un objet de classe représentant un tas binaire.

    Description:
        - La fonction monter fait remonter un nœud dans le tas en échangeant avec son parent jusqu'à ce que la propriété du tas soit rétablie.

    Arguments:
        - noeud: Le nœud à faire remonter dans le tas.

    Retourne:
        Aucun retour explicite dans la fonction, mais elle modifie le tas par référence.

    Note: Le commentaire indique une alternative (commentée) pour la condition d'échange, utilisant l'opérateur de comparaison '<'.
    """
    # Boucle pour faire monter le nœud dans le tas
    while noeud.parent and noeud.cle.inf(noeud.parent.cle):
      # Échange avec le parent si la propriété du tas n'est pas respectée
      noeud.cle, noeud.parent.cle = noeud.parent.cle, noeud.cle
      noeud = noeud.parent

  def descendre(self, noeud):
    """
    Précondition: La fonction descendre est appelée sur un objet de classe représentant un tas binaire.

    Description:
        - La fonction descendre fait descendre un nœud dans le tas en échangeant avec son plus petit enfant jusqu'à ce que la propriété du tas soit rétablie.

    Arguments:
        - noeud: Le nœud à faire descendre dans le tas.

    Retourne:
        Aucun retour explicite dans la fonction, mais elle modifie le tas par référence.

    Note: Le commentaire indique une alternative (commentée) pour les conditions d'échange, utilisant l'opérateur de comparaison '<'.
    """

    # Boucle pour faire descendre le nœud dans le tas
    while True:
      if not noeud:
        break

      gauche = noeud.gauche
      droite = noeud.droite
      plus_petit = noeud

      # Comparaison avec le plus petit enfant
      if gauche and gauche.cle.inf(plus_petit.cle):
        plus_petit = gauche

      if droite and droite.cle.inf(plus_petit.cle):
        plus_petit = droite

      # Échange si nécessaire avec le plus petit enfant
      if plus_petit != noeud:
        noeud.cle, plus_petit.cle = plus_petit.cle, noeud.cle
        noeud = plus_petit
      else:
        break

  def rec_Construction(self, gd=True, parent=None, taille=0):
    """
    Précondition: La fonction rec_Construction est appelée sur un objet de classe représentant un tas binaire.

    Description:
        - La fonction rec_Construction réalise la construction récursive d'un tas binaire à partir d'une liste à construire.
        - Elle utilise la liste self.to_build comme source des éléments à ajouter au tas.
        - La construction suit le schéma de répartition des nœuds déterminé par la fonction calculNoeud.

    Arguments:
        - gd: Un booléen indiquant si le nœud actuel est le fils gauche (True) ou le fils droit (False) du nœud parent.
        - parent: Le nœud parent actuel pour lequel le fils (gauche ou droit) est en cours de construction.
        - taille: La taille totale du sous-arbre en cours de construction.

    Retourne:
        Aucun retour explicite dans la fonction, mais elle modifie le tas par référence.

    Note: La fonction effectue une descente (self.descendre) à la fin de la construction pour s'assurer que la propriété du tas est respectée.
    """
    # Cas de base: arrêt de la construction si la taille est nulle ou la liste à construire est vide
    if taille == 0 or len(self.to_build) == 0:
      return

    # Récupération des informations sur la répartition des nœuds dans le sous-arbre
    res = self.calculNoeud(taille)

    # Cas initial: construction de la racine du tas
    if not parent:
      self.racine = NoeudTasMin(self.to_build.pop())
      self.rec_Construction(True, self.racine, res[1])
      self.rec_Construction(False, self.racine, res[2])
    else:
      # Construction du fils gauche ou droit en fonction de 'gd'
      if gd:
        parent.gauche = NoeudTasMin(self.to_build.pop())
        if res[1] != 0:
          # si le nombre de noeuds à ajouter au fils gauche est différent de 0
          self.rec_Construction(True, parent.gauche, res[1])
        if res[2] != 0:
          # si le nombre de noeuds à ajouter au fils droit est diférent de 0
          self.rec_Construction(False, parent.gauche, res[2])
        parent.taille = 1 + parent.gauche.taille
        parent.gauche.parent = parent
      else:
        parent.droite = NoeudTasMin(self.to_build.pop())
        if res[1] != 0:
          # si le nombre de noeuds à ajouter au fils gauche est différent de 0
          self.rec_Construction(True, parent.droite, res[1])
        if res[2] != 0:
          # si le nombre de noeuds à ajouter au fils droit est diférent de 0
          self.rec_Construction(False, parent.droite, res[2])
        #maj des attributs
        parent.taille += parent.droite.taille
        parent.droite.parent = parent

    # Descendre pour maintenir la propriété du tas
    if not parent:
      return
    self.descendre(parent)

  def Construction(self, liste):
    """
    Précondition: La fonction Construction est appelée sur un objet de classe représentant un tas binaire.

    Description:
        - La fonction Construction initialise la construction d'un tas binaire à partir d'une liste d'éléments.
        - Elle utilise la fonction rec_Construction pour réaliser la construction récursive du tas.

    Arguments:
        - liste: La liste d'éléments à utiliser pour la construction du tas.

    Retourne:
        Aucun retour explicite dans la fonction, mais elle modifie le tas par référence en construisant la racine et ses sous-arbres.
    """
    # Vérification si le tas a déjà une racine (déjà construit)
    if self.racine:
      return

    # Initialisation de la liste à construire et appel de rec_Construction pour démarrer la construction
    self.to_build = liste
    self.rec_Construction(True, None, len(liste))

  def calculNoeud(self, taille):
    """
    Précondition: La fonction calculNoeud est appelée sur un objet de classe représentant un tas binaire.

    Description:
        - La fonction calculNoeud prend en entrée la taille d'une liste d'éléments et retourne une liste d'informations sur la construction d'un nœud du tas.
        - Elle est utilisée pour déterminer comment répartir les éléments lors de la construction récursive du tas.

    Arguments:
        - taille: La taille de la liste d'éléments pour laquelle les informations de construction du nœud sont nécessaires.

    Retourne:
        Une liste contenant trois éléments:
            1. Un entier (1) indiquant que le nœud est en cours de calcul.
            2. La taille de la sous-liste pour le sous-arbre gauche du nœud.
            3. La taille de la sous-liste pour le sous-arbre droit du nœud.
    """
    # Vérification si la taille est nulle
    if taille == 0:
      return

    # Calcul de la hauteur de l'arbre
    h = int(math.log2(taille))

    # Cas où la taille est une puissance de 2 moins 1
    if taille == (2**(h + 1) - 1):
      taille -= 1
      return [1, taille // 2, taille - taille // 2]
    else:
      # Calcul du reste après avoir construit un tas binaire complet
      reste = ((taille + 1) - ((2**h) - 1)) - 1
      liste_g = (taille - reste) // 2
      liste_d = (taille - reste) // 2

      # Répartition du reste entre les sous-arbres gauche et droit
      if reste <= ((2**h) // 2):
        liste_g += reste
      else:
        liste_g += ((2**h) // 2)
        liste_d += reste - ((2**h) // 2)

      return [1, liste_g, liste_d]

  def liste_feuilles(self, noeud):
    if self.racine is None:
      return []
    if not noeud:
      return []

    self.liste_feuille.append(noeud.cle)

    if noeud.gauche:
      self.liste_feuilles(noeud.gauche)

    if noeud.droite:
      self.liste_feuilles(noeud.droite)

    return self.liste_feuille

  def Union(self, tas2):
    """
    Précondition: La fonction Union est appelée sur un objet de classe représentant un tas binaire et prend un autre objet de classe TasMin en tant que paramètre.

    Description:
        - La fonction Union combine deux tas binaires minimaux en fusionnant leurs feuilles respectives dans un nouveau tas binaire minimal.
        - Elle utilise la méthode liste_feuille pour obtenir les listes des feuilles de chaque tas, puis les fusionne pour construire un nouveau tas binaire minimal avec la méthode Construction.

    Arguments:
        - tas2: Un objet de classe TasMin représentant le deuxième tas binaire minimal à fusionner avec le tas actuel.

    Retourne:
        - Un nouvel objet de classe TasMin représentant le résultat de l'union des deux tas binaires minimaux.

    Note: La méthode liste_feuille est utilisée pour obtenir la liste des feuilles de chaque tas, et la méthode Construction est utilisée pour construire un nouveau tas binaire minimal à partir de ces listes combinées.
    """
    # Remise à 0 de liste feuilles
    self.liste_feuille = []
    tas2.liste_feuille = []

    # Obtention des listes de feuilles de chaque tas
    l1 = self.liste_feuilles(self.racine)
    l2 = tas2.liste_feuilles(tas2.racine)

    if l2 == []:
      return self
    if l1 == []:
      return tas2

    # Fusion des listes de feuilles
    for i in l2:
      l1.append(i)

    # Création d'un nouvel objet TasMin et construction du tas binaire minimal résultant
    tasres = TasMin()
    tasres.Construction(l1)
    return tasres

  def afficher_arbre(self, noeud, prefixe="", est_dernier=True):
    """
    Précondition: La fonction afficher_arbre est appelée sur un objet de classe représentant un tas binaire avec un nœud spécifique comme paramètre.

    Description:
        - La fonction afficher_arbre affiche l'arbre associé au tas binaire, à partir d'un nœud spécifié, en utilisant une représentation avec des préfixes.
        - Elle utilise une approche récursive pour parcourir l'arbre, en affichant chaque nœud avec sa clé sous forme de chaîne de caractères.
        - Chaque niveau de l'arbre est décalé avec un préfixe pour indiquer la relation entre les nœuds.

    Arguments:
        - noeud: Le nœud à partir duquel commencer l'affichage de l'arbre.
        - prefixe: La chaîne de caractères représentant le préfixe pour le niveau actuel de l'arbre.
        - est_dernier: Un booléen indiquant si le nœud est le dernier parmi ses frères à ce niveau.

    Retourne:
        - Aucun retour (imprime l'arbre à la console).

    Note: On affiche d'abord la clé puis sur la meme ligne la clé du fil gauche puis sout le fils gauche on affiche le fils droit cle -- gauche
                                                                                                                                       |- droite
    """
    # Vérification si le nœud existe
    if noeud:
      # Affichage du nœud avec sa clé
      print(prefixe + ("└── " if est_dernier else "├── ") +
            str(noeud.cle.toString()))

      # Mise à jour du préfixe pour le prochain niveau
      nouveaux_prefixe = prefixe + ("    " if est_dernier else "│   ")

      # Appels récursifs pour afficher les sous-arbres gauche et droit
      self.afficher_arbre(noeud.gauche, nouveaux_prefixe, not noeud.droite)
      self.afficher_arbre(noeud.droite, nouveaux_prefixe, True)
