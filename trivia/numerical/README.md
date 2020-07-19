## The Machine Learning Workflow
At least in an abstract sense the machine learning workflow looks something like

```
data prep -> training model -> model depolyment -> deploy and scale
```

### Data Prep
In Python Data Prep is done with 
- Pandas
- Matplotlib
- PySpark
In addition to some SQL

### Model Training
In Python training a model will depend on the approach

For machine learning
- sklearn
- xgboost

For deep learning
- Some deep learning framework (pytorch, tensorflow, mxnet etc...)

### Model Deployment
In either case at scale a model needs to be "query-able", which generally meants you expose some route which takes a POST request (either an image or some text), and returns whatever the model is supposed to respond with

eg.
```
[cat.jpg] -> route -> {"labels" : "cat, orange, fuzzy, stripes", "scores": ".99, .97, .8, .76"}
```

## Scalability
Now that application needs to scale with the number of requests which are being submitted at any given point in time.

## Production Solutions
There are a bunch of ways to approach this problem
- Render
- Google App Engine
- AWS Lambda
- Amazon SageMaker
- AWS Elastic Beanstalk
- Microsoft Azure Functions
- Docker and Kubernetes
(all discussed in more detail under *Prod Solutions*)

### References
- https://www.youtube.com/watch?v=EkELQw9tdWE
- https://course.fast.ai/deployment_amzn_sagemaker.html