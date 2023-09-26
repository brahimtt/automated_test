import os
  
configs = {
    'development': '.config.settings.DevConfig',
    'testing': '.config.settings.TestingConfig',
    'production': '.config.settings.ProdConfig'
}

class Config():
    pass

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_DATABASE", os.path.join("/home/winnyskill/backend/db.sqlite3")),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}
AUTH_USER_MODEL = "api_user.User"
