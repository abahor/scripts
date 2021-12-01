import os

for f,d,i in os.walk(r'C:\Users\Al Lewaa COMPANY\OneDrive\Desktop\hell'):
    for dat in i:
        try:
            de = open(f + '/' + dat, 'w')
            de.close()
            os.remove(f + '/' + dat)
        except:
            pass