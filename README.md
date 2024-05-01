# Fibonaci Experience

Creates a website which can calculate fibonacci values.

![image](https://github.com/mustardjelly/fib/assets/32181718/12b14078-ed62-4691-8cc2-caa1deba1f22)


## To install

I have included poetry and requirement.txt installation files allowing for a
wide range of package management support.

My recommendation is to use poetry to handle package management.

```bash
cd ./fib
```

### poetry

```bash
poetry install

# Dev
poetry install --with dev
```

### pip

```bash
python3 -m pip install -r requirements.txt
```

## To run

Simply run app.py in your favourite environment after installing the required
dependencies.

```bash
poetry run app.py
```
Then visit http://127.0.0.1:5000

## To test

To test run 
```bash
cd ./fib
pytest tests/
```

## Deployment

Suggested deployment depends on scale of requests.

### Light Traffic

For simple deployments, use docker running on a single webhosted instance routing
traffic to 127.0.0.1:5000. This provides isolation to the running server.

Containers can be pulled to the server or pushed via CI/CD tooling.

Server would be vulnerable to outages unless load balancing
applied.

### Large Requests

For larger scale deployments we should consider a distributed network hosting
the application. Latency is not a large consideration so hosting in cheaper 
cloud servers would be a good way to save costs.

Servers should be deployed and maintained using Kubernetes or similar 
technology.

Request scaling should pass through an application gateway capable of load
balancing traffic to servers.

Servers can be upgraded individually allowing for high availability.

## CI/CD

A build platform such as Github Actions, or CircleCI should be used to run 
tests, create packages, and deploy to environments.

### Testing

Containers can be deployed to environments in build pipelines to run
integration and unittests.

UI Automation can be tested by deploying the application and using a framework
such as selenium to automate interations with the application.

Postman or a similar API testing framework should be used to verify integrity
of APIs.

## Logging

Logging can be handled by using a generic log class which is capable of routing
to many sources. The best log is a log that is read. This allows for quick
routing of logs to different sources.

Additionally we can inject loggers which are more PII aware by ensuring all log
messaging goes through the same logging logic.

I would recommend developing both a logger and a standard log formatter such as
`logfmt` which is compatible with platforms such as Grafana and allows for 
effective and scalable querying of log data.

## Monitoring

Grafana can be used to monitor servers. It can be configuired to alert on
specific metrics.

Monitoring logs for issues with intelligent group of exceptions will enable a
rich error handling environment.
