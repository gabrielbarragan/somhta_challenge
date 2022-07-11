# SOMHTA CHALLENGE

Este es repositorio responde al desarrollo de un reto planteado para validación de conocimientos para una empresa de desarrollo es aplicable para cualquier tipo de lenguaje de programación, el lenguaje para desarrollar la prueba debe ser el que se solicita para la vacante.

La prueba consiste en 2 fases, cada una con su grado de complejidad y finalidad.

## Prueba Algorítmica:

Mejorar un algoritmo que  procesa más de 1.000 de órdenes por segundo, estas órdenes
tienen que hacer un proceso de actualización y guardado en base de datos para que la
persistencia de los datos de esas órdenes esté siempre protegida a lo largo del tiempo, el
principal problema que se presenta con estas órdenes es que guardar dichas órdenes de
manera lineal provoca un embudo, lo que se pide hacer es una solución que mejore la velocidad de guardado de las ordenes que ofrece el algoritmo existente.

### Algoritmo original:

[test01.py](https://gist.github.com/athmos-pedrocarvajal/d5148df0fa664bc242c222ccb40911c2)

### Algoritmo mejorado:

Esta solución se planteó haciendo uso de paralelismo basado en hilos, esto se logra con el módulo **threading** que incluye Python por defecto desde la version 3.8 (en la versión 3.7 era opcional).

[](https://github.com/gabrielbarragan/somhta_challenge/blob/main/test_01_modified.py)

**Tiempos:**

El algoritmo original tarda alrededor de 500 segundos en terminar de procesar las ordenes.

La mejora planteada en la solución permite que las ordenes en su totalidad se procesen en aproximadamente 1 segundo.

## Prueba de uso de librerías y servicios:

se busca mejorar es un servicio usado para la distribución de un listado de órdenes que están dentro del sistema. Este listado lo conforman más de 1.000.000 de órdenes, por lo que tendrá que tener presente que la respuesta de este endpoint no puede tardar más de 15 segundos en devolver la información que se solicita. 

Las tareas que se piden son:

- Plantear un diagrama basado en micro-servicios especificando qué tecnologías se
deben usar, sustentando sus decisiones y respondiendo las siguientes preguntas:
- [ ]  ¿Por qué deberíamos usar esa arquitectura?
- [ ]  ¿Por qué deberíamos usar esas tecnologías?
- [ ]  ¿Cuáles son las ventajas de su arquitectura propuesta sobre el resto de
arquitecturas existentes? Compare por lo menos 3 arquitecturas.
- [ ]  ¿Cuáles son las ventajas de las tecnologías propuestas para desarrollar dicha
arquitectura? compara contra otras tecnologías dentro del mercado.
- [ ]  Desarrollar un código de ejemplo donde se apliquen la arquitectura y tecnologías
seleccionadas.


## Código de la solución:

[https://github.com/gabrielbarragan/somhta_challenge](https://github.com/gabrielbarragan/somhta_challenge)

1. Clone el repositorio.
    
    ```bash
    git clone https://github.com/gabrielbarragan/somhta_challenge.git
    ```
    
2. Dirijase a la carpeta:
    
    ```bash
    cd somhta_challenge
    ```
    
3. Instale todas las dependencias y cree el entorno virtual con poetry (tener instalado el gestor de dependencias poetry para Python):
    
    ```bash
    poetry install
    ```
    
4. Ubíquese en la carpeta “orders_microservices” que se encuentra dentro del repositorio y cree el archivo **.env** copie y pegue el siguiente código y cambie los valores que se encuentran en el siguiente
    
    ```bash
    MONGODB_URL=<<string_de_conexion_mongo_data_base>>
    MONGODB_NAME=<<nombre_de_la_base_de_datos>>
    MONGODB_COLLECTION_NAME=<<nombre_de_la_coleccion>>
    ```
    
5. ubiquese en la carpeta principal del repositorio y ejecute el siguiente comando para ir a la carpeta **src** dentro del proyecto:
    
    ```bash
    cd orders_microservices/distribution_microservices/src
    ```
    
6. Ejecute el siguiente comando y la aplicación estará corriendo en el puerto indicado en la consola:
    
    ```bash
    uvicorn main:app --reload
    ```

