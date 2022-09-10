'''
Momento de retroalimentacion 3
Alan Eduardo Aquino Rosas

Para este modelo se trabajo sobre un dataset para la detencion de anemia
Se decidio usar una metodo de la libreria de scikit-learn para redes neurnales.
Asi en las capas ocultas se puedan computar nuevas caracteristicas y funciones mas interesantes

Las 5 principales  caracteristicas del dataset son:

Gender: 0 - male, 1 - female
Hemoglobin: Hemoglobin is a protein in your red blood cells that carries oxygen to your body's organs and tissues and transports carbon dioxide from your organs and tissues back to your lungs
MCH: MCH is short for "mean corpuscular hemoglobin." It's the average amount in each of your red blood cells of a protein called hemoglobin, which carries oxygen around your body.
MCHC: MCHC stands for mean corpuscular hemoglobin concentration. It's a measure of the average concentration of hemoglobin inside a single red blood cell.
MCV: MCV stands for mean corpuscular volume. An MCV blood test measures the average size of your red blood cells.



La variable dependiente que queremos predecir correctamente a partir de nuestras caracteristicas es la persona es anemica o no
Results: 0- not anemic, 1-anemic



La funcion de activacion elegida fue la relu debido a que funciona mejor para redes neuronales


Se haran varias comparaciones para determinar cuales con los hyperparamentros que mas nos convienen 
'''


#Importacion de librerias 
import pandas as pd #For dataset reading
from sklearn.model_selection import train_test_split #For Training/Cross-Validation/Test
from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
import matplotlib.pyplot as plt #For graphing


#Preparacion de dataset
DF=pd.read_csv("./Dataset/anemia.csv")
df_gender=pd.get_dummies(DF["Gender"],prefix="Gender")
DF_clean=pd.concat([DF,df_gender],axis=1)
DF_clean=DF_clean.drop("Gender",axis=1)
df_y=DF_clean["Result"]
DF_Xclean=DF_clean.drop("Result",axis=1)
print(DF_Xclean.head())


train_x,test_x,train_y,test_y=train_test_split(DF_Xclean,df_y,random_state=2)


#----------------------------------Red Neuronal con 1 capa------------------------------------

#Configuracion de red neuronal para clasificacion
anemia_nn_1=MLPClassifier(random_state = 0,
                        hidden_layer_sizes = (5),
                        activation = "relu",
                        verbose = False,
                        solver = "adam",
                        learning_rate = "adaptive", 
                        max_iter = 1000)

#Entrenamiento red neuronal
anemia_nn_1.fit(train_x,train_y)

#Resultados red neuronal
print("Training Score",anemia_nn_1.score(train_x,train_y))
print("Testing Score",anemia_nn_1.score(test_x,test_y))


#Prediciones 
print("---------------------------Predicciones--------------------------------------")
for i in range(0,100,10):
    print("Anemia? Estimado",anemia_nn_1.predict([DF_Xclean.loc[i]]),"Real",df_y[i])


print("---------------------Red Neuronal con 2 capas----------------------------------------")    
#----------------------------------Red Neuronal con 2 capas------------------------------------

#Configuracion de red neuronal para clasificacion
anemia_nn_2=MLPClassifier(random_state = 0,
                        hidden_layer_sizes = (5,5),
                        activation = "relu",
                        verbose = False,
                        solver = "adam",
                        learning_rate = "adaptive", 
                        max_iter = 1000)

#Entrenamiento red neuronal
anemia_nn_2.fit(train_x,train_y)

#Resultados red neuronal
print("Training Score",anemia_nn_2.score(train_x,train_y))
print("Testing Score",anemia_nn_2.score(test_x,test_y))


#Prediciones 
print("---------------------------Predicciones--------------------------------------")
for i in range(0,100,10):
    print("Anemia? Estimado",anemia_nn_2.predict([DF_Xclean.loc[i]]),"Real",df_y[i])
    
#----------------------------------Red Neuronal con 5 capas------------------------------------

#Configuracion de red neuronal para clasificacion
anemia_nn_3=MLPClassifier(random_state = 0,
                        hidden_layer_sizes = (5,5,5,5),
                        activation = "relu",
                        verbose = False,
                        solver = "adam",
                        learning_rate = "adaptive", 
                        max_iter = 1000)

#Entrenamiento red neuronal
anemia_nn_3.fit(train_x,train_y)

#Resultados red neuronal
print("Training Score",anemia_nn_3.score(train_x,train_y))
print("Testing Score",anemia_nn_3.score(test_x,test_y))


#Prediciones 
print("---------------------------Predicciones--------------------------------------")
for i in range(0,100,10):
    print("Anemia? Estimado",anemia_nn_3.predict([DF_Xclean.loc[i]]),"Real",df_y[i])