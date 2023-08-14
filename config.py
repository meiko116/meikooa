
SECRET_KEY='sfafasfa,fe'


# 数据库的配置信息
# MySQL所在的主机名
HOSTNAME = '192.168.31.90'
# MySQL监听的端口号，默认3306
PORT = 3306
# 连接MySQL的用户名，读者用自己设置的
USERNAME = 'root'
# 连接MySQL的密码，读者用自己的
PASSWORD = '123456'
# MySQL上创建的数据库名称
DATABASE = 'meikooa'

DB_URI= f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = ""
# lbyswnlnmcmubbed
