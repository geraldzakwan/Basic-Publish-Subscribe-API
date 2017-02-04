# Basic-Publish-Subscribe-API

I wrote the solution in Python because recently Python is the programming language that I used most frequently. Python is very concise and I like it because I don't have to compile everytime I make changes.

I've got some assumptions for this problem :
1.  There would be two class, Publisher which can only publish and Subscriber which can only receive
2.  Register/Unregister a publisher to a topic -> It means that publisher can only publish notes which topic is already registered 
3.  The communication between publisher and subscriber can be established using socket. Each time the topics sent match the subscriber's filter, the subscriber will catch the message
4.  Each class has a list which save all the notes sent/received (I am currently not using any database)

Please correct me if I am wrong, I will try to fix my code if my assumptions are wrong. 

So, here's how I solve the problem :
1.  I use TCP for the communication protocol. Currently, I am still using localhost so the program would work only on two terminal in single computer. I'll try to add IP parameter later so I can test the program with two computers.
2.  In publisher, to test if a topic is registered, I used Python dictionary
3.  The message format is topic + space + note (string type). The message is sent using socket.send()
4.  In subscriber, I also used Python dictionary to register topic. Inside the dictionary there is a list to save all the notes. So this data structure is used to identify topic and to save the note received.
5.  Filter is set using ZeroMQ socket.setsockopt(). Only notes with subscribed topic will be received. 
6.  Before saving the notes, the notes should be converted to string first (notes received are still in bytes)

In the code, I used ZeroMQ/zmq package, mainly for the socket programming (I actually ever use ZeroMQ for college assignment, so that's why I prefer to work with this again). 

Dependencies :
zmq 0.0.0 (this the package I use)
pyzmq 16.0.2 (this is the requirement for zmq) 

I am trying to register my package (basicpublisher and basicsubscriber) to PyPI but I've got some problems. After I upload my package to PyPI, I try to install my own package using pip and it gives me this error : Could not find a version that satisfies the requirement basicpublisher (from versions: ) No matching distribution found for basicpublisher. This is the first time I upload my own package to PyPI. I'm currently working on this and hopefully it will be registered soon.
