var io = require('socket.io').listen(8000);

io.sockets.on('connection', function (socket) {
	socket.emit("connection_succeed", 'Connection succeed');

	socket.on("message", function (data) {
	   console.log(data); 
	   console.log("message received")
	   socket.emit('identification_query', 'who are you ?');
	}); 

	socket.on("identification", function (data) {
	   console.log(data); 
	   console.log("Thank you sir")
	}); 

	socket.on('status', function(data) {
		console.log("New status : "+data)
		socket.emit('watering', 5)
	});

	// setTimeout(function () {
	// 	socket.emit('watering', 5)
	// }, 2000);
	
});