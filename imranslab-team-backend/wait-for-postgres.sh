#!/bin/bash
until PGPASSWORD=$DATABASE_PASSWORD psql -h postgres-team-db -U postgres -c '\l'; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 2
done

# Start the Django app
python manage.py migrate
exec "$@"