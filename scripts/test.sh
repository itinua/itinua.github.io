#!/usr/bin/env bash
pandoc --template=my.latex --variable sansfont=Arial --variable fontsize=12pt -V geometry:margin=1in -V mainfont=Georgia -s kak.md --latex-engine=xelatex  -o demo.pdf
#pandoc --template=default.html -s kak.md -o demo.html