#!/bin/bash

DBNAME=$1
USER=$2
OUTPUT_FILE=${3:-output.txt}

exec > $OUTPUT_FILE

if [[ -z "$DBNAME" || -z "$USER" ]]; then
    echo "Usage: $0 dbname username"
    exit 1
fi

TABLES=$(psql -U $USER -d $DBNAME -t -c "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

for TABLE in $TABLES; do
    echo "Table: $TABLE"
    psql -U $USER -d $DBNAME -t -c "SELECT column_name || ' | ' || data_type FROM information_schema.columns WHERE table_name = '$TABLE'"
    echo
done
