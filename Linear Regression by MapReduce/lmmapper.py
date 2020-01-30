#！ /usr/bin/env python
# -*- coding:UTF-8 -*-
import sys
import numpy as np

pplus1 = None
for line in sys.stdin:
    line = line.strip().split(",")
    line.insert(0,1)
    line = np.array(line,float)
    
    if pplus1 == None:
        pplus1 = len(line) - 1
        XY = np.zeros(pplus1) 
        XTX = np.zeros(shape=(pplus1,pplus1))
    
    XY += line[:pplus1] * line[pplus1]
    for i in range(pplus1):
        XTX[i] += line[:pplus1] * line[i]
    
out = XY.tolist() + XTX.reshape(1,pplus1**2)[0].tolist() 
print(",".join(str(i) for i in out),file=sys.stdout)
