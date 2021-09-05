class Dev(object):
    ENV = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@47.98.161.129/edu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
