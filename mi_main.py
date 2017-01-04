#!/usr/bin/env python

'''
Showcase for several python functionalities:
- config file
- logfiles
- unittests
- multicore processing (if available)
- package building
- applied to process of gaussian elimination of a tridiagonal matrix
'''

config = configparser.ConfigParser()
config.read( r"C:\Software\python\distrisense\distrisense.ini" )

class gauss_elim:
  def __init__( A = [], a = [], b = [], c = []  ):
    if A.size > 0:
      a = np.diag( A, -1 )
      b = np.diag( A )
      c = np.diag( A, 1 )
    self.N = len(b)
    self.C1[0]   = c[0]/b[0]
    self.C2[0]   = 1/b[0]
    for i in range( 1, N ):
       self.C1[i] = c[i] / ( b[i] - a[i]*C1[i-1] )
       self.C2[i] = a[i] / ( b[i] - a[i]*C1[i-1] )             
  
  def standard( d ):
    #forward pass:
    d_prime[0] = d[0]*C2[0]
    for i, d_elem in enumerate( d[1:] ):
       d_prime[i] = d[i]
    
  def twocores():
    pass


if __name__ == '__main__':
  #simple test case
  N = 512
  a = np.ones( N-1 )
  b = np.ones( N )
  c = np.ones( N-1 )
  A = np.diag( a, -1 ) + np.diag( b ) + np.diag( c, +1 )
  b = np.random.randn( N )
  
  #can use timeit, cProfile, pstats for performance
  x = np.linalg.solve( A, b )
  
