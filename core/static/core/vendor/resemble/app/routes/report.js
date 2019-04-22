'use strict'

var express = require('express');

var ReportController = require('../controllers/report');

var api = express.Router();

api.get('/home', ReportController.home);
api.post('/compare-images/', ReportController.compareImgs);

module.exports = api;