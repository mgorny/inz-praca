show: inz.pdf
	xdg-open $<

inz.pdf: inz.ltx inz.toc wstep.tex nomenklatura.tex wykresy/.stamp inz.bib
	bibtexu inz
	xelatex $<

inz.toc: inz.ltx wykresy/.stamp
	xelatex $<

wykresy/.stamp: wykresy/gen.py
	cd wykresy; python gen.py

clean:
	rm -f `cat .gitignore`

inz.pdf: struktura.tex symbole.tex metody-teorii-grafow-przykl.tex
inz.pdf: wstepne.tex ukl-rown.tex ukl-rown-przykl.tex
inz.pdf: elem-skl.tex elem-skl/kociol.tex elem-skl/turbina.tex elem-skl/skraplacz.tex
inz.pdf: elem-skl/pompa.tex
inz.pdf: elem-skl/czynnik.tex elem-skl/paliwo.tex
inz.pdf: test.tex

.PHONY: show
