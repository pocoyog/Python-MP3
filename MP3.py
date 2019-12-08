import numpy as np

print('   Machine Problem 3 (Python): ')
print('Input should be in "n x 2" matrix form')
print('You should input your variable as:')
print('                                  "Matrixx = np.array([[n,m],[n,m]])"')
print('                                  "where: n & m are the values of the corresponding matrix"')
print('To return the coefficient of the polynomial f(x) use:')
print('                                                     "MP3(Matrixx)"')

def MP3(Matrixx):
    A = Matrixx[:,0]
    B = Matrixx[:,1]
    for fx in range(len(Matrixx)):
        aa = np.polyfit(A, B, fx)
        bb = np.polyval(aa, A)    
        cc = np.linalg.norm(B - bb)    
        dd = [fx,cc]
        
        if fx == 0:        
            x = dd
            
        elif x[1] >= dd[1]:        
            z = dd[0]
            
    p = np.polyfit(A, B, z)
    
    print('The coefficients are: ',p)