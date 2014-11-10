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

if len(sys.argv) != 7:
   print "not enough arguments"
   sys.exit(1)

reg_file = sys.argv[1]
coord_file = sys.argv[2]
opt_file = sys.argv[3]
output_file = sys.argv[4]
title = sys.argv[5]
opt_name = sys.argv[6]

reg_exp = read_experiment(reg_file)
coord_exp = read_experiment(coord_file)
opt_exp = read_experiment(opt_file)

N = reg_exp.num_threads()
ind = np.arange(N)
width = 0.25
cmap = plt.get_cmap('gray')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylabel('Number of Locks')
ax.set_xlabel('Threads')
ax.set_title(title)

pbasicreg = ax.bar(ind, reg_exp.get_basic_locks(), width, color=cmap(0.9), hatch=".")

pbasicc = ax.bar(ind + width, coord_exp.get_basic_locks(), width, color=cmap(0.9), hatch='/')
pcoordc = ax.bar(ind + width, coord_exp.get_coord_total_locks(), width, color=cmap(0.5), bottom=coord_exp.get_basic_locks())

pbasico = ax.bar(ind + 2 * width, opt_exp.get_basic_locks(), width, color=cmap(0.9), hatch='\\')
pcoordo = ax.bar(ind + 2 * width, opt_exp.get_coord_total_locks(), width, color=cmap(0.5), bottom=opt_exp.get_basic_locks())

ax.set_ylim([0, max([max(reg_exp.get_total_locks()), max(coord_exp.get_total_locks())])*1.5])
#ax.set_ylim([0, YAXIS])
ax.set_xticks(ind)
ax.get_yaxis().get_major_formatter().set_scientific(True)
ax.get_yaxis().get_major_formatter().set_powerlimits((-3, 3))
ax.set_xticklabels(('1', '2', '4', '6', '8', '10', '12', '14', '16'))
ax.legend((pbasicreg, pbasicc, pcoordc, pbasico, pcoordo), ('Regular - Basic', 'Coordinated - Basic',
         'Coordinated - Coordination', opt_name + ' - Basic', opt_name + ' - Coordination'), loc=2)
plt.savefig(output_file)
