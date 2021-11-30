# Proyecto Final Python II  
## Identificación de genes involucrados en carcinogénesis viral  

Cristina Sotomayor Vivas (cristina@lcg.unam.mx)  
Luz Rosario Guevara Cruz (lguevara@lcg.unam.mx)  

### Objetivo  
Utilizar la base de datos [KEGG (Kyoto Encyclopedia of Genes and Genomes)](https://www.genome.jp/kegg/) para identificar qué genes están involucrados más frecuentemente en la carcinogénesis viral y en qué vías de señalización se encuentran.  

### Metodología

1. Utilizamos el módulo Bio.KEGG para acceder a la vía de señalización de interés. Por medio de la función `kegg_get` del módulo Bio.KEGG.REST, accedemos a la vía por su KEGG ID.
2. Posteriormente, obtenemos los genes de la vía, y utilizando una versión modificada de la clase `Record` de Bio.KEGG.Gene, obtenemos la información de cada gen. Modificamos la clase para, además de la información que ya se obtiene, almacenar las vías de señalización en las que participa cada uno de esos genes.
3. Utilizamos la librería `pandas` para almacenar los datos obtenidos. Almacenamos los genes en un `DataFrame`, guardando por columnas la información acerca del código de acceso, el nombre, la posición, los links a otras bases de datos, y las vías de señalización, los cuales se obtienen como atributos del objeto `Gene`.
4. Utilizamos diversas funciones de la librería de `pandas` para analizar la información obtenida, específicamente
  * Evaluamos qué genes eran los que se repetían más.
  * Evaluamos qué vías de señalización asociadas a cáncer se repiten más.
5. Utilizamos las librerías `seaborn` y `matplotlib` para obtener y guardar las gráficas que representan los resultados obtenidos. 

### Resultados

Observamos que el gen que codifica a la proteína p53 es el que más repeticiones presenta, con un total de 9.
La proteína p53 o proteína tumoral p53 es una proteína nuclear que se encarga de controlar la proliferación celular, p53 induce tanto la parada del ciclo celular que previene la replicación de DNA dañado y la apoptósis. Está clasificado como un gen supresor de tumores. Se ha encontrado que las mutaciones generadas en un álelo del gen p53 en las células somáticas se relaciona con la aparición de cancér, sin embargo cuando la mutación se presenta en células de la l´nea germinal se desarrolla el síndrome Li-Fraumeni.
El gen p53 es codificado a bajos niveles en las células de manera normal, sin embargo bajo situaciones de estrés celular p daño al DNA p53, se genera un proceso de activación y modificación post-traduccional de los residuos proteicos.
![Genes](https://github.com/CrisSotomayor/ProyectoPythonII/blob/main/figures/signif_genes.png "Genes")
Estos resultados señalan Que las mutaciones relacionadas al gen p53 es un indicio consistente para indicar la presencia o alta probabilidad para desarrollar cáncer, pues su presencia es doble al resto de mutaciones en demás genes.

La vía de señalización más asociada a cáncer es FOXO, con un total de 9 repeticiones.
FOXO box es una subfamilia de factores de transcripción asociados a la mitocrondría, estos son responsables de la expresión de ligandos a receptores para la apoptósis celular. Asímismo también se encarga de regular los procesos de proliferación celular, el metabolismo de la glucosa y resistencia a estrés oxidativo. La vía de señalixación encontrada en distintos tipos de cáncer que más interactúa con FOXO es la vía de señalización PK13/AKT.
![Vias](https://raw.githubusercontent.com/CrisSotomayor/ProyectoPythonII/main/figures/signif_pathways.png "Vias de señalizacion")
En esta gráfica podemos observar que no hay un a sola ví de señalización que sea determinante para el desarrolló de cáncer, ya que una diversidad de vías de señalzación se pueden encontrar involucradas en su desarrollo. 

### Conclusiones

Las mutaciones asociadas al gen p53 y la vía de señalización FOXO tienen evidencia cuantitativa de ser variaciones asociadas a la supresión de tumores, y los residuos proteicos alterdos son comúnmente aislados de tumores. 

