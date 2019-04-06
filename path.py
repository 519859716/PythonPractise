import sys
import os

#path = os.path.normpath("C:/pa/a/a")
#path1 = os.path.normpath(os.path.join(os.path.abspath(__file__)))
#path2 = os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir))
#path3 = os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir,os.pardir))
#path4 = os.path.join(os.path.abspath(__file__),os.pardir,os.pardir)
#path5 = os.pardir
#path6 = os.path.join("1","2",os.path.curdir)
#print "path",path
#print "path1",path1
#print "path2",path2
#print "path3",path3
#print "path4",path4
#print "path5",path5
#print "path6",path6


print os.environ

env =os.environ

print env.get("USERPROFILE")

