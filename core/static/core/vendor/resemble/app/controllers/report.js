'use strict'

var Report = require('../models/report');

var ResCompare = require('./resemble-compare');

const compare = require("resemblejs").compare;

var https1 = require('https');

var fs = require('fs');

var fs2 = require("mz/fs");

var Minio = require('minio');

const { endpoint, accesskey, secretkey } = require('../../config');

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
    report.idExec1 = params.idExec1;
    report.image2 = params.image2;
    report.idImg2 = params.idImg2;
    report.idExec2 = params.idExec2;
    console.log('parametros: ', params.image1, params.image2, params.idImg1, params.idImg2);
    let name = report.idExec1 + '_' + report.idImg1 + '_' + report.idExec2 + '_' + report.idImg2 + '_' + new Date().getTime() + '.png';
    console.log('este es el nombre: ' + name);
    let pathDownloads = 'app/uploads/downloads/';
    let pathConverted = 'app/uploads/reports/';
    //download(report.image1, pathDownloads + 'a_' + nameUrlFile(report.image1), {});
    //download(report.image2, pathDownloads + 'b_' + nameUrlFile(report.image2), {});

    var s3Client = new Minio.Client({
        endPoint:  'URL_AMAZON',
        accessKey: 'KEY',
        secretKey: 'SECRET'
    });

    const options = {
        output: {
            errorColor: {
                red: 255,
                green: 0,
                blue: 255
            },
            errorType: "movement",
            transparency: 0.4,
            largeImageThreshold: 1200,
            useCrossOrigin: false,
            outputDiff: true
        },
        scaleToSameSize: true,
        ignore: "antialiasing"

    };

    var metaData = {
        "x-amz-acl": "public-read"
    }

    let image1 = 'steps/'+ report.idExec1 + '/' + nameUrlFile(report.image1);
    let image2 = 'steps/'+ report.idExec2 + '/' + nameUrlFile(report.image2);
    let imageDiff = pathConverted + name;
    var size = 0;
    console.log(image1);
    console.log(image2);
    s3Client.fGetObject('tsdc-automation.media',  image1, 'app/uploads/downloads/a_' + nameUrlFile(report.image1), function(err) {
        if (err) {
            console.log('error descarga 1: ', err);
            return res.status(500).send({ message: 'fail' });
        }
        s3Client.fGetObject('tsdc-automation.media', image2, 'app/uploads/downloads/b_' + nameUrlFile(report.image2), function(err) {
            if (err) {
                console.log('error descarga 2: ', err);
                return res.status(500).send({ message: 'fail' });
            }
            console.log('success');
            //ResCompare.getDiff(pathDownloads + 'a_' + nameUrlFile(report.image1), pathDownloads + 'b_' + nameUrlFile(report.image2), imageDiff);


            compare(pathDownloads + 'a_' + nameUrlFile(report.image1), pathDownloads + 'b_' + nameUrlFile(report.image2), options, function(err, data) {
                if (err) {
                    console.log('error compare: ', err);
                } else {
                    console.log(data);
                    fs2.writeFile(imageDiff, data.getBuffer());

                    var fileStream = fs.createReadStream(imageDiff)
                    var fileStat = fs.stat(imageDiff, function(err, stats) {
                        if (err) {
                            console.log('error en el stream de archivo: ', err)
                            return res.status(500).send({ message: 'fail' });
                        }
                        s3Client.putObject('tsdc-automation.media', 'vrt/' + name, fileStream, metaData, function(err, etag) {
                            fileStream.destroy();
                            if(err){
                                console.log('error en la subida: ', err, etag) // err should be null
                                return res.status(500).send({ message: 'fail' });
                            }else
                            {
                                report.imageDiff = 'https://s3.us-east-2.amazonaws.com/tsdc-automation.media/vrt/' + name;
                                return res.status(200).send({ report: report,
                                    data: JSON.stringify(data)});
                            }
                       });
                    });

                }
            });

        })
    })

    //var data = getDiff('a_' + nameUrlFile(report.image1), 'b_' + nameUrlFile(report.image2), pathDownloads, pathConverted, name);
    //setTimeout(function() {
    //    ResCompare.getDiff(pathDownloads + 'a_' + nameUrlFile(report.image1), pathDownloads + 'b_' + nameUrlFile(report.image2), pathConverted + name);
     //   //console.log(data);
     //   report.imageDiff = name;
      //  return res.status(200).send({ report: report });
    //}, 3000);
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

