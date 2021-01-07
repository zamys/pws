import pandas
import re

from tkinter import filedialog

path = filedialog.askopenfilename()
f = pandas.read_csv(path, encoding='unicode_escape')
f.head(5)

for i in range(len(f)):
    txt = f.loc[i]["tekst"]
    txt=re.sub(r'@[A-Z0-9a-z_:]+','',txt)#verwijdert gebruikersnaam tag
    txt=re.sub(r'^[RT]+','',txt)#verwijdert RT tekst
    txt = re.sub('https?://[A-Za-z0-9./]+','',txt)#verwijdert URLS
    txt=re.sub("[^a-zA-Z]", " ",txt)#verwijdert hashtags
    f.at[i,"tekst"]=txt

print(f['tekst'][10])