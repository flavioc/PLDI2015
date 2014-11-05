
SCRIPT = $(HOME)/Projects/meld/scripts/plots/plot_coord.py

IMGS = min-max-tictactoe.png new-heat-transfer-80.png \
	shortest-uspowergrid.png

all: $(IMGS)

min-max-tictactoe.png: minmax.txt
	python $(SCRIPT) minmax.txt ""

new-heat-transfer-80.png: ht.txt
	python $(SCRIPT) ht.txt ""

shortest-uspowergrid.png: sssp.txt
	python $(SCRIPT) sssp.txt ""

clean:
	rm -f $(IMGS)
