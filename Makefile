.PHONY: pdf clean distclean
.DEFAULT_GOAL: pdf

plots := $(patsubst plots/%.py,gfx/%.pgf,$(wildcard plots/*.py))
tables := $(patsubst scripts/%.py,tables/%.tex,$(wildcard scripts/*.py))

gfx/%.pgf: plots/%.py
	python $<

tables/%.tex: scripts/%.py
	python $<

pdf: $(plots) $(tables)
	latexmk thesis -pdf

clean:
	latexmk -c

distclean:
	latexmk -C
	rm gfx/*.pgf
	rm tables/*.tex

