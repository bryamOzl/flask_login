import secrets


class Config:
    # secret_key = secrets.token_urlsafe(32)
    # print(f"SECRET_KEY = '{secret_key}'")
    SECRET_KEY = 'sluVNkbCUiyf4QwOAF4vCQQxNBcSIC6vOppvPAcrrkY'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'pctel2023'
    MYSQL_DB = 'flask_login'


config = {
    'development': DevelopmentConfig
}
