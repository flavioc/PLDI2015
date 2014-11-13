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
nqueens_static = read_experiment("nqueens-static.txt")

def translate(num):
   if num > 1000000:
      return str(round(num/1000000.0, 1)) + "M"
   elif num > 1000:
      return str(round(num/1000.0, 1)) + "K"
   else:
      return str(num)

def show_instructions0(exp):
   count = exp.queue_instruction_count()
   return translate(count[0]) + " & " + translate(count[1]) + " & " + translate(count[2]) + " & " + translate(count[4]) + " & " + translate(count[8])

def show_instructions(exp, name):
   print name + " & " + show_instructions0(exp) + " \\\\"

def show_facts_per_op(exp, name):
   instrs = exp.queue_instruction_count()
   facts = exp.facts_derived_count()
   count = [round(float(ft)/float(it), 2) for it, ft in zip(instrs, facts)]
   print name + " & " + translate(count[0]) + " & " + translate(count[1]) + " & " + translate(count[2]) + " & " + translate(count[4]) + " & " + translate(count[8]) + " \\\\"

def show_facts_derived0(exp):
   count = exp.facts_derived_count()
   return translate(count[0]) + " & " + translate(count[1]) + " & " + translate(count[2]) + " & " + translate(count[4]) + " & " + translate(count[8])

def show_facts_derived(exp, name):
   print name + " & " + show_facts_derived0(exp) + "\\\\"

def show_separated(exp, name):
   normal = exp.normal_instruction_count()
   prio = exp.heap_instruction_count()
   print name + "& " + translate(normal[0]) + "+" + translate(prio[0]) + " & " + translate(normal[1]) + "+" + translate(prio[1]) + " & " + translate(normal[2]) + "+" + translate(prio[2]) + " & " + translate(normal[4]) + "+" + translate(prio[4]) + " & " + translate(normal[8]) + "+" + translate(prio[8])

def show_instructions_and_facts(exp, name):
   print name + " & " + show_instructions0(exp) + " & " + show_facts_derived0(exp) + " \\\\"

def display_data(fun):
   fun(sssp_reg, "SSSP - Regular")
   fun(sssp_coord, "SSSP - Coordinated")
   fun(sssp_buffered, "SSSP - Buffered")
   print "\hline"

   fun(ht_reg, "HT - Regular")
   fun(ht_coord, "HT - Coordinated")
   fun(ht_local_only, "HT - Local-Only")

   print "\hline"

   fun(lbp, "LBP - Regular")
   fun(sbp, "SBP - Coordinated")

   print "\hline"

   fun(minmax_reg, "MiniMax - Regular")
   fun(minmax_coord, "MiniMax - Coordinated")

   print "\hline"

   fun(nqueens_reg, "N Queens - Regular")
   fun(nqueens_coord, "N Queens - Coordinated")
   fun(nqueens_static, "N Queens - Static")


display_data(show_instructions)
print
print
print
display_data(show_separated)
print
print
print
display_data(show_facts_per_op)
print
print
print
display_data(show_facts_derived)
print
print
print
display_data(show_instructions_and_facts)
