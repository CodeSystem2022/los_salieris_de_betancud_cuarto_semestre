const fs = require('fs')

// Primero leemos archivo.txt
function leer(ruta, cb) {
    fs.readFile(ruta, (err, data) => {
        cb(data.toString());
    })
}

// Segundo escribimos el archivo1.txt creandolo
function escribir(ruta, contenido, cd) {
    fs.writeFile(ruta, contenido, (err) => {
        if (err) {
            cd('No se ha podido escribir', err);
        } else {
            cd('Se ha escrito correctamente');
        }
    })
}

// Tercero eliminamos el archivo1.txt
function borrar(ruta, cb) {
    fs.unlink(ruta, cb)
}


// leer(`${__dirname}/archivo.txt`, console.log) // Sintaxis ES6
// escribir(`${__dirname}/archivo1.txt`, 'Reescribimos el archivo', console.log)
// leer(`${__dirname}/archivo1.txt`, console.log) // Sintaxis ES6
borrar(`${__dirname}/archivo1.txt`, console.log)