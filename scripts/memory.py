#!/usr/bin/python

#MIT License
#
#Copyright (c) 2020 Jonas Christian Rabe aka Quisl (https://github.com/Quisl)
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os
import time

def __getMemory():
  memlist = []
  for i in os.popen("free").read().split(" "):
    if i != "":
      memlist.append(i)
  memory =  100*float(memlist[7])/float(memlist[6])
  return memory

def __grabCPUdata():
  with open('/proc/stat', 'r') as file:
    firstline = file.readline()
  data = firstline.split(" ")
  data.remove("")
  return int(data[1]),int(data[2]),int(data[3]),int(data[4])


def __getCPU():
  a, b, c, previdle = __grabCPUdata()
  prevtotal = a+b+c+previdle
  time.sleep(0.5)
  a, b, c, idle = __grabCPUdata()
  total = a+b+c+idle
  total = int(total)
  prevtotal = int(prevtotal)
  idle = int(idle)
  cpu = (100*( (total-prevtotal) - (idle-previdle) ) / (total-prevtotal) )
  return cpu


memory = int(__getMemory())
cpu = int(__getCPU())

memcolor = ""
cpucolor = ""
if memory < 30:
  memcolor = "lightgreen"
elif memory < 70:
  memcolor = "yellow"
elif memory < 100:
  memcolor = "pink"

if cpu < 30:
  cpucolor = "lightgreen"
elif cpu < 70:
  cpucolor = "yellow"
elif cpu < 100:
  cpucolor = "pink"
print ("<span foreground='lightblue'>RAM</span> <span foreground='"+memcolor+"'>"+str(memory)+"%</span> <span foreground='lightblue'>CPU</span> <span foreground='"+cpucolor+"'>"+str(cpu)+"%</span>")
