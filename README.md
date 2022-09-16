# Analisis Reporte y Reporte Sobre Desempeño modelo

## Reporte Modelo

El documento pdf con reporte y Analisis se encuentra en la carpeta MRAR junto al archivo ejecutable 

## Arquitectura del Modelo

Varia para su analisis

##  Caracteristicas Dataset
Dataset de personas con anemia y sus caracteristicas obtenido  de kaggle

Link de dataset:
https://www.kaggle.com/datasets/biswaranjanrao/anemia-dataset

### Variables independientes

Gender: 0 - male, 1 - female


Hemoglobin: Hemoglobin is a protein in your red blood cells that carries oxygen to your body's organs and tissues and transports carbon dioxide from your organs and tissues back to your lungs


MCH: MCH is short for "mean corpuscular hemoglobin." It's the average amount in each of your red blood cells of a protein called hemoglobin, which carries oxygen around your body.


MCHC: MCHC stands for mean corpuscular hemoglobin concentration. It's a measure of the average concentration of hemoglobin inside a single red blood cell.


MCV: MCV stands for mean corpuscular volume. An MCV blood test measures the average size of your red blood cells.

### Variable dependientes

La variable dependiente que queremos predecir correctamente a partir de nuestras caracteristicas es si la persona tiene anemia o no

## Preprocesamiento

Se cambio en caracteristica de Genero los valores categoricos de label encoding a 1-hot-enconding.

Se dividio el dataset en trainig set y validation set

## Resultados

Se realizarion varias comparaciones,el modelo elejido finalmente tiene:


Training Score 0.952112676056338


Testing Score 0.9634831460674157
### Metricas
![image](https://user-images.githubusercontent.com/43545831/190538341-5b20fd91-1ed1-494f-8511-70132cc59005.png)

