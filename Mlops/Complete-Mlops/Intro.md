# MLOps Learning Journey

This repository will document my learning journey in MLOps, starting from the foundational concepts outlined in the provided MLOps introduction.

## Introduction to MLOps

[cite_start]MLOps emphasizes an Agile process  [cite_start]for data science projects, incorporating modularity, YAML configurations, pipelines, and GitHub Actions. Key tools and concepts include:

* [cite_start]**DVC (Data Version Control)** 
* [cite_start]**MLflow**  (for experiment tracking, model creation, and deployment)
* [cite_start]**Schedulers** like Apache Airflow 
* [cite_start]**Docker** 
* [cite_start]**AWS** [cite: 1, 2] [cite_start](and other cloud platforms like Azure )
* [cite_start]**GitHub Actions** 
* [cite_start]**Amazon SageMaker** 

## Life Cycle of a Data Science Project (MLOps Perspective)

The data science project life cycle, under an MLOps lens, involves several key stages:

### 1. Requirements Gathering

* [cite_start]Involves Data Analysts/Data Scientists, Domain Expertise/Product Owners, and Business Analysts.
* [cite_start]Follows an Agile approach with "Requirements Sprints".

### 2. Data Pipeline & Ingestion

* [cite_start]**Identify the Data:** Data can come from Cloud, 3rd party APIs, IOT, FTL Pipeline, or MongoDB.
* [cite_start]**Data Ingestion:** Reading from data sources such as Cloud, S3, MongoDB, or PostgreSQL.
* [cite_start]Tools like Apache Airflow [cite: 1] [cite_start](and Astronomer  for Airflow) are crucial for building robust data pipelines.

### 3. Feature Engineering

[cite_start]This stage focuses on preparing the data for model training:

* [cite_start]Exploratory Data Analysis 
* [cite_start]Handling Missing Values 
* [cite_start]Handling Outliers 
* [cite_start]Categorical Encoding 
* [cite_start]Normalization & Standardization 

### 4. Feature Selection

[cite_start]Techniques to select the most relevant features for the model:

* [cite_start]Correlation 
* [cite_start]Forward Elimination 
* [cite_start]Backward Elimination 
* [cite_start]Univariate Selection 
* [cite_start]RandomForest Importance 
* [cite_start]Feature Selection With Decision Trees 

### 5. Model Creation & Hyperparameter Tuning

[cite_start]This involves building and optimizing machine learning models:

* [cite_start]GridSearchCV 
* [cite_start]RandomizedSearchCV 
* [cite_start]Keras Tuner 
* [cite_start]Bayesian Optimization (Hyperopt) 
* [cite_start]Genetic Algorithms 
* [cite_start]Optuna 

### 6. Model Deployment

[cite_start]Once a model is trained and optimized, it needs to be deployed. This often involves:

* [cite_start]GitHub Repository for code tracking 
* [cite_start]Cloud platforms (AWS, Azure, Heroku) 
* [cite_start]DAGsHub 
* [cite_start]DVC 

### 7. Model Monitoring & Retraining

[cite_start]Continuous monitoring and retraining are critical for maintaining model performance in production.

* [cite_start]**Experiment Tracking:** MLflow  [cite_start]and Grafana  [cite_start]are mentioned for visualization and monitoring.

## Key MLOps Tools & Technologies

Throughout the MLOps lifecycle, various tools and technologies are utilized:

* [cite_start]**Agile Process** 
* [cite_start]**Modular, YAML, Pipeline, GitHub Actions** 
* [cite_start]**DVC (Data Version Control)** 
* [cite_start]**MLflow (Experiment Tracking, Model Management)** 
* [cite_start]**Schedulers:** Apache Airflow [cite: 1][cite_start], Astronomer (for Airflow) 
* [cite_start]**Cloud Platforms:** AWS [cite: 1, 2][cite_start], Azure [cite: 1][cite_start], Heroku 
* [cite_start]**Containerization:** Docker 
* [cite_start]**Version Control:** Git, GitHub 
* [cite_start]**Databases:** MongoDB [cite: 1, 2][cite_start], PostgreSQL 
* [cite_start]**Visualization/Monitoring:** Grafana 
* [cite_start]**Machine Learning Platforms:** Amazon SageMaker 
* [cite_start]**Programming Language:** Python 

This structured approach aims to streamline the development, deployment, and maintenance of machine learning models.