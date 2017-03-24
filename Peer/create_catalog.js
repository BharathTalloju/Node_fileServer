var fs = require('fs');
var merge_json = require('merge-json');
var json_beautify = require("json-beautify");
var ip = require("ip");

var shared_dir_path = './sharedFolder';
var catalog = null;
var log_file_path = './create_catalog.log';
var catalog_file_path = './catalog.json';
var log_message = '';


var read_sharedFolder = function(){
	var files = fs.readdirSync(shared_dir_path);
	log_message = '\nRead Files: ';
	for (var i in files){
		log_message += '\n\t'+String(i)+'. ' +files[i];
	}

	fs.appendFileSync(log_file_path, log_message);
	for(var i in files){

		var stats = fs.statSync(shared_dir_path+'/'+files[i]);

		if(! stats.isFile()){
			continue;
		}

		var new_file = JSON.parse('\
		{\
			"name": "'+ files[i] +'",\
			"size": '+ stats["size"] +'\
		}\
		');

		catalog.files.push(new_file);
	}

	console.log(json_beautify(catalog, null, 4, 100));

//	if(fs.existsSync(catalog_file_path)){
//		var prev_catalog = JSON.parse( fs.readFileSync(catalog_file_path) );
//		catalog = merge_json.merge(prev_catalog, catalog);
//	}

	fs.writeFileSync(catalog_file_path, json_beautify(catalog, null, 4, 100));

};

var create_catalog = function(add){
	catalog = JSON.parse('{\
		"id": "'+add+'",\
		"files": []\
	}');

	read_sharedFolder();
};

create_catalog(ip.address())

var print_file_stats = function(stats){
	console.log('\t\tSize: '+(stats.size/1000) + 'KB');
};

var stat_files = function(err, files){
	console.log("Files: ");

	for(var i in files){
		console.log('\n\t'+files[i]+':');

		//Get details of each file
		print_file_stats( fs.statSync(shared_dir_path+'/'+files[i]) );
	}
};
