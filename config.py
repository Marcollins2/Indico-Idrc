# Basic Indico Config File

# Mail settings to route through Maildump
MAIL_DEFAULT_SENDER = 'noreply@localhost'
MAIL_SERVER = 'localhost'
MAIL_PORT = 1025  # Default port for Maildump
MAIL_USE_TLS = False

# Add any other necessary configurations here (e.g., database settings, logging, etc.)


SQLALCHEMY_DATABASE_URI = 'postgresql://$collin@localhost/indico'
SQLALCHEMY_TRACK_MODIFICATIONS = False
