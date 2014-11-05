
SCRIPT_DIR = $(HOME)/Projects/meld/scripts/plots
SCRIPT = $(SCRIPT_DIR)/plot_coord.py

IMGS = min-max-tictactoe.png new-heat-transfer-80.png \
	shortest-uspowergrid.png system_splash-bp-400.png \
	system_belief-propagation-400.png \
	system_improve_belief-propagation-400.png

all: $(IMGS)

min-max-tictactoe.png: minmax.txt
	python $(SCRIPT) minmax.txt ""

new-heat-transfer-80.png: ht.txt
	python $(SCRIPT) ht.txt ""

shortest-uspowergrid.png: sssp.txt
	python $(SCRIPT) sssp.txt ""

system_improve_belief-propagation-400.png system_belief-propagation-400.png system_splash-bp-400.png: splash-bp.txt
	python $(SCRIPT_DIR)/plot_compare_system.py splash-bp.txt "system_"

clean:
	rm -f $(IMGS)
