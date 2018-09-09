.PHONY: pdf clean distclean
.DEFAULT_GOAL: pdf

plots := $(patsubst plots/%.py,gfx/%.pgf,$(wildcard plots/*.py))

gfx/%.pgf: plots/%.py
	python $<

pdf: plots
	latexmk -pdf

clean:
	latexmk -c

distclean:
	latexmk -C
	rm gfx/*.pgf

