from numpy import sqrt
from Utils import *
def coeficientePearson(xquadrado, yquadrado, x, y, xy, n):
    return (n*xy-x*y)/(sqrt(n*xquadrado-x**2)*sqrt(n*yquadrado-y**2))

def testeHipotese(r, n):
    return r*sqrt((n-2)/(1-r**2))

def calculaBeta1(n, xy, x, y, x2):
    return (n*xy-x*y)/(n*x2-x**2)

def calculaBeta0(n, x, y, beta1):
    return (y/n)-beta1*(x/n)

def calculaQMRES(n, y2, y, beta1, xy, x):
    return ((n*y2-y**2)-beta1*(n*xy-x*y))/(n-2)

def calculaCoefDeter(n,  xy,  x,  y,  x2,  y2):
    return (n*xy-x*y)**2/((n*x2-x**2)*(n*y2-y**2))

def calculaCoefDeterAjust( n,  xy,  x,  y,  x2,  y2):
    return 1-(n-1)/(n-2)*(1-calculaCoefDeter(n,xy,x,y,x2,y2))

def intervaloConfiancaBeta1(t, beta1, qmres, x2, x,n):
    return (beta1-t*sqrt(qmres/(n*x2-x**2)),beta1+t*sqrt(qmres/(n*x2-x**2)))
    
def intervaloConfiancaBeta0(t,beta0, qmres, x2, x,n):
     return (beta0-t*sqrt(qmres*(1/n+(x/n)**2/(n*x2-x**2))),beta0+t*sqrt(qmres*(1/n+(x/n)**2/(n*x2-x**2))))

def testeHipotesebeta1(beta1, qmres, x2, x,n):
    return beta1/sqrt(qmres/(n*x2-x**2))

def testeHipotesebeta0(beta0, qmres, x2, x,n):
    return beta0/sqrt(qmres*(1/n+(x/n)**2/(n*x2-x**2)))

def icparatodosx(t,beta0,beta1,qmres,x2,x,n,x0):
    return ((beta0+beta1*x0)-t*sqrt(qmres*(1/n+((x0-x/n)**2)/(n*x2-x**2))), (beta0+beta1*x0)+t*sqrt(qmres*(1/n+((x0-x/n)**2)/(n*x2-x**2))))
    



