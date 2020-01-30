#! /usr/bin/env python
# -*- coding:UTF-8 -*-
import sys
import numpy as np
import math
import os

n = 0
sumresall = 0 
for line in sys.stdin:
    line = line.strip().split(",")
    line = np.array(line,float)
    n += line[0]
    sumresall += line[1]

XTX=os.getenv('XTX')
XTX = np.array(XTX.strip().split(","),float)
pplus1 = int(math.sqrt(len(XTX)))
XTX = np.matrix(XTX).reshape(pplus1,pplus1)
sigma_hat = math.sqrt(sumresall/(n-pplus1))
stderr_beta = (sigma_hat*np.sqrt(XTX.I.diagonal())).tolist()[0]

beta_hat=os.environ.get('beta_hat')
beta_hat=np.array(beta_hat.strip().split(","),float)
print("beta_hat: "+",".join(str(i) for i in beta_hat),file=sys.stdout) 
print("sigma_hat: "+str(sigma_hat),file=sys.stdout) 
print("stderr_beta: "+",".join(str(i) for i in stderr_beta),file=sys.stdout) 
