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

**Respuesta:**

**Arquitectura propuesta:**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ca85fd9-04f1-43d3-b6b7-06ec09c3e729/Untitled.png)

**¿Por qué deberíamos usar esa arquitectura?**

La arquitectura que se usará será una arquitectura limpia basada en una arquitectura hexagonal. Nuestra solución estará divida por módulos, entidades o conceptos de la lógica del negocio (inicialmente solo se verá allí la entidad ORDERS). Dividir nuestra solución de está forma nos va a permitir dar cumplimiento a una mayor cantidad de atributos de calidad por cuanto a la hora de realizar modificaciones sabremos a que parte de la lógica del negocio dirigirnos, permitiendo una mayor facilidad a la hora de mantener nuestro código. 

Por otra parte, en cuanto al atributo de desplegabilidad, la idea de la implementación de esta arquitectura, es que esta nos permite sin importar la infraestructura en la que se despliegue nuestra solución debería ser fácilmente integrable en cuanto se encuentra separada e independiente de nuestra lógica del negocio. En cuento a seguridad, la arquitectura limpia nos permite que la dependencia entre capas sea desde el exterior hacia el interior, lo cual nos garantiza hasta cierto punto, que las capas más externas no tendrán información relevante de las capas internas y simplemente interactúe con estas.

El punto a favor más importante es la escalabilidad, esta arquitectura nos permite escalar nuestra solución de una forma más rápida, si a la lógica del negocio (que regularmente no cambia mucho) se le agrega un nuevo modulo o entidad, solo debemos agregarla con sus propias capas, y si es necesario alguna modificación o usar otro módulo, podremos disponer de las interfaces que estos dispongan para esto o ir puntualmente a la capa que requiere la modificación para ese módulo. 

En cuanto a usabilidad, está nos permitiría implementar diferentes interfaces para que nuestro servicio, si así lo requiere, se pueda usar por aplicaciones externas.

Comparando nuestra solución con una arquitectura por capas, por ejemplo, esta dificulta varios factores importantes, uno de esos es que la lógica del negocio dependerá siempre de la capa de acceso a datos. Esto implica que todas las demás capas dependan al final de la capa de acceso a datos. También, los cambios en una capa, suelen afectar a las demás capas en alguna medida. Para **sistemas más grandes,** el mantenimiento y la escalabilidad se hace más complejos por la cantidad de partes del sistema que se deben cambiar o modificar.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/62ab6100-e067-44bc-9e5b-764b7b79a3eb/Untitled.png)

Ahora si hacemos una comparación con una arquitectura monolítica, en está es sabido que es fácil su desarrollo, pero está al no ser un arquitectura limpia y mantener todo tan junto, su mantenibilidad y escalabilidad no son las mejores, a la vez que como toda arquitectura basada en capas, depende mucho de los datos y no así del dominio o lógica del negocio toda la lógica.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b46ab238-8d48-408d-99c3-c69a8e310800/Untitled.png)

### **¿Por qué deberíamos usar esas tecnologías?**

Las tecnologías que se plantean para la solución son: 
FastAPI, Starlette, Uvicorn, MongoDB.

### **FastAPI:**

Se plantea el uso de FastAPI ya que es un framework ligero pero potente, además es el que mejor domino. Por otra parte, tomando de la web de FastAPI sus características, encontramos lo siguiente:

- Basado en estándares abiertos (Open API, JSON Schema).
- Documentación automática (Swagger UI y ReDoc).
- Excelente soporte para los editores visualstudio code y pycharm.
- No es muy extenso, con configuraciones por defecto para todo.
- Validaciones para la mayoría de tipos de datos.
- La seguridad y la autenticación están integradas. Sin ningún compromiso con bases de datos ni modelos de datos.
    - HTTP Basic.
    - **OAuth2** (también con **JWT tokens**).
    - API keys en:
        - Headers.
        - Parámetros de Query.
        - Cookies, etc.
    - todas las características de seguridad de Starlette (incluyendo **session cookies**
    ).
- Incluye un sistema de **Inyección de dependencias** manejadas automáticamente por FastAPI.
- Alto desempeño, incluso a la par de Nodejs y Go.

### Starlette:

Gracias a Starlette FastAPI tiene, entre otras cosas, soporte ASGI. Cuando creamos una app con fastapi, esta podrá hacer uso de asincronismo y su integración será con servidores basados en ASGI que tienen un mejor rendimiento como sería Uvicorn.

### Uvicorn:

Es un servidor web para Python basado en ASGI, Liviano y fácil de manipular. Es el servidor sobre el que se suele montar las apps desarrolladas con FastAPI.

### Comparación FastAPI con otros Frameworks

**Django**

Si hacemos una comparación de FastAPI con Django, este último es un framework mucho más extenso, robusto y que por defecto no viene optimizado para microservicios (Puede usarse Django REST framework para este fin), por el contrario está pensado en un modelo (Model Template View) el cuál prioriza el desarrollo de aplicaciones completas (monolíticas), haciendo que se requieran una serie de configuraciones antes de poder iniciar (esto puede ser una ventaja o desventaja según se mire) para nuestro caso, Django aunque es fácil de manejar requiere muchas configuraciones y librerías adicionales para llegar a un desarrollo tan corto como el de este problema.

**Flask**:

Flask es un excelente framework para python pero con la desventaja que inicialmente no está pensado para el soporte de asincronismo, aunque se puede resolver esto con el uso de servidores que suplan esta necesidad, debe hacerse con librerías externas, lo cual podría traer inconvenientes por la falta de soporte.

### MONGO DB:

Debido a que lo que requerimos es un servicio que ponga a disposición una lista de ordenes (haremos solo consultas) requerimos una base de datos que optimice el rendimiento al hacer lectura de datos. MongoDB al ser una base de datos no relacional, facilita las “transacciones” de este tipo, optimizando el rendimiento especialmente en este aspecto para nuestro servicio.

Si por el contrario estuvieramos desarrollando un servicio que buscara optimizar la escritura de datos garantizando la integridad de los mismos podríamos hacer uso de una base de datos SQL.

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

