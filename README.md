# Wine Prediction Model Deployment using FastAPI
***
This repository contains the code for deploying a machine learning model to predict wine quality using FastAPI. The model has been trained to evaluate wine based on various features and predict its quality. This guide will walk you through setting up, running, and interacting with the API.


### Features 
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
M- achine Learning Model: A pre-trained model that predicts wine quality based on input features.
- Docker Support: Dockerfile provided for containerized deployment.
- API Documentation: Auto-generated documentation available via Swagger UI.


### Requirements 
- Python 3.7+
- FastAPI: pip install fastapi
- Uvicorn: ASGI server implementation, pip install uvicorn
- Scikit-learn: For loading and using the pre-trained model, pip install scikit-learn
- Pandas & Numpy: For data handling, pip install pandas numpy


### Getting Started
- Clone the repo 
```
git clone git@github.com:toraaglobal/deploy-model-using-fastapi.git
cd deploy-model-using-fastapi
```

- Install requirements 
```
pip install -r requirements.txt
```

- Run the API 
```
uvicorn main:app --reload
```

The API will be accessible at http://127.0.0.1:8000.


###  Interact with the API
Once the server is running, you can access the interactive API documentation at:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

These interfaces allow you to test the API endpoints directly from your browser.


### API Endpoints
`POST /predict`

This endpoint predicts the quality of wine based on the input features.


**Request Body**

The request body should be a JSON object containing the following features:

```
fixed_acidity: float
volatile_acidity: float
citric_acid: float
residual_sugar: float
chlorides: float
free_sulfur_dioxide: float
total_sulfur_dioxide: float
density: float
pH: float
sulphates: float
alcohol: float
```

**Example**

```
{
    "fixed_acidity": 7.4,
    "volatile_acidity": 0.7,
    "citric_acid": 0.0,
    "residual_sugar": 1.9,
    "chlorides": 0.076,
    "free_sulfur_dioxide": 11.0,
    "total_sulfur_dioxide": 34.0,
    "density": 0.9978,
    "pH": 3.51,
    "sulphates": 0.56,
    "alcohol": 9.4
}

```

**Response**
The response will be a JSON object containing the predicted quality:

```
{
    "quality": 5
}


```


## Docker Deployment
A Dockerfile is provided to containerize the application for easy deployment.

-  Build the Docker Image
```
docker build -t wine-prediction-api .

```

- Run the Docker Container
```
docker run -d -p 8000:8000 wine-prediction-api

```

The API will now be accessible at http://localhost:8000.


## Model Training
If you want to retrain or update the model, you can do so by following these steps:

- Prepare the dataset: Use the wine quality dataset from a reliable source.
- Train the model: Using a tool like scikit-learn, train a model on the dataset.
- Save the model: Export the trained model as a .pkl file.
- Replace the existing model: Update the model file used in this project.



## Deployment on Railway
Railway is a platform that allows you to deploy applications with ease. Follow these steps to deploy the Toraaglobal website on Railway:

- Sign Up/Log In to Railway: If you don't already have an account, sign up at Railway.

- Create a New Project:

    - After logging in, click on "New Project" from the dashboard.
    - Select "Deploy from GitHub repo" and connect your GitHub account if you haven't done so already.
    - Choose the repository from your list of repositories.


- Deploy the Project:
    - Once everything is configured, click "Deploy" to start the deployment process.
    - After deployment, you can access your site via the domain provided by Railway, or you can set up a custom domain (e.g., www.toraaglobal.com).

- Monitor and Manage:
Railway provides logs and metrics to help you monitor the performance of your site. Use these tools to ensure everything is running smoothly.





