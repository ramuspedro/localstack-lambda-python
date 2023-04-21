# localstack-lambda-python
Testing docker and localstack with python

```sh
# run localstack:
$ docker-compose up --build -d localstack
```

Teste open 
- http://localhost:4566/health on browser

```sh
# build image lambda python:
$ docker-compose build test-lambda

# run lambda
$ docker run -p 9000:8080 test-lambda:latest
```

To test run curl
```sh
$ curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

----

To test 

docker-compose up

aws --endpoint-url=http://localhost:4566 lambda create-function --function-name test-lambda --code ImageUri=test-lambda:latest --role arn:aws:iam::000000000000:role/lambda-role