# PRUEBA T.EVOLVERS

## Descripción objetivos de la prueba.

<p>
    El actual repositorio hace referencia a la prueba técnica para la empresa T.EVOLVERS, realizada en el lenguaje de programación python.
    El proyecto tiene tres objetivos:
    <br><br>
</p>

<ol>

### <li>Implementar simulador de dispositivo  eléctico. </li>
   <p>
        Para el cumplimiento de este punto, se realizó una función que de manera dinámica genera datos, 
        logrando la simulación de información dada por un dispositivo eléctrico.
        Un ejemplo de la ejecución de la función es el siguiente:
        {
            id dispositivo: 34,
            consumo: 50kW,
            fecha: 2022-07-09:08-81-59
        }.
   </p>
   <br>

### <li>Gestión de la información del punto 1.</li>
   <p>  
       Se implementa función que está pendiente de la generación de información del punto 1. 
        Al detectar una nueva generación de medida, se captura y se envía a una base de datos. 
        Dejando lista la información para tratarla en el punto 3.         
   <p>
   <br>

### <li>Administración de la información.</li>
   <p>  
       Se implementan funcionalidades sobre la información que se tiene en la base de datos.
       Las diferentes opciones son: 
        <ul>
            <li>Crear un dato relacionado a una medida eléctrica.</li>
            <li>Modificar o actualizar la información de un registro existente.</li>
            <li>Eliminar el registro de una medidad existente en la base dedatos.</li>
            <li>Leer la información guardada en la base de datos.</li>
         </ul>
   <p>
   <br>
</ol>

## Descarga del contenido del repositorio.

<p>
Para ejecutar el contenido del repositorio deberá contar con conocimientos básicos en el manejo de: <br>
    <ul>
        <li>Terminal del sistema operativo que utilice.</li>
        <li>administrador de bases de datos Postgres.</li>
        <li>Navegador de internet.</li>
    </ul>

<p>Teniendo en cuenta lo anterior se deberán llevar a cabo los siguientes pasos:</p><br>
<ul>
    <li>Clonar el repositorio. <a href='http://www.google.com.co'>GOOGLE</a></li>
    <li>Abrir la terminal y acceder a la carpeta donde esta el repositorio clonado.</li>
    <li>Ejecutar el comando <b>py install -r requirements.txt</b></li>
    <li>Crear una base de datos SQL localmente con el nombre: medidas.</li>
    <li>Abrir la terminal y acceder a la carpeta donde esta el repositorio clonado.</li>
    <li>Navegador de internet</li>
</ul>
<br>

## Ejecución del contenido del repositorio.

<ul>
    <li>Abrir una terminal, entrar a la carpeta donde esté el repositorio e ingresar el comando: <b>uvicorn main:app --reload --env-file=.env</b></li>
    <li>Abrir una terminal, entrar a la carpeta donde esté el repositorio e ingresar a la ruta redis app y ejecutar el comando: 
    <b>py publisher.py</b> </li>
    <li>Abrir una terminal, entrar a la carpeta donde esté el repositorio e ingresar a la ruta redis app y ejecutar el comando: 
    <b>py consumer.py</b> </li>
    <li>Abrir el navegador e ingresar en el campo de url el siguiente comando: <b>localhost:8000/docs</b> <li>
</ul>
<br>

<p>Ya en este punto puede ver las opciones de administración de la información.</p>
<br>

## Diagrama de flujo del modelo.

<br>
<img src='https://res.cloudinary.com/dojsvmsif/image/upload/v1657377868/Personal/flujo-python_mylamc.jpg' alt='diagrama'/>