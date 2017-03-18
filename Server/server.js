var fs = require('fs');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var path = require('path');

// app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


var router = express.Router();

router.use(function(req, res, next){
    console.log('Router working.. ');
    next();
});

router.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/HtmlPages/index.html'));
});

router.post('/peers', function(req, res){
    var content = '';
    req.on('data', function(data){
        content += data;
    });

    req.on('end', function(){
        var data = JSON.parse(content);
        console.log('Received: ' + JSON.stringify(data));
    });

    console.log(res.body);
    res.send(req.body);
});



app.use('/', router);

app.listen(12345);
console.log('Connect on 12345');
