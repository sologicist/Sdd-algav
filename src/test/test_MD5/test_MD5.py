import lib.hachage.md5 as md5


def test_MD5():
  mot = "which"
  # MD5 attendu : 8b7af514f25f1f9456dcd10d2337f753
  print(md5.md5_to_hex(md5.md5(mot.encode('utf-8'))))
