class Tournoi:

  def __init__(self, cle):
    self.T = [cle]
    self.Deg = 0  #[racine, fils_g,..., fils_d]

  def EstVide(self):
    """ TournoiB −> booleen
    Renvoie vrai ssi le tournoi est vide."""
    return len(self.T) == 0

  def Degre(self):
    """ TournoiB −> entier
    Renvoie le degre de la racine du tournoi ."""
    return self.Deg

  def Union2Tid(self, T2):
    """ TournoiB * TournoiB −> TournoiB
    Renvoie l’union de 2 tournois de meme taille ."""

    if self.Deg != T2.Deg:
      return "Les deux tournois ne sont pas de même taille"
    elif self.Racine() < T2.Racine():
      self.T.append(T2)
      self.Deg += 1
      return self
    else:
      T2.T.append(self)
      T2.Deg += 1
      return T2

  def Racine(self):
    return self.T[0]

  def Decapite(self):  #O(log(N))
    """ TournoiB −> FileB
    Renvoie la file binomiale obtenue en supprimant la racine
    du tournoi T_k −> <T_{k −1} , T_{k −2} , ... ,T_1 ,T_0 >. """
    if self.EstVide() or len(self.T) == 1:
      return None
    F = File()
    for i in range(len(self.T) - 1, 0, -1):
      F.AjoutMin(self.T[i])  #file decroissante
    return F

  def File(self):
    """ TournoiB −> FileB
    Renvoie la file binomiale reduite au tournoi
    T_k −> <T_k >. """
    file = File()
    file.AjoutMin(self)
    return file

  def str(self):
    """Renvoie le degre ainsi que la racine du tournoi"""
    return "(" + str(self.Deg) + "," + str(self.T[0]) + ")"


class File:

  def __init__(self):
    self.LT = []
    self.MinDegreIndex = None if len(self.LT) == 0 else self.LT[-1].Deg
    self.taille = 0

  def EstVide(self):
    """ FileB −> booleen
    Renvoie vrai ssi la file est vide."""
    return len(self.LT) == 0

  def MinDeg(self):
    """ FileB −> TournoiB
    Renvoie le tournoi de degre minimal dans la file."""
    return self.LT[self.MinDegreIndex] if self.MinDegreIndex else None

  def Reste(self):
    """ FileB −> FileB
    Renvoie la file privee de son tournoi de degre minimal ."""
    tk = self.LT.pop(-1)
    self.taille -= (2**tk.Degre())
    return self

  def AjoutMin(self, Tk):
    """ Tournoi * FileB −> FileB
    Hypothese : le tournoi est de degre inferieur au MinDeg de la file
    Renvoie la file obtenue en ajoutant le tournoi comme
    tournoi de degre minimal de la file initiale ."""

    self.LT.append(Tk)
    self.MinDegreIndex = -1
    self.taille += (2**Tk.Degre())
    return self

  def UnionFile(self, F2):
    """ FileB * FileB −> FileB
    Renvoie la file binomiale union des deux files F1 et F2."""

    return self.UFret(F2, None)

  def UFret(self, F2, T):
    """ FileB * FileB * TournoiB −> FileB
    Renvoie la file binomiale union de deux files et d’un tournoi ."""
    if not T or T.EstVide():  #pas de tournoi en retenue

      if not self or self.EstVide():
        return F2
      if not F2 or F2.EstVide():
        return self

      T1 = self.MinDeg()
      T2 = F2.MinDeg()

      if T1 and T2 and T1.Degre() < T2.Degre():
        return self.Reste().UnionFile(F2).AjoutMin(T1)
      if T1 and T2 and T2.Degre() < T1.Degre():
        return self.UnionFile(F2.Reste()).AjoutMin(T2)
      if T1 and T2 and T1.Degre() == T2.Degre():

        return self.Reste().UFret(F2.Reste(), T1.Union2Tid(T2))
    else:  #T tournoi en retenue
      if self.EstVide():
        return T.File().UnionFile(F2)
      if F2.EstVide():
        return self.UnionFile(T.File())
      T1 = self.MinDeg()
      T2 = F2.MinDeg()
      if T1 and T2 and T.Degre() < T1.Degre() and T.Degre() < T2.Degre():
        return self.UnionFile(F2).AjoutMin(T)
      if T1 and T2 and T.Degre() == T1.Degre() and T.Degre() == T2.Degre():
        return self.Reste().UFret(F2.Reste(), T1.Union2Tid(T2)).AjoutMin(T)
      if T1 and T2 and T.Degre() == T1.Degre() and T.Degre() < T2.Degre():
        return self.Reste().UFret(F2, T1.Union2Tid(T))
      if T1 and T2 and T.Degre() == T2.Degre() and T.Degre() < T1.Degre():
        return self.UFret(F2.Reste(), T2.Union2Tid(T))

  def Construction(self, liste):
    """ liste * FileB −> FileB
    Renvoie la file binomiale construction de la liste d’entiers L."""
    for x in liste:  #O(n)
      self.Ajout(x)

  def Ajout(self, x):
    t = Tournoi(x)
    res = self.UnionFile(t.File())
    self.LT = res.LT
    self.MinDegreIndex = res.MinDegreIndex

  def SupprMin(self):  #O(4*log(N)) -> #O(log(n))
    """ FileB −> FileB
    Renvoie la file binomiale en supprimant le tournoi de degre minimal de la file."""
    if self.EstVide():
      return "Rien a supprimé"
    else:
      index = -1
      min = 9999999999999999999999999999999999999999999999
      for i in range(len(
          self.LT)):  #O(log(n)) car il y'a log(n) elts dans la liste
        tk = self.LT[i]
        if tk.T[0] < min:
          min = tk.T[0]
          index = i

      tksup = self.LT.pop(
          index)  #O(log(n)) car il y'a log(n) elts dans la liste

      self.taille -= 1
      r = tksup.Racine()
      F = tksup.Decapite()  #O(log(n))
      if F:
        res = self.UnionFile(F)  #O(log(n))
        self.LT = res.LT
      return r

  def get_taille(self):  #O(log(n))
    self.taille = 0 if len(self.LT) == 0 else sum([(2**t.Degre())
                                                   for t in self.LT])
    return self.taille

  def afficheFile(self):

    print("File" + str(self.get_taille()) + " = ", end=" "),
    for i in range(len(self.LT)):  #O(log(n))
      print(self.LT[i].str(), end=" "),
    print(" ")
