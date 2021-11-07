import os, sys, re

# liste = []
dictionaire = {}
def parcours(repertoire) :
    print("Je suis dans "+repertoire)
    liste = os.listdir(repertoire)
    for fichier in liste :
        if os.path.isdir(repertoire+'/'+fichier) :
            print('repo_path '+repertoire+'/'+fichier)
            parcours(repertoire+'/'+fichier)
        if os.path.isfile(repertoire+'/'+fichier) :
            print('file_path '+repertoire+'/'+fichier)
            if fichier.find(".") != -1
                data = fichier.split(".")
                clefNew = '.'+data[1]
            else :
                clefNew = 'pas de suffixe'
            for clef in dictionaire :
                if clef == clefNew :
                    dictionaire[clef]=dictionaire[clef]+1
                    break
            else :
                dictionaire[clefNew]]=1
           

parcours(sys.argv[1])
print(dictionaire)
