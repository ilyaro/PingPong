# PingPong
The Docker Compose contain 2 containers, each listening on a different port on the host, but both implement the same API:

http://localhost:[port]/pingpong?iterations=[integer]

When the container gets the request, it starts playing ping pong with the other container by sending it an HTTP request
and receiving a response. Each request/response is a single iteration, and the number of iterations to play is determined
by the parameter of the pingpong request.


# How to run Docker Compose
Login to the machine (Tested on https://labs.play-with-docker.com)

[node1] (local) root@192.168.0.18 ~git clone https://github.com/ilyaro/PingPong.git

[node1] (local) root@192.168.0.18 ~
$ cd PingPong/

[node1] (local) root@192.168.0.18 ~/PingPong
$ docker-compose up --build

