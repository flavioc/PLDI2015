#!/usr/bin/python

import re
import sys
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib import rcParams
from numpy import nanmax

reg_file = sys.argv[1]
coord_file = sys.argv[2]
output_file = sys.argv[3]
title = sys.argv[4]

class dataobj(object):
   ATTRS = ['coord_normal_lock', 'coord_priority_lock', 'schedule_next_lock', 'add_priority_lock', 'set_priority_lock', 'set_moving_lock', 'set_static_lock', 'set_affinity_lock']

   def set(self, name, fail, total):
      self.info_fail[name] = fail
      self.info_total[name] = total

   def get_total(self, name):
      return self.info_total[name]

   def get_fail(self, name):
      return self.info_fail[name]

   def total_locks(self):
      return sum(total for name, total in self.info_total.iteritems())

   def total_fail(self):
      return sum(total for name, total in self.info_fail.iteritems())

   def total_coord_locks(self):
      return sum(self.get_total(name) for name in self.ATTRS)

   def fail_coord_locks(self):
      return sum(self.get_fail(name) for name in self.ATTRS)

   def frac_coord_locks(self):
      return (float(self.total_coord_locks()) / float(self.total_locks())) * 100

   def show(self):
      print "THREADS", self.threads
      acc = 0
      for name, total in self.info_total.iteritems():
         print name, self.get_fail(name), "/", total
         acc = acc + total
      print acc

   def __init__(self, th):
      self.threads = th
      self.info_total = {}
      self.info_fail = {}

class experiment(object):

   def add_thread(self, thread, data):
      self.threads[thread] = data

   def get_thread(self, thread):
      return self.threads[thread]

   def num_threads(self):
      return len(self.threads.keys())

   def get_coord_total_locks(self):
      return [data.total_coord_locks() for th, data in sorted(self.threads.iteritems())]

   def get_coord_fail_locks(self):
      return [data.fail_coord_locks() for th, data in sorted(self.threads.iteritems())]

   def get_fail_locks(self):
      return [data.total_fail() for th, data in sorted(self.threads.iteritems())]

   def get_frac_coord_locks(self):
      return [data.frac_coord_locks() for th, data in sorted(self.threads.iteritems())]

   def get_total_locks(self):
      return [data.total_locks() for th, data in sorted(self.threads.iteritems())]

   def get_threads(self):
      return [th for th in sorted(self.threads.keys())]

   def get_lock_fraction(self, other):
      # Compute other.locks / self.locks
      return [(float(other.get_thread(th).total_locks()) / float(data.total_locks())) * 100.0 for th, data in sorted(self.threads.iteritems())]

   def __init__(self):
      self.threads = {}

def read_experiment(filename):
   thread = None
   data = None
   exp = experiment()
   with open(filename, "r") as fp:
      for line in fp:
         line = line.rstrip("\n")
         if line == "":
            continue
         if line.startswith("#"):
            continue
         if line.startswith("THREAD "):
            vec = line.split(" ")
            if data:
               exp.add_thread(thread, data)
            thread = int(vec[1])
            data = dataobj(thread)
            continue
         vec = line.split(":")
         if len(vec) != 2:
            continue
         name = vec[0]
         res = vec[1].lstrip(" ")
         resvec = re.split('\s+', res)
         fail = int(resvec[0])
         total = int(resvec[2])
         data.set(name, fail, total)
   if data:
      exp.add_thread(thread, data)
   return exp

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
ax.set_xticks(ind)
ax.set_xticklabels(('1', '2', '4', '6', '8', '10', '12', '14', '16'))
ax.legend((ptotal, pcoord, pfail, ptotalreg), ('Original Locks', 'Coordination Locks', 'Coordination Locks (Failed)', 'Original Regular Locks'), loc=2)
plt.savefig(output_file)
