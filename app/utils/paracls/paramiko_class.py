import paramiko
import ConfigParser




client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def paramiko_exec(cmd):
    try:
        conf = ConfigParser.ConfigParser()
        conf.read("../config/config.ini")
        host = conf.get("section1", "host")
        user = conf.get("section1", "user")
        passwd = conf.get("section1", "passwd")
        client.connect(hostname='host', username='user', password='passwd')
        client.exec_command('cmd')
    except Exception,e:
        print e
    finally:
        client.close()



# stdin, stdout, stderr = client.exec_command('ls')
# for line in stdout:
#     print '... ' + line.strip('\n')
# client.close()