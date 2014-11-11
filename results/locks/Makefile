
all: ht-locks.png sssp-locks.png minmax-locks.png \
	bp.png nqueens-locks.png

ht-locks.png: ht-reg.txt ht-coord.txt ht-local-only.txt plot_three.py lib.py
	python plot_three.py ht-reg.txt ht-coord.txt ht-local-only.txt ht-locks.png "HT locks" "Local-Only"

sssp-locks.png: sssp.txt sssp-coord.txt plot_three.py lib.py
	python plot_three.py sssp.txt sssp-coord.txt sssp-buffer.txt sssp-locks.png "SSSP locks" "Buffered"

minmax-locks.png: minmax-reg.txt minmax-coord.txt plot.py lib.py
	python plot.py minmax-reg.txt minmax-coord.txt minmax-locks.png "MiniMax locks"

nqueens-locks.png: nqueens-reg.txt nqueens-coord.txt lib.py plot.py
	python plot.py nqueens-reg.txt nqueens-coord.txt nqueens-locks.png "N Queens locks"

bp.png: bp.txt sbp.txt plot.py lib.py
	python plot.py bp.txt sbp.txt bp.png "LBP / SBP"

queue_operations: *.txt
	@python queue_operations.py
