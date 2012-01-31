SANDBOX:
--------

DISCRIPTION:
------------
THE PROGRAM HAS TWO PARTS :
	The Server:-Provides the services.[list,pwd ,rm,touch,time].
	Start the server and get a connection.Do a hand shake.
	The server is running.When a new data comes in if it is 'close' it shutsdown
    else it passes the value as argument to handle_option().
	The function takes the data and performes the action and returns some result.
	the touch command alone has the ability to execute its last
    parameter if it starts with '$' symbol.
	
	The Client:-Client program .It has two threads.
	  1. the main thread itself,through which you can request for verious services.
	  2. A secondary thread ,which becomes active every 1min to create a file with a
      random name and server time as content.Dies when the main thread is no longer alive
	Two global variables some_one,main_alive are used to sinc both the threads.

DEPENDANCIES:
-------------
	python-2.7

USAGE:
------
	Start 		tcp_server.py 		first
	start 		client.py 			later in  a seperate console.
	type 'close' to exit any time or 'help' to get a list of possible commands.
	all inputs are on the client side only.
	