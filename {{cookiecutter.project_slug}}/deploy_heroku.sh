#!/bin/bash
set -e
set -u

# Configure
heroku config:set \
  MARKETPLACE_HOST="${MARKETPLACE_HOST}" \
  OAUTH2_CLIENT_ID="${CLIENT_ID}" \
  OAUTH2_CLIENT_SECRET="${CLIENT_SECRET}" \
  OAUTH2_REQUESTED_SCOPES="${SCOPES}" \
  FLASK_SECRET_KEY="${FLASK_SECRET_KEY}" \
  CALLBACK_URL="${APP_HOST}/callback"

# Push and build container
heroku container:push web
heroku container:release web
