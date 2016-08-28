
import paramiko
import tornado
import tornado.web
import pyrestful.rest
from pyrestful.rest import put, get, post ,delete
from pyrestful import mediatypes
from db import *




class AddhostHandle(tornado.web.RequestHandler):
    # def get(self, *args, **kwargs):
    #     self.render('func1.html')


    def post(self, *args, **kwargs):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("127.0.0.1", 22, "zzp", "zzp")
        stdin, stdout, stderr = ssh.exec_command("pwd")
        adhost=stdout.readlines()
        adhost2=db_operation('select id from user').select()
        print stdout.readlines()
        ssh.close()
        self.render('func1.html',adhost=adhost,adhost2=adhost2)


