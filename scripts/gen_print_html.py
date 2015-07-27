import os
import re


os.system("rm -rf ../print/html")
os.system("mkdir ../print/html")
for fn in os.listdir('../_posts'):
    if "[" in fn:
        for md in os.listdir('../_posts/'+fn):
            if ".md" in md:
                path = '../_posts/'+fn+"/"+md
                name = re.sub('[0-9]*-[0-9]*-[0-9]*-','',md)
                #path = path.replace("[","\[").replace("]","\]").replace(" ","\ ")
                print name
                print path

                file = open(path,"r")
                r = file.read()
                r = r.replace("layout: article","layout: html")

                fw = open("../print/html/"+name,"w")
                fw.write(r)
                fw.close()






