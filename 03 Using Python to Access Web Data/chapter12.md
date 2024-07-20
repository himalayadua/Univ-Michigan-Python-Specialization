# Network Programs
TCP
- handles flow control using a transmit window
- provides a nice reliable pipe
- python code to talk to transport layer
- using sockets
    - intent to talk to an app
    - using name and number
    - different apps listening on different ports

![Ports are like extension numbers](./assets/ports.png)

### Sockets in Python
TCP Sockets
- an endpoint for communication between two devices over a network
- Each socket is identified by an IP address and a port number (e.g., `192.168.1.1:80`)

```Python
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("google.com", 80))
                        #host        #port
```

Once the socket is created:
- this moves us from Transport layer to Application layer
- what we say on a phone call first
    - hello
    - gets the conversation started
- this is similar to the protocol
    - HTTP
- URL (Uniform resource locator)
    - contains information
    - protocol
    - host
    - document

Anytime you click on a link:
- you are asking the web browser to `GET` something
- it's a GET request
    - get some content from the URL
- 

```python

```


```python

```


```python

```


```python

```


```python

```

