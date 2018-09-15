#/usr/bin/env bash -e

VENV=venv

if [ ! -d "$VENV" ]
then

    PYTHON=`which python2`

    if [ ! -f $PYTHON ]
    then
        echo "could not find python"
    fi
    virtualenv --system-site-packages -p $PYTHON $VENV

fi

. $VENV/bin/activate

sudo pip install --no-deps -I -r requirements.txt
