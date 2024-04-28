import lib.utilitaire as ut

class Cle128Bits:
  def __init__(self, quadruplet):
      """
      Initialise un objet Cle128Bits à partir d'un quadruplet hexadécimal.

      Arguments:
          - quadruplet (str): Chaîne hexadécimale représentant le quadruplet.

      Description:
          - La fonction prend en entrée un quadruplet hexadécimal sous forme de chaîne.
          - Si la longueur de la chaîne est supérieure à 32 caractères, elle est tronquée pour ne prendre que les 32 caractères significatifs.
          - Le quadruplet est converti en une liste d'entiers représentant les parties hexadécimales de 8 caractères chacune.
      """
      if len(quadruplet) > 32:
          quadruplet = quadruplet.strip()
          quadruplet = quadruplet[2:]

      self.quadruplet = ut.hex_to_list(quadruplet)

  def __repr__(self):
    return f"Cle128Bits({self.quadruplet})"

  def inf(self, quad):
    """
    Compare deux clés Cle128Bits.

    Arguments:
        - quad (Cle128Bits): Clé à comparer avec l'objet Cle128Bits actuel.

    Description:
        - La fonction compare les quadruplets des deux clés.
        - Elle itère sur chaque partie du quadruplet et compare les valeurs.
        - Si une partie de la clé actuelle est plus grande, la fonction renvoie False.
        - Si une partie de la clé actuelle est plus petite, la fonction renvoie True.
        - Si les deux parties sont égales, elle passe à la partie suivante.
        - Si toutes les parties sont égales, la fonction renvoie False.

    Returns:
        bool: True si l'objet Cle128Bits est inférieur à la clé donnée, False sinon.
    """
    for i in range(4):
        if self.quadruplet[i] > quad.quadruplet[i]:
            return False
        elif self.quadruplet[i] < quad.quadruplet[i]:
            return True
        else:
            if i == 3:
                return False
            else:
                continue


  def eq(self, quad):
    """
    Vérifie si deux clés Cle128Bits sont égales.

    Arguments:
        - quad (Cle128Bits): Clé à comparer avec l'objet Cle128Bits actuel.

    Returns:
        bool: True si les deux clés sont égales, False sinon.
    """
    return self.quadruplet == quad.quadruplet

  def sup(self, quad):
    """
    Vérifie si l'objet Cle128Bits est strictement supérieur à une autre clé.

    Arguments:
        - quad (Cle128Bits): Clé à comparer avec l'objet Cle128Bits actuel.

    Returns:
        bool: True si l'objet Cle128Bits est strictement supérieur, False sinon.
    """
    for i in range(4):
        if self.quadruplet[i] < quad.quadruplet[i]:
            return False
        elif self.quadruplet[i] > quad.quadruplet[i]:
            return True
        else:
            if i == 3:
                return False
            else:
                continue


  def toString(self):
    return str(self.quadruplet)

  def toStringSimplified(self):
    return str(self.quadruplet[0])[:4]

  def getquad(self):
    return self.quadruplet
    