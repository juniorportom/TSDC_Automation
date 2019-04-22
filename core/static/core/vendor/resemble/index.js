'use strict'
var app = require('./app');
var port = 8080;

//Crear servidor
app.listen(port, () => {
    console.log('Servidor corriendo en http://localhost:' + port);
});

