
SCRIPT_DIR = $(PWD)
SCRIPT = plot_coord.py

IMGS = min-max-tictactoe.png new-heat-transfer-80.png \
	shortest-uspowergrid.png system_splash-bp-400.png \
	system_belief-propagation-400.png \
	system_improve_belief-propagation-400.png \
	comparison1.png 13queens.png

all: $(IMGS)

min-max-tictactoe.png: minmax.txt plot_coord.py lib.py
	python $(SCRIPT) minmax.txt ""

new-heat-transfer-80.png: ht.txt plot_coord.py lib.py
	python $(SCRIPT_DIR)/plot_ht.py ht.txt

shortest-uspowergrid.png: sssp.txt plot_coord.py lib.py
	python $(SCRIPT) sssp.txt ""

system_improve_belief-propagation-400.png system_belief-propagation-400.png system_splash-bp-400.png: splash-bp.txt lib.py plot_compare_system.py
	python $(SCRIPT_DIR)/plot_compare_system.py splash-bp.txt "system_"

comparison1.png: compare.txt plot_compare.py lib.py
	python $(SCRIPT_DIR)/plot_compare.py compare.txt "" --global-only

13queens.png: nqueens.txt plot_coord.py lib.py
	python $(SCRIPT) nqueens.txt ""

clean:
	rm -f $(IMGS)
