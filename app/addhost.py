
import paramiko
import tornado
import tornado.web



class AddhostHandle(tornado.web.RequestHandler):
    # def get(self, *args, **kwargs):
    #     self.render('func1.html')


    def post(self, *args, **kwargs):
        ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("127.0.0.1", 22, "zzp", "zzp")
        stdin, stdout, stderr = ssh.exec_command("pwd")
        adhost=stdout.readlines()
        # print stdout.readlines()
        ssh.close()
        self.render('func1.html',adhost=adhost)
