#!/bin/bash


echo "Starting Restore Process..."

mongorestore --username "$MONGO_INITDB_ROOT_USERNAME" \
             --password "$MONGO_INITDB_ROOT_PASSWORD" \
             --authenticationDatabase admin \
             --archive=/atlas_data.archive.gz \
             --gzip

echo "Restore Complete!"