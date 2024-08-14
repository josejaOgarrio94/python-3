# Programación orientada a objetos

## Qué es la POO?
La programación orientada a objetos es un paradijma de programación, en el cual vemos todo como si fueran "objetos" de la vida real, el cual tiene propiedades, acciones, métodos, etc.

Pensaremos en objetos para abstraernos del caso concreto que vamos a hacer. Eso nos ayudará a organizar el programam, escalarlo y a la reusabilidad. 

Nuestro programa estará formado por diferentes objetos, los cuales se encargarán cada uno de una cosa cada uno.

## Fundamentos de la POO

### Clases
Las clases son los elementos que nos permiten definir las propiedades y elementos contienen los objetos. 

Podríamos decir que la clase es el "molde" que nos permite crear nuestros objetos.

Para el resto de definiciones, pondremos de ejemplo que la clase será "Coche".

Para generar un nuevo objeto de la clase "Coche", podríamos indicar en el código: 
~~~
new Coche()
~~~

### Atributos / Propiedades
Los atributos son las características que tienen las clases.

Por ejemplo, si decimos que la clase define a un coche, podremos tener como atributos el color, el modelo, la marca, etc.

### Métodos o funciones
Estos métodos son las acciones que puede realizar la clase. 

Por ejemplo, en nuestra clase coche, podríamos tener como métodos:

- Arrancar()
- Acelerar()
- Frenar()
- ...

### Abstracción

Con la abstracción podemos utilizar un objeto sin conocer el funcionamiento interno de dicho objeto. Podemos ignorar qué hay dentro del objeto pero podemos utilizarlo para realizar una funcionalidad en concreto o para una tarea en concreto.

Podemos utilizar los métodos del objeto, de la clase, para interactuar con el objeto.

Es por ello que decimos que nos "abstraemos", la clase no funciona para un caso en concreto, sino que funciona para cualquier objeto que hayamos definido con dicha clase.

### Herencia

Las clases dentro de la programación orientada a objetos van a heredar propiedades y métodos unas de otras. De más genérico a más concreto.

Es decir, podemos tener una clase "Vehículo", más genérica, y otras clases más concretas, como "Autobús", "Moto", heredan las propiedades y métodos más básicos de la clase padre, y le añadirán sus propios métodos y propiedades las clases hijas.

### Modularidad

Con la modularidad podemos dividir la aplicación en partes más pequeñas que sean más específicas. Por ejemplo, podemos dividir las clases en diferentes ficheros, podemos agrupar diferentes funcionalidades similares en mismas clases, etc.

### Encapsulación

Con la modularidad, podemos obtener también el concepto de la encapsulación, que es reunir los métodos que tienen relación con una entidad concreta.

### Ocultación

Esto indica que cada objeto tiene sus datos en concreto, y dichos datos únicamente deben modificarse dentro de la clase. 
Para que estos atributos puedan ser modificados, lo que hay que tener dentro de clase son los métodos Getter y Setter de cada atributo.

Aunque si tenemos atributos públicos, podemos modificarlos desde fuera.