var ws = new WebSocket("ws://localhost:8001/")

ws.addEventListener("open", ev => {
  console.log("opened websocket ")
  while (true) {
	  const message = prompt("> ")
  	ws.send(`[client.js] ${message}`);
  }
})

ws.addEventListener("message", ev => {
  console.log("incoming message:  ", ev.data)
})

