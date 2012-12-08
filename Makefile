show: inz.pdf
	xdg-open $<

inz.pdf: inz.ltx wstep.tex
	xelatex $<

inz.pdf: struktura.tex symbole.tex metody-teorii-grafow-przykl.tex
inz.pdf: elem-skl.tex
inz.pdf: program.tex
inz.pdf: test.tex

.PHONY: show
