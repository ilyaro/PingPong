# PingPong
The Docker Compose contain 2 containers, each listening on a different port on the host, but both implement the same API:

http://localhost:[port]/pingpong?iterations=[integer]&timeout=[integer]&pongsleep=[integer]

Example: http://localhost:8001/pingpong?iterations=10&timeout=70&pongsleep=2

timeout and pongsleep in miliseconds only!
The Game takes aproximately 60 miliseconds on https://labs.play-with-docker.com

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

Run this URL (Click on 8001 or 8002 link)
![alt text](https://user-images.githubusercontent.com/40502115/97773120-cff45b00-1b55-11eb-8b19-f399844a5406.png)

The Game results in Browser
![alt text](https://user-images.githubusercontent.com/40502115/97773511-0384b480-1b59-11eb-932c-573f08751031.png)

The Game results in Docker Compose STDOUT
![alt text](https://user-images.githubusercontent.com/40502115/97773453-6f1a5200-1b58-11eb-8ce4-1f8c1a889415.png)
