#!/usr/bin/python

import sys
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib import rcParams
from numpy import nanmax
from lib import name2title, experiment_set, experiment, coordinated_program

if len(sys.argv) != 2:
  print "Usage: plot_queens.py <filename>"
  sys.exit(1)

filename = sys.argv[1]
max_threads = 16

# read data.
expset = experiment_set()
with open(filename, "r") as fp:
   for line in fp:
      line = line.rstrip("\n")
      if line == "":
         continue
      if line.startswith("#"):
         continue
      vec = line.split(" ")
      if len(vec) < 3:
         continue
      name = vec[0]
      threads = int(vec[1][2:])
      time = int(vec[len(vec)-1])
      expset.add_experiment(name, threads, time)

reg = expset.get_experiment('8queens-13')
coord0 = expset.get_experiment('8queens-13-coord0')
coord1 = expset.get_experiment('8queens-13-coord1')
reg.create_ht(coord0, coord1, "Static")
