show: inz.pdf
	xdg-open $<

inz.pdf: inz.ltx inz.toc wstep.tex nomenklatura.tex wykresy/.stamp inz.bib
	xelatex $<
	bibtexu inz

inz.toc: inz.ltx wykresy/.stamp
	xelatex $<

wykresy/.stamp: wykresy/gen.py
	cd wykresy; python gen.py

clean:
	rm -f `cat .gitignore`

inz.pdf: struktura.tex symbole.tex metody-teorii-grafow-przykl.tex
inz.pdf: wstepne.tex ukl-rown.tex ukl-rown-przykl.tex
inz.pdf: elem-skl.tex elem-skl/kociol.tex elem-skl/turbina.tex elem-skl/skraplacz.tex
inz.pdf: elem-skl/pompa.tex elem-skl/wym-regen.tex elem-skl/odgaz.tex
inz.pdf: elem-skl/czynnik.tex elem-skl/paliwo.tex
inz.pdf: elem-skl/wezel-bilans.tex elem-skl/wezel-rozgalez.tex elem-skl/wezel-miesz-prosty.tex
inz.pdf: test.tex obl.tex
inz.pdf: abstrakt.tex wstep.tex zakonczenie.tex

.PHONY: show
