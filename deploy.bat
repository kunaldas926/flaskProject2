@ECHO OFF
serverless plugin install -n serverless-wsgi
serverless plugin install -n serverless-python-requirements
serverless deploy
PAUSE