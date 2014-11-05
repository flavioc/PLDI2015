
all: paper.pdf

paper.pdf: paper.tex ack.tex intro.tex \
		language.tex coordination.tex \
		experiments.tex related.tex \
		abstract.tex intro.tex \
		implementation.tex \
		application.tex sssp.tex \
		minimax.tex heat-transfer.tex \
		splash-bp.tex nqueens.tex \
		conclusions.tex
	pdflatex paper.tex
	pdflatex paper.tex
	bibtex paper
	pdflatex paper.tex
	pdflatex paper.tex

clean:
	rm -f *.log *.aux *.out *.bbl *.blg paper.pdf
