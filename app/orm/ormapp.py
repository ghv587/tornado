
from peewee import *

dbname = MySQLDatabase( 'auto',**{'host': 'localhost', 'password': 'mysql', 'port': 3306, 'user': 'root'})

class BaseModel(Model):
    class Meta:
        datebase = dbname

class Group(BaseModel):
    _id = PrimaryKeyField()
    order_up_day = IntegerField(null=True)
    order_up_hours = IntegerField(null=True)
    order_up_moon = IntegerField(null=True)
    order_up_quarter = IntegerField(null=True)
    order_up_week = IntegerField(null=True)
    order_up_year = IntegerField(null=True)
    tu_shopid = CharField(null=True)

    class Meta:
        db_table = 'group_master'


class SyShieldUser(BaseModel):
    _id = PrimaryKeyField()
    tu_account = CharField(null=True)
    tu_area = CharField(null=True)
    tu_city = CharField(null=True)
    tu_commence = DateField(null=True)
    tu_contract = DateField(null=True)
    tu_cost = IntegerField(null=True)
    tu_domain = CharField(null=True)
    tu_nick = CharField(null=True)
    tu_platform = CharField(null=True)
    tu_province = CharField(null=True)
    tu_realcost = IntegerField(null=True)
    tu_shopid = CharField(null=True)
    tu_version = CharField(null=True)

    class Meta:
        db_table = 'sy_shield_user'

dbname.connect()
Group.create_table()
SyShieldUser.create_table()
