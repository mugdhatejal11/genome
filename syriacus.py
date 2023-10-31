#

import re
from xml.dom import minidom
import json

#f = open("hibiscus_syriacus.txt", "r")

#syriacus = f.read()

AA = {"Arginine": "R", "Histidine": "H", "Lysine": "K", "Aspartic Acid": "D", 
      "Glutamic Acid": "E", "Serine": "S", "Threomine": "T", "Asparagine": "N", 
      "Glutamine": "Q", "Cysteine": "C", "Glycine": "G", "Proline": "P", 
      "Alanine": "A", "Valine": "V", "Isoleucine": "I", "Leucine": "L", 
      "Methionine": "M", "Phenylalamine": "F", "Tyrosene": "Y", "Trypphan": "W"}



file = minidom.parse("sequence_syriacus.xml")

#protein_id = re.search(r'[A-Z]+[0-9]+.[0.9]', syriacus)

protein = file.getElementsByTagName("Textseq-id_accession")
#protein_id = protein[0].firstChild.nodeValue

protein_list = []
for p in protein:
    key = p.firstChild.nodeValue
    protein_list.append(key)
    
    
translation = file.getElementsByTagName("NCBIeaa")
#translation[0].firstChild.nodeValue

translation_list = []
for t in translation:
    value = t.firstChild.nodeValue
    translation_list.append(value)
    
pt = dict(zip(protein_list, translation_list))

with open('catalog.txt', 'w') as file:
    file.write(json.dumps(pt))
    
    

#polypeptides = []

#for k, v in AA.items():
#    polypeptides.append(v)
    
#flag = False
    
#pattern = re.search(r'/translation="(.*)"\n     gene')

#for polypeptide in polypeptides:
#    if polypeptide in pattern:
#        flag = True
        
#if flag is True: translation = pattern    