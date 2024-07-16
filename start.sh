#!/bin/bash

export $(grep -v '^#' .env | xargs)

fuser -k -n tcp $PORT
cd $CWDIR

source $PYENV_DIR
exec nohup uwsgi -w index:app --logto app.log --http $HOST:$PORT > app.out &