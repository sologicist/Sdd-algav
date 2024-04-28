import math

# Liste des quantités de rotation pour chaque itération dans le calcul du hash MD5.
nb_rotations = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 5, 9, 14, 20,
    5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 4, 11, 16, 23, 4, 11, 16, 23, 4,
    11, 16, 23, 4, 11, 16, 23, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6,
    10, 15, 21
]

# Liste de constantes générées à partir de la fonction sinus pour chaque itération.
constantes = [
    int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)
]

# Valeurs initiales pour le calcul du hash MD5
val_initiales = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

# Fonctions de compression utilisées dans chaque itération.
# Les 16 premières fonctions lambda de la liste effectuent l'opération : (b & c) | (~b & d)
# Les 16 suivantes effectuent l'opération : (d & b) | (~d & c)
# Les 16 suivantes effectuent l'opération b ^ c ^ d
# Les 16 dernieres fonctions effectuent l'opération c ^ (b | ~d)
fonctions_bitwise = 16 * [lambda b, c, d: (b & c) | (~b & d)] + 16 * [
    lambda b, c, d: (d & b) | (~d & c)
] + 16 * [lambda b, c, d: b ^ c ^ d] + 16 * [lambda b, c, d: c ^ (b | ~d)]

# Fonctions qui déterminent l'index pour chaque itération.
# Les 16 premières fonctions sont définies comme lambda i: i
# Les 16 suivantes sont définies comme lambda i: (5*i + 1) % 16
# Les 16 suivantes sont définies comme lambda i: (3*i + 5) % 16
# Les 16 dernières sont définies comme lambda i: (7*i) % 16
index_fonctions_bitwise = 16 * [lambda i: i] + 16 * [
    lambda i: (5 * i + 1) % 16
] + 16 * [lambda i: (3 * i + 5) % 16] + 16 * [lambda i: (7 * i) % 16]


def decalage_g(x, val_dec):
  # Fonction pour effectuer une rotation vers la gauche sur un entier 32 bits.
  x &= 0xFFFFFFFF
  return ((x << val_dec) | (x >> (32 - val_dec))) & 0xFFFFFFFF


def md5(message):

  message = bytearray(
      message)  # Convertit le message d'entrée en un tableau d'octets
  taille = (
      8 * len(message)
  )  #  Calcule la longueur du message en bits et stocke le résultat dans orig_len_in_bits en s'assurant que ça ne dépasse pas 64 bits
  message.append(0x80)  # Ajouter le bit "1" au message
  while len(
      message
  ) % 64 != 56:  # Ajouter le bit "0" jusqu'à ce que la taille du message en bits soit égale à 448
    message.append(0)
  message += taille.to_bytes(
      8, byteorder='little'
  )  # Ajouter la taille du message initial(avant le padding) codée en 64-bit little-endian au message
  # on garde le message en octets par simplicité
  res_hash = val_initiales[:]

  for bloc in range(
      0, len(message),
      64):  # Pour chaque bloc de 512 bits du message, soit 64 octets
    a, b, c, d = res_hash  # On récupere h0, h1, h2, h3
    buffer = message[bloc:bloc +
                     64]  # On récupère le bloc de 64 bits du message
    for i in range(64):
      f = fonctions_bitwise[i](b, c, d)
      g = index_fonctions_bitwise[i](i)
      #var entier temp := d
      #d := c
      #c := b
      #b := leftrotate((a + f + k[i] + w[g]), r[i]) + b
      #a := temp
      to_rotate = a + f + constantes[i] + int.from_bytes(
          buffer[4 * g:4 * g + 4], byteorder='little'
      )  # On récupere une portion de 32 bits du message, soit 4 octets, et on transforme ces octets en entier en utilisant la fonction int.from_bytes, on a 64 elts dans W au ieu de 16 comme dans le pseudo code Wikipedia
      new_b = (
          b + decalage_g(to_rotate, nb_rotations[i])
      ) & 0xFFFFFFFF  # decalage gauche ((a + f + k[i] + w[g]), r[i]) + b et on s'assure q'uil ne dépasse pas 32bits
      a, b, c, d = d, new_b, b, c
    for i, val in enumerate([a, b, c, d]):
      # Ajoute les valeurs mises à jour des hachés (a, b, c, d) aux parties correspondantes des hachés actuels (res_hash). Chaque addition est suivie d'un masquage avec 0xFFFFFFFF pour s'assurer que les valeurs restent sur 32 bits.
      #h0 := h0 + a
      #h1 := h1 + b
      #h2 := h2 + c
      #h3 := h3 + d
      res_hash[i] += val
      res_hash[i] &= 0xFFFFFFFF
  #h0 concaténer h1 concaténer h2 concaténer h3 en LITTLE-ENDIAN 
  # On crée un 128 bits donc on décale chaque de 32*i vers la gauche
  return sum(x << (32 * i) for i, x in enumerate(res_hash))


#Fonction pour convertir le message haché en hexadécimal
def md5_to_hex(digest):
  raw = digest.to_bytes(16, byteorder='little')
  return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))
