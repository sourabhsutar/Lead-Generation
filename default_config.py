DEBUG = True
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/crm"
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
SECRET_KEY = "change-this-key-in-the-application-config"
JWT_SECRET_KEY = "change-this-key-to-something-different-in-the-application-config"
