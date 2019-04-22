'use strict'

var Report = require('../models/report');

var ResCompare = require('./resemble-compare');

var https1 = require('https');

var fs = require('fs');


function home(req, res) {
    res.status(200).send({
        message: 'Hola mundo desde el servidor de NodeJS'
    });
}

function nameFile(file) {
    var filePath = file.path;
    var fileSplit = filePath.split(/[\\/]/);
    var fileName = fileSplit.pop();
    return fileName;
}

function nameUrlFile(file) {
    var fileSplit = file.split(/[\\/]/);
    var fileName = fileSplit.pop();
    return fileName;
}

// Registro de reporte
function compareImgs(req, res) {
    var params = req.body;
    var report = Report;
    report.image1 = params.image1;
    report.idImg1 = params.idImg1;
    report.image2 = params.image2;
    report.idImg2 = params.idImg2;
    let name = report.idImg1 + '_' + report.idImg2 + '_' + new Date().getTime() + '.jpg';
    console.log('este es el nombre: ' + name);
    let pathDownlodas = 'app/uploads/downloads/';
    let pathConverted = 'app/uploads/reports/';
    download(report.image1, pathDownlodas + 'a_' + nameUrlFile(report.image1), {});
    download(report.image2, pathDownlodas + 'b_' + nameUrlFile(report.image2), {});
    //var data = getDiff('a_' + nameUrlFile(report.image1), 'b_' + nameUrlFile(report.image2), pathDownlodas, pathConverted, name);
    setTimeout(function() {
        ResCompare.getDiff(pathDownlodas + 'a_' + nameUrlFile(report.image1), pathDownlodas + 'b_' + nameUrlFile(report.image2), pathConverted + name)
    }, 1000);

    //console.log(data);
    report.imageDiff = name;

    return res.status(200).send({ report: report });
}

var download = function(url, dest, cb) {
    var file = fs.createWriteStream(dest);
    var request = https1.get(url, function(response) {
        response.pipe(file);
        file.on('finish', function() {
            file.close();
        });
    });
}

module.exports = {
    home,
    compareImgs
}