import os
import re
os.system("rm -rf ../print/pdf")
os.system("mkdir ../print/pdf")
for fn in os.listdir('../_posts'):
    if "[" in fn:
        for md in os.listdir('../_posts/'+fn):
            if ".md" in md:
                path = '../_posts/'+fn+"/"+md
                name = re.sub('[0-9]*-[0-9]*-[0-9]*-','',md)
                name = name.replace(".md",".pdf")
                path = path.replace("[","\[").replace("]","\]").replace(" ","\ ")
                print path
                os.system("pandoc --template=my.latex --variable sansfont=Arial --variable fontsize=12pt -V geometry:margin=1in -V mainfont=Georgia  -s "+path+" --latex-engine=xelatex  -o ../print/pdf/"+name)





