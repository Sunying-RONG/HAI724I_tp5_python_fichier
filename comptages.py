import os, sys, re

# parameter finish by /
# liste = []
dictionaire = {}
def parcours(repertoire) :
    print("Je suis dans "+repertoire)
    liste = os.listdir(repertoire)
    for fichier in liste :
        if os.path.isdir(repertoire+fichier) :
            parcours(repertoire+fichier+'/')
        if os.path.isfile(repertoire+fichier) and (not fichier.startswith('.')) :
            if '.' in fichier :
                data = fichier.split(".")
                clefNew = '.'+data[1]
            else :
                clefNew = 'pas de suffixe'
            for clef in dictionaire :
                if clef == clefNew :
                    dictionaire[clef]=dictionaire[clef]+1
                    break
            else :
                dictionaire[clefNew]=1
           
parcours(sys.argv[1])
if 'pas de suffixe' in dictionaire :
    dictionaire['pas de suffixe']=dictionaire.pop('pas de suffixe')
    
for (key, value) in dictionaire.items() :
    print(key, ":", value)
print('TOTAL', ':', len(dictionaire.keys()))