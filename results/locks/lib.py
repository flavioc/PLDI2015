import re
import math

YAXIS = 200000000

class dataobj(object):
   COORD_ATTRS = ['coord_normal_lock', 'coord_priority_lock', 'schedule_next_lock', 'add_priority_lock', 'set_priority_lock', 'set_moving_lock', 'set_static_lock', 'set_affinity_lock']

   def set(self, name, fail, total):
      self.info_fail[name] = fail
      self.info_total[name] = total

   def set_heap_operations(self, ops):
      self.heap_operations = ops

   def set_normal_operations(self, ops):
      self.normal_operations = ops

   def get_total(self, name):
      return self.info_total[name]

   def get_fail(self, name):
      return self.info_fail[name]

   def total_locks(self):
      return sum(total for name, total in self.info_total.iteritems())

   def total_basic_locks(self):
      return self.total_locks() - self.total_coord_locks()

   def total_fail(self):
      return sum(total for name, total in self.info_fail.iteritems())

   def total_coord_locks(self):
      return sum(self.get_total(name) for name in self.COORD_ATTRS)

   def fail_coord_locks(self):
      return sum(self.get_fail(name) for name in self.COORD_ATTRS)

   def normal_queue_operations(self):
      return self.get_total('normal_lock')

   def priority_queue_operations(self):
      return self.get_total('priority_lock')

   def normal_instruction_count(self):
      return self.normal_operations

   def heap_instruction_count(self):
      return self.heap_operations

   def queue_instruction_count(self):
      return self.normal_operations + self.heap_operations

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
      self.heap_operations = 0
      self.normal_operations = 0

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

   def percent_fail(self):
      return [(float(data.total_fail())/float(data.total_locks())) * 100 for th, data in sorted(self.threads.iteritems())]

   def get_fail_locks(self):
      return [data.total_fail() for th, data in sorted(self.threads.iteritems())]

   def get_frac_coord_locks(self):
      return [data.frac_coord_locks() for th, data in sorted(self.threads.iteritems())]

   def get_total_locks(self):
      return [data.total_locks() for th, data in sorted(self.threads.iteritems())]

   def get_basic_locks(self):
      return [data.total_basic_locks() for th, data in sorted(self.threads.iteritems())]

   def normal_instruction_count(self):
      return [data.normal_instruction_count() for th, data in sorted(self.threads.iteritems())]

   def heap_instruction_count(self):
      return [data.heap_instruction_count() for th, data in sorted(self.threads.iteritems())]

   def queue_instruction_count(self):
      return [data.queue_instruction_count() for th, data in sorted(self.threads.iteritems())]

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
         if len(resvec) == 3:
            fail = int(resvec[0])
            total = int(resvec[2])
            data.set(name, fail, total)
         else:
            total = int(resvec[0])
            if name.startswith("normal_operations"):
               data.set_normal_operations(total)
            else:
               data.set_heap_operations(total)
   if data:
      exp.add_thread(thread, data)
   return exp

