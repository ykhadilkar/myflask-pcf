# Flask App for Pivotal Cloud Foundry

## To run locally
```bash
source venv/bin/activate
FLASK_APP=app.py flask run
```

## Test
```bash
http http://127.0.0.1:5000/ //should return "Hello, World!"

http http://127.0.0.1:5000/foo/123
```

## To run on PCF
```bash
cf push
```