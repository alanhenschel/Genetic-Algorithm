
# coding: utf-8

# In[44]:



# coding: utf-8

# In[22]:



# coding: utf-8

# In[29]:


import numpy as np
import random
import copy


# In[86]:

sequencia_rotas = np.array([[0,4,7,2,0],[0,2,7,8,0],[0,2,1,8,0],[0,9,4,2,0],[0,5,1,9,0]])





# In[87]:


sequencia_rotas


# In[88]:


class valor_rotas:
    valor = np.random.randint(low=0, high=10,size=(10,10))




# In[89]:


valor_rotas.valor


# In[90]:


def fitness(populacao):
    
    fit = 0
    fit2 = [None] * (populacao.shape[0] )
    for i in range(populacao.shape[0]):
        #print("rota:{}".format(i))
        fit = 0
        for j in range((populacao.shape[1] -1)):
            fit+= valor_rotas.valor.item(populacao.item(i,j),populacao.item(i,j+1))
                #print("cidade 1:{}".format(populacao.item(i,j)) + "cidade2:{}".format(populacao.item(i,j+1)))
                #print("fit cromossomo:{}".format(fit) + "valor cromosso:{}".format(valor_rotas.valor.item(populacao.item(i,j),populacao.item(i,j+1))))
        fit2[i] = fit;
    return fit2


# In[91]:


def fitness_especial(populacao):
    fit = 0
    for i in  range(len(populacao)-1):
        fit+= valor_rotas.valor.item(populacao[i],populacao[i+1])
    #print("\033[33mfitness\033[m" + repr(fit))
    return fit
    


# In[92]:


def filho_melhor(populacao,filho):
    custos = []
    custos2 = []
    menores = []
    menores2 = []
    custos = fitness(populacao)
    custos2 = fitness_especial(filho)
    
    for i in  range(len(custos)):
        if custos[i] > custos2:
            menores.insert(i,i);
    for i in menores:
        menores2.insert(i,fitness_especial(populacao[i]))
    if len(menores)!=0:
        return menores2.index(max(menores2))
    else:
        return 0


# In[93]:


def roleta(populacao):
    
    r = random.random()
    soma = 0
    total = sum(fitness(populacao))
    for i in populacao:
        soma = soma + (fitness_especial(i)/total)
        
        if r < soma:
            return i


def auto_generated():
    
    a = np.random.randint(10, size=5)
    
    temp2 = list(np.copy(a))
    for e in range(len(a)):
        if temp2.count(a[e]) > 1:
            a = auto_generated()
    
    return list(a)



def reproduz(x,y):
    filho = []
    temp = list(np.copy(filho))
    aux = x[1:]
    aux2 = y[:-1]
    aux = aux[:-1]
    aux2 = aux2[1:]
    
    filho.insert(0,0)
    for i in range(len(aux)):
        if i < 1:
            filho.append(aux[i])
    for j in range(len(aux2)):
        
        if j >=1 and j <=2:
            filho.append(aux[j])
    filho.append(0)
    print("valor de filho:{}".format(filho))
        
    for e in range(len(filho)):
        if temp.count(filho[e]) > 1:
            filho = auto_generated()
            
        
    return filho


# In[96]:


def mutacao(filho):
    aux = list(np.copy(filho[: -1]))
    aux2 = list(np.copy(filho[1:]))
    aux = list(np.copy(aux[1:]))
    aux2 = list(np.copy(aux2[:-1]))
    print("valor de aux:{}".format(aux))
    print("valor de aux2:{}".format(aux2))
    
    del filho[:]
    filho.insert(0,0)
    for i in range(len(aux)):
        if i ==2:
            filho.append(aux[i])
    for j in range(len(aux2)):
        
        if j <2:
            filho.append(aux[j])
    
    print("valor de filho mutado:{}".format(filho))
    
    temp = list(np.copy(filho))
    for e in range(len(filho)):
        if temp.count(filho[e]) > 1:
            filho = auto_generated()
            
    filho.insert(4,0)
    
    
    return filho


# In[97]:


def insere_filho(populacao,filho):
    custos = []
    custos2 = 0
    menores = []
    menores2 = []
    custos = fitness(populacao)
    custos2 = fitness_especial(filho)
    
    for i in  range(len(custos)):
        if custos[i] > custos2:
            menores.insert(i,i)
    for i in menores:
        menores2.insert(i,fitness_especial(populacao[i]))
    for i in  range(len(populacao)):
        if len(menores)!=0 and i == menores2.index(max(menores2)):
            populacao[i] = list(np.copy(filho))

    return populacao


# In[98]:


def algoritmo_genetico(populacao):
    iteracoes = 0
    
    while (iteracoes < 20):
        
        custos = fitness(populacao)
        print("\n populacao:\n{}".format(populacao))
        print("\n custos:\n{}".format(custos))
        y = roleta(populacao)
        x = roleta(populacao)
        #print("valor de x:{}".format(x))
        #print("valor de y:{}".format(y))
        filho = reproduz(x,y)
        if (random.random() < 0.2):
            filho = mutacao(filho)
        
        for i in custos:
            if i > fitness_especial(filho):
                populacao = insere_filho(populacao,filho)
                break
        print("\n populacao:\n{}".format(populacao))
        print("\nfitness população:\n{}".format(sum(fitness(populacao))))
        print("\n iterações:\n{}".format(iteracoes))
        iteracoes+=1
        


# In[99]:


algoritmo_genetico(sequencia_rotas)



# In[21]:




