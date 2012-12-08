show: inz.pdf
	xdg-open $<

inz.pdf: inz.ltx wstep.tex struktura.tex symbole.tex
	xelatex $<

.PHONY: show
