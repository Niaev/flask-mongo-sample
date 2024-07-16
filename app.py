# Project imports
from index import app as application

# Environment variables
from config import *

if __name__ == '__main__':
    application.run(
        debug=DEBUG
    )