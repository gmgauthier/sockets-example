# sockets-example

This project is just me trying to remediate myself on more advanced python topics. There are a few variant iterations of this example floating around the internet. But my example is unique for three reasons:

1. I bundle the server and client into proper classes. Most people just give you the "more pythonic" flat method technique. I think this is questionable.
2. I provide a runner that handles everything. Starts the server, starts the client, passes messages between them, and logs it all to the console.
3. I use multiprocessing to be able to start the server and run the client in the same demo script. 

