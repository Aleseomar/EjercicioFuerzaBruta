[![Python Tests](https://github.com/Aleseomar/EjercicioFuerzaBruta/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/Aleseomar/EjercicioFuerzaBruta/actions/workflows/python-package-conda.yml)

# EjercicioFuerzaBruta

**Realizado por:** *GRUPO 3*  

**Participantes:**

- Álvaro González
- Alejandro Seoane
- Israel Valderrama
- Víctor Jiménez

****

**Definición del ejercicio**  

Desarrollar en equipo un script que permita usando técnicas de fuerza bruta, comprobar usando un diccionario el texto con el que se generó un valor usando un algoritmo SHA.

****

**Perfiles y labores del grupo:**

1.- ***Product owner:*** Alejandro Seoane.   
Se encargará de organizar las tareas, crear el soporte del proyecto y se asegura del cumplimiento del calendario.

2.- ***Technical chief:*** Alejandro Seoane y Álvaro González. Investigaran las tecnologías necesarias para el desarrollo.   

3.- ***Q&A:*** Álvaro González. Desarrollará las pruebas del código.

4.- ***Devops:*** Javier Ortega e Israel Valderrama. Organizarán el procedimiento para automatizar la ejecución de las pruebas de código.

5.- ***Developer:*** Javier Ortega e Israel Valderrama. Desarrollarán el código.

****

**Realización:**

- Alejandro encontro un diccionario con un montón de contraseñas comunes para poder realizar las pruebas.
- Álvaro  encontro una librería llamada hashlib para ejecutar los cáculos del sha de las contraseñas. Se ha asegurado de que sea segura ya que el único CVE es de 2008 y ya está parcheado.
- Posteriormente hemos creado el test que usaremos posteriormente que verifica la contraseña.
- Por último, entre Javi e Israel han programado el programa para automatizar la lectura de las contraseñas, transformarlas con el sha y compararlas
