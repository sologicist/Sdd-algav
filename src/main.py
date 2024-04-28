import lib.utilitaire as ut
import json
import random
import lib.hachage.md5 as md5
import test.test_sdd_integer.test_tasmin as testTas
import test.test_sdd_integer.test_tasmin_tableau as testTastab

import test.test_experimentation.test_Shakespeare as shake
import test.test_sdd_integer.test_ABR as testABR
import test.test_sdd_integer.test_File as testFile
import lib.sdd_bigint.abr_bigint as abr
import lib.sdd_integer.tasmin_binaire as tas

import test.test_complexite.test_complex_tas as tsc
import test.test_complexite.test_complex_file as tsf

import matplotlib.pyplot as plt
import lib.utilitaire as ut

import test.test_sdd_bigint.test_ABR_bigint as testABR_bigint
import test.test_sdd_bigint.test_file_bigint as testFile_bigint
import test.test_sdd_bigint.test_tasmin_bigint as testTasmin_bigint
import test.test_sdd_bigint.test_tasmin_tableau_bigint as testT_bigint
import lib.sdd_bigint.bigint as bi  #Importer les fichiers nécessaire

#print(tasmin.calculNoeud(5))
#testFile.testFile()
#testABR.testABR()
#testTas.testTasmin()
#testTastab.testTasmin_tab()

#shake_abr = shake.ABR_shakespeare(ut.mots_Shakespeare())
#print(shake.collisions(ut.mots_unique_Shakespeare()))

#abr.PrintTree(shake_abr)

#tsc.test_tas_arbre()
#tsc.test_tas_tab()
#tsc.supprmin_tas()
#tsc.union_tas()
#tsc.supprmin_tas()
#tsf.test_construction()
#tsf.union_file()
#tsf.supprmin_file()

#mot = "ALGAV"
#print(md5.md5_to_hex(md5.md5(mot.encode('utf-8'))))

#shake.sddVERSUS_Construction()
#shake.sddVERSUS_Union()
#shake.sddVERSUS_Ajout()
#shake.sddVERSUS_SupprMin()

testABR_bigint.testABR()
#testFile_bigint.testFile()
#testTasmin_bigint.testTasmin()
#testT_bigint.testTasmin()

#Création des entiers 128Bits
#grand_entier1 = bi.Cle128Bits("0xdf6943ba6d51464f6b02157933bdd9ad")
#grand_entier2 = bi.Cle128Bits("d192acf4c06fe7c7df042f07d290bdd4")
#print(grand_entier1.toString())
#print(grand_entier2.toString())


print("\nFin des tests")
