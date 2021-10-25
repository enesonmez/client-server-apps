# Counter Client-Server Application

## Server 
* Keeps track of how many times it has been contacted 
* Returns that count in an ASCII string 

## Client 
* Establishes connection 
* Waits for message from server (ASCII string) 
* Prints data from message 

## Application-level protocol: 
* Syntax: 
    * No headers 
    * Client sends null message body 
    * Server message contains ASCII string 
* Semantics - Client establishes connection; server returns ASCII string 

## Program architecture
![](https://i.pinimg.com/originals/79/0d/6c/790d6c9680ae2ba82196f164b8393f27.jpg)