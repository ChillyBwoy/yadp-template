#!/usr/bin/env bash

set -e

DB_USER="{{ project_name }}"
DB_NAME="{{ project_name }}"
DB_PASS=""

PROJECT_NAME="{{ project_name }}"
PROJECT_PATH="$(cd ../ | cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

VARDIR=$PROJECT_PATH/var
SOCKFILE=$VARDIR/server.sock
PIDFILE=$VARDIR/server.pid
    
export DJANGO_SETTINGS_MODULE="{{ project_name }}.settings.env.production"

test -d $VARDIR || mkdir -p $VARDIR

function cleanup {
    find $PROJECT_PATH/{{ project_name }} -name '*.pyc' -delete
}

function start {
    
    # workers = (2 x $num_cores) + 1

    cleanup
    gunicorn {{ project_name }}.wsgi:application \
                  --name=$PROJECT_NAME \
                  --bind=unix:$SOCKFILE \
                  --pythonpath=$PROJECT_PATH \
                  --workers=9 \
                  --user=www --group=www
    chmod 0666 $PROJECT_PATH/var/server.sock
}

function stop {
    if [ -f $PIDFILE ]; then
      kill `cat $PIDFILE`
      rm $PIDFILE
    else
      echo "No pid file was found. Skipping."
    fi
    
    if [ -f $SOCKFILE ]; then
      rm $SOCKFILE
    else
      echo "No socket file was found. Skipping."
    fi
}

function dumpsql {
    local path_sql="$PROJECT_PATH/db"
    local fname="$path_sql/$PROJECT_NAME-`date +%FT%H-%M`"

    if [ ! -d $path_sql ]; then
        mkdir -p "$path_sql"
    fi

    mysqldump -u $DB_USER -p$DB_PASS $DB_NAME | gzip > $fname.sql.gz
}

case $1 in
    start)
        echo "Starting"
        runfcgi
        ;;
    
    stop)
        echo "Stopping"
        stop
        ;;

    cleanup)
        echo "Cleaninig"
        cleanup
        ;;

    dumpsql)
        echo "Dumping data as SQL"
        dumpsql
        ;;

    restart)
        echo "Restarting"
        stop
        sleep 1
        start
        ;;
    *)
        echo "Usage: {start|stop|restart|dumpsql|cleanup}"
        exit 3
        ;;
esac
exit 0
