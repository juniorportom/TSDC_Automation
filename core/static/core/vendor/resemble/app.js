'use strict'

var express = require('express');
var bodyParser = require('body-parser');

var app = express();

// cargar rutas

var reportRoutes = require('./app/routes/report');

//middlewares
app.use(express.static(__dirname = './app'));

app.get('/contacts', function(req, res) {
    console.log('I receive a Get request');
    var contacts = [
        { name: 'Reinaldo', email: 'prueba@correo.com', number: '(111) 111-1111' },
        { name: 'Junior', email: 'prueba2@correo.com', number: '(222) 222-2222' },
        { name: 'Jhon', email: 'prueba3@correo.com', number: '(333) 333-3333' }
    ];

    res.json(contacts);
});


app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

//cors
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Authorization, X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Allow-Request-Method');
    res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
    res.header('Allow', 'GET, POST, OPTIONS, PUT, DELETE');

    next();
});

//rutas
app.use('/', reportRoutes);
//exportar
module.exports = app;