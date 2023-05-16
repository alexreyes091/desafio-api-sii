# Desafío API SII

## Desafio

---

El Servicio de Impuestos Internos (SII) de Chile mantiene una tabla con los valores de la Unidad de Fomento actualizados para cada año. Tu desafío consiste en crear una API en Python que permita a los usuarios consultar el valor de la Unidad de Fomento para una fecha específica utilizando scraping.

Para ayudarte en el desarrollo de este desafío, puedes utilizar la tabla de valores de la Unidad de Fomento actualizados para cada año que se encuentra en el siguiente enlace: <https://www.sii.cl/valores_y_fechas/uf/uf2023.htm>

## Requisitos

---

- Python 3.x
- pip (administrador de paquetes de Python)

## Dependencias

---

- La lista de dependencias se encuentra en  'requirements.txt'

## Puesta en marcha

---

##### 1. Clonar el repositorio

```bash
> git clone https://github.com/alexreyes091/desafio-api-sii.git
```

##### 2. Navegar al directorio del proyecto

- Instalar las dependencias del proyecto.

```bash
> pip install -r requirements.txt
```

##### 3.  Ejecutar el main.py

```bash
> uvicorn main:app --reload
```

## Detalles de Uso

---
Tras iniciar el servidor podra ingresar a la siguiente URL.

```bash
http://127.0.0.1:8000/docs
```

Encontraremos dos endpoint, el primero es por redireccionamiento a *'/docs'*, el segundo cumple con la funcionalidad que nos interesa.

##### *Ejemplo base de la url:*

```bash
http://127.0.0.1:8000/api/sii/date/day/uf/2023-05-16
```

El endpoint se estructura de la siguiente forma:
```bash 
http://127.0.0.1:8000/api/sii/date/{typeSearch}/{unitFoment}/{date}
```

- **typeSearch**: *es el tipo de busqueda que desea realizar, pueden ser entre los valores: ['day', 'month', 'year']*
<!--  -->
- **unitFoment**: *es la unidad que puede recibir, entre las cuales son ['uf', 'dolar']*
<!--  -->
- **date**: *esta definida en formato YYYY-MM-dd, y nos devuelve la fecha segun su tipo de busqueda, y su tipo de unidad*
<!--  -->

## Bugs to fix
---

- La busqueda por: 'year' en tipo de unidad 'dolar', no devuelve la data completa.
<!--  -->
