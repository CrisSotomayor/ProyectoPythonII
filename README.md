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
4. Utilizamos diversas funciones de la librería de `pandas` para analizar la información obtenida, específicamente, evaluamos qué genes eran los que se repetían más y qué vías de señalización están asociadas a ellos.
5. Utilizamos la librería `matplotlib` para obtener gráficas representando los resultados obtenidos. 
