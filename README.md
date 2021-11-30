# Proyecto Final Python II  
## Identificación de genes involucrados en carcinogénesis viral  

Cristina Sotomayor Vivas (cristina@lcg.unam.mx)  
Luz Rosario Guevara Cruz (lguevara@lcg.unam.mx)  

### Objetivo  
Utilizar la base de datos [KEGG (Kyoto Encyclopedia of Genes and Genomes)](https://www.genome.jp/kegg/) para identificar qué genes están involucrados más frecuentemente en la carcinogénesis viral y en qué vías de señalización se encuentran.  

### Metodología

1. Utilizamos el módulo Bio.KEGG para acceder a la vía de señalización de interés. Por medio de la función `kegg_get` del módulo Bio.KEGG.REST, accedemos a la vía por su KEGG ID.
2. Posteriormente, obtenemos los genes de la vía, y utilizando una versión modificada de la clase `Record` de Bio.KEGG.Gene, obtenemos la información de cada gen. Modificamos la clase para, además de la información que ya se obtiene, almacenar las vías de señalización en las que participa cada uno de esos genes.
3. Utilizamos la librería `pandas` para almacenar los datos obtenidos. Almacenamos los genes en un `DataFrame`, guardando por columnas la información acerca del código de acceso, el nombre, la posición, y las vías de señalización, los cuales se obtienen como atributos del objeto `Gene`.
4. Utilizamos diversas funciones de la librería de `pandas` para analizar la información obtenida, específicamente
  * Evaluamos qué genes eran los que se repetían más.
  * Evaluamos qué vías de señalización asociadas a cáncer se repiten más.
5. Utilizamos las librerías `seaborn` y `matplotlib` para obtener y guardar las gráficas que representan los resultados obtenidos.

### Resultados

Observamos que el gen que codifica a la proteína p53 es el que más repeticiones presenta, con un total de 9.
La proteína p53 o proteína tumoral p53 es una proteína nuclear que se encarga de controlar la proliferación celular, p53 induce tanto la parada del ciclo celular que previene la replicación de DNA dañado y la apoptósis. Está clasificado como un gen supresor de tumores. Se ha encontrado que las mutaciones generadas en un alelo del gen p53 en las células somáticas se relaciona con la aparición de cáncer, sin embargo cuando la mutación se presenta en células de la línea germinal se desarrolla el síndrome Li-Fraumeni.
El gen p53 es codificado a bajos niveles en las células de manera normal, sin embargo bajo situaciones de estrés celular o daño al DNA p53, se genera un proceso de activación y modificación post-traduccional de los residuos proteicos.
![Genes](https://github.com/CrisSotomayor/ProyectoPythonII/blob/main/figures/signif_genes.png "Genes")
Estos resultados señalan que las mutaciones relacionadas al gen p53 son un indicio consistente para indicar la presencia o alta probabilidad para desarrollar cáncer, pues su presencia es doble al resto de mutaciones en demás genes.

Los siguientes 6 genes todos corresponden a subunidades de kinasas de la familia PI3K, las cuales participan en la transducción de señales y también se han asociado a cáncer.  

La vía de señalización más asociada a cáncer es FOXO, con un total de 9 repeticiones.
FOXO box es una subfamilia de factores de transcripción asociados a la mitocrondría, estos son responsables de la expresión de ligandos a receptores para la apoptósis celular. Asímismo también se encarga de regular los procesos de proliferación celular, el metabolismo de la glucosa y resistencia a estrés oxidativo. La vía de señalización encontrada en distintos tipos de cáncer que más interactúa con FOXO es la vía de señalización PIK3/AKT.
![Vias](https://raw.githubusercontent.com/CrisSotomayor/ProyectoPythonII/main/figures/signif_pathways.png "Vias de señalizacion")
En esta gráfica podemos observar que no hay una sola vía de señalización que sea determinante para el desarrollo de cáncer, ya que una diversidad de vías de señalización se pueden encontrar involucradas en su desarrollo, y se sabe que los genes encontrados previamente pueden participar en varias vías. Resaltamos la presencia de la vía PI3K-Akt, la cual podemos esperar dados los diferentes genes relacionados a ella que encontramos en el paso previo.

### Conclusiones

Las mutaciones asociadas al gen p53 y la vía de señalización FOXO tienen evidencia cuantitativa de ser variaciones asociadas a la supresión de tumores, y los residuos proteicos alterados son comúnmente aislados de tumores. Por medio de este proyecto, vimos cómo podemos recopilar diferentes tipos de información de la base de datos KEGG, en este caso genes y vías metabólicas, para obtener información de los mecanismos involucrados en esta enfermedad. Podríamos repetir este proceso para diferentes vías metabólicas, solo cambiando el código de acceso de cada vía, e incluso modificar el código para recopilar más información, por ejemplo, incluir los links que da KEGG a otras bases de datos, y usar otros módulos como `Bio.Entrez` para obtener información de otras bases. El saber cómo trabajar con diferentes bases de datos a través de programas que nosotros mismos creamos es una herramienta muy útil y muy versátil para acceder y manejar información, y el uso de herramientas como `pandas`, `matplotlib` y `seaborn` amplía lo que podemos llevar a cabo con esos datos.

### Referencias 

* Farhan, M., Wang, H., Gaur, U., Little, P., Xu J., Zheng, W. (2017) FOXO Signaling Pathways as Therapeutic Targets in Cancer, NCBI. doi: 10.7150/ijbs.20052
* Silva, A., Gutiérrez, A., Arias, C., Lazaro, I. (2006) Estructura, regulación y funciones del gen supresor de tumores p53, Congreso virtual Hispanoamérica de Anatomía Patológica. https://conganat.uninet.edu/conferencias/C016/index.html
* Carter, M., Brunet, A. (2007) FOXO transcription factors, NCBI. doi:10.1016/j.cub.2007.01.008


