const path = require('path');
const {spawn} = require('child_process');
var express = require("express");
const app = express();

app.use("", express.static(__dirname));

app.get('./json/data.json', function(req, res) {
    res.sendFile(__dirname + './json/data.json');
});

app.get('../src/videoToFrames.py', function(req, res) {
    res.sendFile('../src/videoToFrames.py');
});

//flask --> alternative to nodejs
//xmlhttprequest --> asynchronous requests


// function runVidToFrames(){
// 	return spawn('python', [
// 		"-u",
// 		path.join(__dirname, '../src/videoToFrames.py')
// 	]);
// }

// const subprocess = runVidToFrames()

// subprocess.stdout.on('data', (data) => {
//    console.log(`data:${data}`);
// });


var PORT = 8080;
app.listen(PORT, function() {
    console.log("Listening on port " + PORT);
});