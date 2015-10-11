import socket
import time
import sys
from subprocess import call
from PyQt4 import QtCore,QtGui

passwords={}
cfg=[]

class Mapping:
    def __init__(self,pattern,drive,path,user,passwordName):
        self.pattern=pattern
        self.drive=drive
        self.path=path
        self.user=user
        self.passwordName=passwordName

def getip():
    return socket.gethostbyname(socket.gethostname())
    
def unmount(drive):
    call(['net','use',drive,'/DELETE'])
    
def mount(drive,share,user='',password=''):
    args=['net','use',drive,share]
    if len(password)>0:
        args+=[password]
    if len(user)>0:
        args+=['/USER:{}'.format(user)]
    args+=['/PERSISTENT:NO']
    print ' '.join(args)
    call(args)
    
def getPassword(name):
    if name in passwords:
        return passwords.get(name)
    pname=name.replace('_',' ')
    res=QtGui.QInputDialog.getText(None,'Password',pname,QtGui.QLineEdit.Password)
    if res[1]:
        password=str(res[0])
        passwords[name]=password
        return password
    return ''
    
def updateMounts(ip):
    for c in cfg:
        if ip.find(c.pattern)>=0:
            password=''
            if len(c.passwordName)>0:
                password=getPassword(c.passwordName)
            mount(c.drive,c.path,c.user,password)
        else:
            unmount(c.drive)

def readConfig(filename):
    global cfg
    cfg=[]
    try:
        for line in open(filename,'r').readlines():
            parts=line.strip().split()
            if len(parts)>=3:
                user=''
                passwordName=''
                if len(parts)>=5:
                    user=parts[3]
                    passwordName=parts[4]
                cfg.append(Mapping(parts[0],parts[1],parts[2],user,passwordName))
    except IOError:
        print "Cannot read configuration file"

def main():
    app=QtGui.QApplication(sys.argv)
    lastip=''
    if len(sys.argv)>1:
        readConfig(sys.argv[1])
    while True:
        ip=getip()
        if ip!=lastip:
            lastip=ip
            updateMounts(ip)
        time.sleep(5)

if __name__=='__main__':
    main()
