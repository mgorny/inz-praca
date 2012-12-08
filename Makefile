show: inz.pdf
	xdg-open $<

inz.pdf: inz.ltx wstep.tex struktura.tex symbole.tex metody-teorii-grafow-przykl.tex
	xelatex $<

.PHONY: show
