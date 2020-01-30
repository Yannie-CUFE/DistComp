import sys
import numpy as np
import math

length = None 
for line in sys.stdin:
    line = line.strip().split(",")
    line = np.array(line,float)
    if length == None: 
        length = len(line)
        XY_XTX = np.zeros(length)
    XY_XTX += line 

pplus1 = int((-1+math.sqrt(1+4.0*length))/2.0) 
XY = np.matrix(XY_XTX[:pplus1]).T 
print(",".join(str(i) for i in XY_XTX[pplus1:]),file=sys.stdout)
XTX = np.matrix(XY_XTX[pplus1:]).reshape(pplus1,pplus1) 
beta_hat = (XTX.I*XY).reshape(1,pplus1).tolist()[0]
print(",".join(str(i) for i in beta_hat),file=sys.stdout) 
