var fs = require('fs');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var path = require('path');
var json_beautify = require('json-beautify');

// app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


var router = express.Router();
var catalog_in_memory;
var catalog_updated = false;
var path_to_catalog = './catalog.json';

var loadCatalog = function(){
    if (catalog_in_memory != undefined  && !catalog_updated){
        return catalog_in_memory;
    }

    catalog_in_memory = JSON.parse(fs.readFileSync(path_to_catalog));
    catalog_updated = false;
    //write catalog to disk
    fs.writeFileSync(path_to_catalog, JSON.stringify(catalog_in_memory));

    return catalog_in_memory;
}

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
        var new_catalog = JSON.parse(content);
        console.log('Received: ' + JSON.stringify(new_catalog));

        //merge with the previous catalog
        var prev_catalog = loadCatalog();
        prev_catalog.Peers[new_catalog.id] = new_catalog["files"];
        console.log("Modified catalog = " +JSON.stringify(prev_catalog));

        res.send(json_beautify(prev_catalog, null, 4, 100));
    });


});



app.use('/', router);

app.listen(12345);
console.log('Connect on 12345');
