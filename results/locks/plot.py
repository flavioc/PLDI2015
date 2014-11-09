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

reg_file = sys.argv[1]
coord_file = sys.argv[2]
output_file = sys.argv[3]
title = sys.argv[4]

reg_exp = read_experiment(reg_file)
coord_exp = read_experiment(coord_file)

N = reg_exp.num_threads()
ind = np.arange(N)
width = 0.35
cmap = plt.get_cmap('gray')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylabel('Number of Locks')
ax.set_xlabel('Threads')
ax.set_title(title)
ptotal = ax.bar(ind, coord_exp.get_total_locks(), width, color=cmap(0.9), hatch='/')
pcoord = ax.bar(ind, coord_exp.get_coord_total_locks(), width, color=cmap(0.5))
pfail = ax.bar(ind, coord_exp.get_fail_locks(), width, color=cmap(0.1))
ptotalreg = ax.bar(ind + width, reg_exp.get_total_locks(), width, color=cmap(0.9), hatch=".")
pfailreg = ax.bar(ind + width, reg_exp.get_fail_locks(), width, color=cmap(0.5))
ax.set_ylim([0, max([max(reg_exp.get_total_locks()), max(coord_exp.get_total_locks())])*1.4])
#ax.set_ylim([0, YAXIS])
ax.set_xticks(ind)
ax.set_xticklabels(('1', '2', '4', '6', '8', '10', '12', '14', '16'))
ax.legend((ptotal, pcoord, pfail, ptotalreg), ('Original Locks', 'Coordination Locks', 'Coordination Locks (Failed)', 'Original Regular Locks'), loc=2)
plt.savefig(output_file)
