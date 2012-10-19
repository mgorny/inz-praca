show: inz.pdf
	xdg-open $<

inz.pdf: inz.ltx
	xelatex $<

.PHONY: show
