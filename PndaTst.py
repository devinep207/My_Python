from pandas import DataFrame

Boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle']
        }

df = DataFrame(Boxes, columns= ['Color','Shape'])
print (df)
