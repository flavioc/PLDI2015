#!/usr/bin/python

import re
import sys
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib import rcParams
from numpy import nanmax
from lib import read_experiment, YAXIS

sssp_reg = read_experiment("sssp.txt")
sssp_coord = read_experiment("sssp-coord.txt")
sssp_buffered = read_experiment("sssp-buffer.txt")
ht_reg = read_experiment("ht-reg.txt")
ht_coord = read_experiment("ht-coord.txt")
ht_local_only = read_experiment("ht-local-only.txt")
lbp = read_experiment("bp.txt")
sbp = read_experiment("sbp.txt")
minmax_reg = read_experiment("minmax-reg.txt")
minmax_coord = read_experiment("minmax-coord.txt")
nqueens_reg = read_experiment("nqueens-reg.txt")
nqueens_coord = read_experiment("nqueens-coord.txt")

def translate(num):
   if num > 1000000:
      return str(num/1000000) + "M"
   elif num > 1000:
      return str(num/1000) + "K"
   else:
      return str(num)

def show(exp, name):
   count = exp.queue_instruction_count()
   print name + " & " + translate(count[0]) + " & " + translate(count[1]) + " & " + translate(count[2]) + " & " + translate(count[4]) + " & " + translate(count[8]) + " \\\\ \hline"

show(sssp_reg, "SSSP - Regular")
show(sssp_coord, "SSSP - Coordinated")
show(sssp_buffered, "SSSP - Buffered")
print "\hline"

show(ht_reg, "HT - Buffered")
show(ht_coord, "HT - Coordinated")
show(ht_local_only, "HT - Local-Only")

print "\hline"

show(lbp, "LBP - Regular")
show(sbp, "SBP - Coordinated")

print "\hline"

show(minmax_reg, "MiniMax - Regular")
show(minmax_coord, "MiniMax - Coordinated")

print "\hline"

show(nqueens_reg, "N Queens - Regular")
show(nqueens_coord, "N Queens - Coordinated")
