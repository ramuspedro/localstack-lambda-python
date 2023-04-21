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
https://www.linkedin.com/pulse/testando-e-debugando-fun%C3%A7%C3%B5es-lambda-em-python-localmente-gleyton-lima/?originalSubdomain=pt

docker-compose up localstack


Enter on folder lambdas/python/src

aws lambda create-function \
    --endpoint=http://localhost:4566 \
    --function-name minha-funcao \
    --runtime python3.8 \
    --zip-file fileb://handler.zip \
    --handler handler.handle \
    --role arn:aws:iam::000000000000:role/lambda-role

List function 
aws lambda list-functions \
    --endpoint=http://localhost:4566

aws lambda invoke \
    --endpoint=http://localhost:4566 \
    --function-name minha-funcao \
    --payload fileb://event.json \
    response.json

-- Próximos passos
Criar um pacote com a lambda incluindo requirements