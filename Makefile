#!/usr/bin/make -f

DEBUG_FLAG ?=
PYTHON3 ?= python3.4

all: demo
	@echo
	@echo "You now have all of these PDFs:"
	@ls *pdf
	@echo "If you don't want them anymore, run 'make clean'."
	@echo

check: test_1_arg.pdf test_2_arg.pdf

clean:
	rm -f *.aux *.log *.pdf *.tex

demo: populate_from_tsv.py populate.py template.tex.in students.tsv
	$(PYTHON3) populate_from_tsv.py $(DEBUG_FLAG) template.tex.in students.tsv

%.pdf: %.tex
	pdflatex $$(basename $@ .pdf)
	pdflatex $$(basename $@ .pdf)
	pdflatex $$(basename $@ .pdf)

test_1_arg.tex: populate.py template.tex.in
	rm -f _$@
	$(PYTHON3) populate.py template.tex.in _$@ 42
	mv _$@ $@

test_2_arg.tex: populate.py template.tex.in
	rm -f _$@
	$(PYTHON3) populate.py template.tex.in _$@ 84 99
	mv _$@ $@
