#!/usr/bin/python
import xmlrpc.client

user="root"
passwd="0fw0rk"
s = xmlrpc.client.ServerProxy("https://" + user + ":" + passwd + "@localhost:8080/xmlrpc")
print("=============== Root's view ================")
print(s.api.ping("Joe mama"))
for x in  s.api.listFlowSpace():
    print(x)

user="alice"
passwd="alicePass"
s = xmlrpc.client.ServerProxy("https://" + user + ":" + passwd + "@localhost:8080/xmlrpc")
print("=============== Alice's view ================")
print(s.api.ping("Joe mama"))
for x in  s.api.listFlowSpace():
    print(x)
print(s.api.getDevices())
#print(s.api.change_passwd("alice","foo"))
user="bob"
passwd="bobPass"
s = xmlrpc.client.ServerProxy("https://" + user + ":" + passwd + "@localhost:8080/xmlrpc")
print("=============== Bob's view ================")
print(s.api.ping("Joe mama"))
for x in  s.api.listFlowSpace():
    print(x)
#print(s.api.changePasswd("alice","foo"))

#### FIXME
#print("=============== available methods ============")
# print(list of available methods)
#print(s.system.listMethods())
