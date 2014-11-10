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

filename = sys.argv[1]

exp = read_experiment(filename)
threads = exp.get_threads()
for ops in exp.queue_instruction_count():
   print ops
