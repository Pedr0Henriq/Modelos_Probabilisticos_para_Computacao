import matplotlib.pyplot as plt
from Functions import *
from Utils import *

n=9
som_x_e_y= somaxy
som_x=somax
som_y=somay
som_x_quadrado= somax2
som_y_quadrado= somay2
xy = som_x_e_y
t=3.49948
resultado = coeficientePearson(som_x_quadrado,som_y_quadrado,som_x,som_y,xy,n)
print(f'Coeficiente de Correlação Linear de Pearson = {round(resultado,5)}')

tc = testeHipotese(resultado,n)
print(f'Estatística de Teste = {round(tc,5)}')

beta1 = calculaBeta1(n,xy,som_x,som_y,som_x_quadrado)
beta0 = calculaBeta0(n,som_x,som_y,beta1)
print(f'Beta1 = {round(beta1,5)}')
print(f'Beta0 = {round(beta0,5)}')

qmres = calculaQMRES(n,som_y_quadrado,som_y,beta1,som_x_e_y,som_x)
print(f'Variância Residual Populacional = {round(qmres,5)}')

coef_deter = calculaCoefDeter(n,som_x_e_y,som_x,som_y,som_x_quadrado,som_y_quadrado)
print(f'Coeficiente de Determinação = {round(coef_deter,5)}')

coef_deter_ajust = calculaCoefDeterAjust(n,som_x_e_y,som_x,som_y,som_x_quadrado,som_y_quadrado)
print(f'Coeficiente de Determinação Ajustado = {round(coef_deter_ajust,5)}')
print(f'Intervalo de Confiança para Beta1 = {intervaloConfiancaBeta1(t,beta1,qmres,som_x_quadrado,som_x,n)}')
print(f'Intervalo de Confiança para Beta0 = {intervaloConfiancaBeta0(t,beta0,qmres,som_x_quadrado,som_x,n)}')
if(t<testeHipotesebeta1(beta1,qmres,som_x_quadrado,som_x,n) or -t>testeHipotesebeta1(beta1,qmres,som_x_quadrado,som_x,n)):
    print(f'{round(testeHipotesebeta1(beta1,qmres,som_x_quadrado,som_x,n),5)}. Rejeita H0 para Beta1')
else:
    print(f'{round(testeHipotesebeta1(beta1,qmres,som_x_quadrado,som_x,n),5)}. Aceita H0 para Beta1')
if(t<testeHipotesebeta0(beta0,qmres,som_x_quadrado,som_x,n) or -t>testeHipotesebeta0(beta0,qmres,som_x_quadrado,som_x,n)):
    print(f'{round(testeHipotesebeta0(beta0,qmres,som_x_quadrado,som_x,n),5)}. Rejeita H0 para Beta0')
else:
    print(f'{round(testeHipotesebeta0(beta0,qmres,som_x_quadrado,som_x,n),5)}. Aceita H0 para Beta0')

icY= map(lambda x: icparatodosx(t,beta0,beta1,qmres,som_x_quadrado,som_x,n,x),lista)
icY_list= list(icY)
print(f'Intervalo de Confiança para cada Y = {icY_list}\n')

plt.plot(lista,list2, label= 'Y', )
plt.plot(lista,icY_list, label = 'Extremos de Y')
plt.xlabel(' Especificação do Fabricante ')
plt.ylabel(' Taxa de Transferência ')
plt.title(' Intervalo de Confiança para cada Y ')
plt.legend()
plt.show()