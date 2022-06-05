
from deap import creator, base, tools, algorithms
import numpy as np
import matplotlib.pyplot as plt

#Definir como un problema de minimizacion, se define fitness
#Encontrar la ruta más corta
creator.create("FitnessMinimo", base.Fitness, weights=(-1.0, ) )

#Representacion de los individuos, cromosomas
creator.create("ReprIndividuo", list, fitness=creator.FitnessMinimo)

#Se obtiene la base de las definiciones 
#Aqui se registran los objetivos y elementos del algoritmo genetico
toolbox = base.Toolbox()

#Registrar el numero de genes
#Para nuestro ejemplo los genes son los diferentes destinos que se deben recorrer en el rally
nDestinos = 11
toolbox.register("Genes", np.random.permutation, nDestinos)
print("Ejemplo de genes: ", np.random.permutation(nDestinos))

#Ahora que tenemos los genes podemos registrar los cromosomas de nuestros individuos
toolbox.register("Individuos", tools.initIterate, creator.ReprIndividuo, toolbox.Genes)
print("Un individuo: ", toolbox.Individuos.func(creator.ReprIndividuo, toolbox.Genes))

#Se debe definir la poblacion
toolbox.register("Poblacion", tools.initRepeat, list, toolbox.Individuos)

#Generacion de la poblacion
pob = toolbox.Poblacion(n=15)
print("Poblacion inicial: ", pob)

#Seleccion por torneo de los cromosomas que seran cruzados en la siguiente generacion
toolbox.register("select", tools.selTournament, tournsize=2)

#Crossover - Recombinacion o cruzamiento
toolbox.register("mate", tools.cxPartialyMatched)

#Mutacion, modifica al azar parte del cromosoma de los individuos 
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1) #probabilidad de un indice de ser mutado


MtDistancia =  [[0,16,86,34,10000,11,10000,72,21,10000,29],
                [16,0,10000,19,36,10000,61,60,82,74,10000],
                [86,10000,0,96,91,70,10000,88,59,19,16],
                [34,19,96,0,10000,32,36,64,55,74,96],
                [10000,36,91,10000,0,9,77,20,7,8,23],
                [11,10000,70,32,9,0,79,13,56,26,64],
                [10000,61,10000,36,77,79,0,42,21,10000,79],
                [72,60,88,64,20,13,42,0,6,27,10000],
                [21,82,59,55,7,56,21,6,0,40,10000],
                [10000,74,19,74,8,26,10000,27,40,0,21],
                [29,10000,16,96,23,64,79,10000,10000,21,0]]

def funcAptitud(individuo):
    f=0
    for i in range(nDestinos-1):
        local1 = individuo[i]
        local2 = individuo[i+1]
        distancia = MtDistancia[local1][local2]
        f = f + distancia

    return f,

#Evaluacion del mejor camino que recorre todos los vertices 
#Registro de la funcion de aptitud
toolbox.register("evaluate", funcAptitud)

#Estadistica
#Guardar los mejores individuos y aptitudes a lo largo de las generaciones
def guardarEstadistica(individuo):
    return individuo.fitness.values

estadistica = tools.Statistics(guardarEstadistica)
estadistica.register("min", np.min)

#Para realizar un seguimiento de las mejores rutas, introducimos un contenedor del salon de la fama.
hallOfFame = tools.HallOfFame(1)

#Ejecucion del algoritmo genetico
result, log = algorithms.eaSimple(pob,
                                  toolbox,
                                  cxpb=0.8,         #probabilidad de apareamiento de dos individuos
                                  mutpb=0.3,        #probabilidad de mutacion en un individuo
                                  stats=estadistica,
                                  ngen=30,          #numero de generaciones
                                  halloffame=hallOfFame,   #objeto que contiene los mejores individuos
                                  verbose=True)

#print(result)

print(hallOfFame)

mejor = hallOfFame[0]
funcAptitud(mejor)

log

menores = log.select('min')

plt.plot(menores, label= 'Minimos')
plt.xlabel('Generaciones')
plt.ylabel('Aptitud')
plt.legend(loc=1)
plt.show()