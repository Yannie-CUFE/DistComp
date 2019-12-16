#! /usr/bin/env python
# -*- coding:UTF-8 -*-
import sys
import os
import numpy as np

beta_hat=os.getenv('beta_hat')
beta_hat=np.array(beta_hat.strip().split(","),float)
sumres = 0 
pplus1 = len(beta_hat) 

i = 0
for line in sys.stdin:
    i += 1
    line = line.strip().split(",")
    line.insert(0,1) 
    line = np.array(line,float)
    sumres += (sum(line[:pplus1]*beta_hat)-line[pplus1])**2 
    
out = [i,sumres]
    
print(",".join(str(i) for i in out),file=sys.stdout) 
