# Echo Client-Server Application

### Content
The server simply echo whatever it receives back to the client.

* Chose an application number  between 1 to 32767 that is not being used by any other applications,
* Specify the number as a command line argument.
* The sever is invoked by the command:
```bash
$ python echoserver.py 20000
```
* In some other application is using number 20000, the server emits an appropriate error message and exist, the user must chose another number.
* A user on an arbitrary computer contact to the sever: 
```bash
$ python echoclient.py localhost 20000
```
