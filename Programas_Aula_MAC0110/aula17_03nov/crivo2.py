# -*- coding: utf-8 -*-

'''
 * Arquivo: crivo2.py
 * ----------------
 * Este programa determina todos os primos menores que n, para um dado n.
 * Para isso, usa o metodo conhecido como o Crivo de Eratóstenes.
 *
 * O programa faz uso de um vetor a[0..n-1] que é inicializado com 1.
 * (Note que os índices 1..n-1 sao exatamente os números que desejamos 
 *  descobrir se são primos ou não.)
 * 
 * No final, as entradas desse vetor serão 0 ou 1, sendo que 
 *   a[i] = 1 indica que i é primo e
 *   a[i] = 0 indica que i não é primo.
 * 
 *
 
'''

import math
import time

def main():
    
    n = int(input("De o valor de n (menor que 10000):  "))

    hora_inicio = time.time()  ## hora nesse ponto
    
    # inicializacao da lista a com valor 1 em todas as posicoes
    a = [1] * n    #<================== Veja (jeito diferente de inicializar a lista a  com 1)

    # print(" a = ", a) 

    a[0] = a[1] = 0  # indica que  0 e 1 não são primos
    
    raizn = int(math.sqrt(n))
    
    for i in range(2, raizn + 1):  #<=======  fica mais eficiente (testa menos)
        if a[i] == 1:          
           j = i
           while i * j < n:
               a[i * j] = 0
               j += 1
    # print(a)    
               
    conta = 0 
    print("Números primos menores que %d:" %(n))           
    for i in range(2, n):
        if a[i] == 1:
            #print(i, end=',  ')
            conta += 1 
    print()
    
    print("total de números primos menores que %d  ====>  %d " %(n,conta))

    hora_fim = time.time()
    print("Tempo gasto = ", hora_fim - hora_inicio) 

    
#--------------
main()


'''
 ---  Você entendeu por que j começa em i? E por que zeramos as posicoes i*j?
 
 ---  O que acontece se o teste "if (a[i]) == 1" for retirado? 
 
'''

