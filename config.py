class Config(object):
    """ Common configurations """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """ Development configurations """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}: {DB_PASS}@{DB_ADDR}/{DB_NAME}" \
        .format(DB_USER="postgres", DB_PASS="", DB_ADDR="127.0.0.1", DB_NAME="dream_team")


class ProductionConfig(Config):
    """ Production configurations """

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """ Testing configurations """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
