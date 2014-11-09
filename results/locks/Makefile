
all: ht-locks.png sssp-locks.png minmax-locks.png \
	nqueens-bottom-moving.png nqueens-bottom-static.png \
	nqueens-top-moving.png nqueens-top-static.png bp.png

ht-locks.png: ht-reg.txt ht-coord.txt ht-local-only.txt plot_three.py lib.py
	python plot_three.py ht-reg.txt ht-coord.txt ht-local-only.txt ht-locks.png "HT locks" "Local-Only"

sssp-locks.png: sssp.txt sssp-coord.txt plot_three.py lib.py
	python plot_three.py sssp.txt sssp-coord.txt sssp-buffer.txt sssp-locks.png "SSSP locks" "Buffered"

minmax-locks.png: minmax-reg.txt minmax-coord.txt plot.py
	python plot.py minmax-reg.txt minmax-coord.txt minmax-locks.png "MiniMax locks"

nqueens-bottom-moving.png: nqueens-reg.txt nqueens-bottom-moving.txt plot.py
	python plot.py nqueens-reg.txt nqueens-bottom-moving.txt nqueens-bottom-moving.png "N Queens (Bottom Moving)"

nqueens-bottom-static.png: nqueens-reg.txt nqueens-bottom-static.txt plot.py
	python plot.py nqueens-reg.txt nqueens-bottom-static.txt nqueens-bottom-static.png "N Queens (Bottom Static)"

nqueens-top-moving.png: nqueens-reg.txt nqueens-top-moving.txt plot.py
	python plot.py nqueens-reg.txt nqueens-top-moving.txt nqueens-top-moving.png "N Queens (Top Moving)"

nqueens-top-static.png: nqueens-reg.txt nqueens-top-static.txt plot.py
	python plot.py nqueens-reg.txt nqueens-top-static.txt nqueens-top-static.png "N Queens (Top Static)"

bp.png: bp.txt sbp.txt plot.py
	python plot.py bp.txt sbp.txt bp.png "LBP / SBP"
