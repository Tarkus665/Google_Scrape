# Simple Python 3 program for .wav soundscape generation. (C) P.B.L. Meijer 2015
# Direct port of the arti1.c C program

FNAME = 'arti1.wav'
N     =    64   # Resolution, i.e., # rows and columns  
FL    =   500   # Lowest  frequency (Hz) in visual sound
FH    =  5000   # Highest frequency (Hz)                
FS    = 20000   # Sample  frequency (Hz)                
T     =  1.05   # Image to sound conversion time (s)    
D     =     1   # Linear|Exponential=0|1 distribution   

# Coefficients used in rnd()
ir = 0
ia = 9301
ic = 49297
im = 233280

import struct, math

TwoPi = 6.283185307179586476925287
WHITE = 1.00
DGREY = 0.25
BLACK = 0.00

def wi(fp,i):
   b0 = int(i%256)
   b1 = int((i-b0)/256)
   fp.write(struct.pack('B',b0 & 0xff))
   fp.write(struct.pack('B',b1 & 0xff))

def wl(fp,l):
   i0 = l%65536
   i1 = (l-i0)/65536
   wi(fp,i0)
   wi(fp,i1)

def rnd():
   global ir, ia, ic, im
   ir = (ir*ia+ic) % im
   return ir / (1.0*im)

def main():
   b     = 0
   d     = D
   ns    = int(FS * T)
   m     = int(ns / N)
   k     = 0
   scale = 0.5/math.sqrt(N)
   dt    = 1.0 / FS

   w    = [0 for i in range(N)]
   phi0 = [0 for i in range(N)]
   A    = [[0 for j in range(N)] for i in range(N)]
   
   # Set hard-coded image: diagonal, filled rectangle, 3 horizontal lines 
   for j in range(0, N):
      for i in range(0, N): A[i][j] = WHITE if i == j else BLACK
   for j in range(39,60):
      for i in range(9,27): A[i][j] = DGREY if j < 47 else WHITE
   for j in range( 4, 8): A[40][j] = WHITE
   for j in range( 8,12): A[31][j] = WHITE
   for j in range(12,16): A[40][j] = WHITE

   # Set lin|exp (0|1) frequency distribution and random initial phase 
   if (d): 
      for i in range(0,N): w[i] = TwoPi * FL * pow(1.0* FH/FL,1.0*i/(N-1))
   else: 
      for i in range(0,N): w[i] = TwoPi * FL + TwoPi * (FH-FL)   *i/(N-1)
   for i in range(0,N): phi0[i] = TwoPi * rnd()

   # Write 8-bit .wav visual sound file, using rectangular time window 
   fp = open(FNAME,'wb')
   fp.write(bytes('RIFF','UTF-8')); wl(fp,ns+36); 
   fp.write(bytes('WAVEfmt ','UTF-8')); wl(fp,16)
   wi(fp,1); wi(fp,1); wl(fp,FS); wl(fp,FS); wi(fp,1); wi(fp,8);
   fp.write(bytes('data','UTF-8')); wl(fp,ns)
   tau1 = 0.5 / w[N-1]; tau2 = 0.25 * (tau1*tau1); y = z = 0.0

   # Not optimized for speed (or anything else) 
   while (k < ns):
      s = 0.0; t = k * dt; j = int(k / m); 
      if j > N-1: j = N-1
      for i in range(0,N,1): s += A[i][j] * math.sin(w[i] * t + phi0[i])
      if k < ns / (5 * N): s = (2.0 * rnd() - 1.0) / scale  # "click" 
      yp = y; y = tau1/dt + tau2/(dt*dt)
      y  = (s + y * yp + tau2/dt * z) / (1.0 + y); z = (y - yp) / dt
      b  = 128 + int(scale * 128 * y)  # y = 2nd order filtered s 
      if b > 255: b = 255
      if b <   0: b =   0
      fp.write(struct.pack('B',b & 0xff))
      k += 1

   if ((math.ceil(ns/2)) != (ns/2)): fp.write(struct.pack('B',0))
   fp.close()
   return 0

main()
