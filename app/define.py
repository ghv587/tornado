
from tornado.options import define, options


define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="auto", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="mysql", help="database password")
