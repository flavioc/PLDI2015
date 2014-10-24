
all: paper.pdf

paper.pdf: paper.tex ack.tex intro.tex \
		language.tex coordination.tex \
		experiments.tex related.tex \
		abstract.tex intro.tex
	pdflatex paper.tex
	pdflatex paper.tex
	bibtex paper
	pdflatex paper.tex
	pdflatex paper.tex

clean:
	rm -f *.log *.aux *.out *.pdf *.bbl *.blg
