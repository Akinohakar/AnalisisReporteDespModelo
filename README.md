# Analisis Reporte y Reporte Sobre Desempeño modelo

##Arquitectura del Modelo

Varia para su analisis

##Caracteristicas Dataset
Es un dataset de personas con anemia de kaggle
Link:
https://www.kaggle.com/datasets/biswaranjanrao/anemia-dataset

###Variables independientes

Gender: 0 - male, 1 - female


Hemoglobin: Hemoglobin is a protein in your red blood cells that carries oxygen to your body's organs and tissues and transports carbon dioxide from your organs and tissues back to your lungs


MCH: MCH is short for "mean corpuscular hemoglobin." It's the average amount in each of your red blood cells of a protein called hemoglobin, which carries oxygen around your body.


MCHC: MCHC stands for mean corpuscular hemoglobin concentration. It's a measure of the average concentration of hemoglobin inside a single red blood cell.


MCV: MCV stands for mean corpuscular volume. An MCV blood test measures the average size of your red blood cells.

###Variable dependientes

La variable dependiente que queremos predecir correctamente a partir de nuestras caracteristicas es si la persona tiene anemia o no

##Preprocesamiento

Se cambio en la caracteristica de Genero de labael encoding a 1-hot-enconding

##Resultados

Se realizarion varias comparaciones,el modelo elejido finalmente tiene:
Training Score 0.952112676056338
Testing Score 0.9634831460674157
