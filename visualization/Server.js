var express = require("express");
const app = express();

app.use("", express.static(__dirname));

app.get('/data.json', function(req, res) {
    res.sendFile(__dirname + '/data.json');
});


var PORT = 8080;
app.listen(PORT, function() {
    console.log("Listening on port " + PORT);
});