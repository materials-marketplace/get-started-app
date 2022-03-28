set -e
set -u

mkdir -p secrets
echo -n $CLIENT_ID > secrets/client_id
echo -n $CLIENT_SECRET > secrets/client_secret
echo -n $SCOPES > secrets/scopes
echo -n $FLASK_SECRET_KEY > secrets/flask_secret
