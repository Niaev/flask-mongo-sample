"""General configurations and environment variables"""

# General imports
import os

# Environment variables stuff
from dotenv import load_dotenv
load_dotenv()

env = os.getenv

# Server stuff
PROTOCOL=env('PROTOCOL')
HOST=env('HOST')
PORT=env('PORT')

# Project root folder
CWDIR=env('CWDIR')

# Development stuff
DEBUG=bool(env('DEBUG'))

# MongoDB Stuff
MONGO_HOST=env('MONGO_HOST')
MONGO_PORT=env('MONGO_PORT')
MONGO_DB=env('MONGO_DB')
MONGO_COLLECTION1=env('MONGO_COLLECTION1')
MONGO_COLLECTION2=env('MONGO_COLLECTION2')