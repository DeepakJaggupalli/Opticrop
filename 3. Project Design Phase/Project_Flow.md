# Project Flow

## OptiCrop Smart Agricultural Production Optimization Engine

```mermaid
flowchart TD
    A[Start: Problem Definition] --> B[Data Collection]
    B --> C[Data Preprocessing]
    
    C --> C1[Handling Null Values]
    C --> C2[Outlier Detection]
    C --> C3[Extract Seasonal Crops]
    C --> C4[Train-Test Split]
    
    C1 --> D
    C2 --> D
    C3 --> D
    C4 --> D[Exploratory Data Analysis]
    
    D --> E[Model Building]
    
    E --> E1[Unsupervised: K-Means Clustering]
    E --> E2[Supervised: Logistic Regression]
    
    E1 --> F
    E2 --> F[Model Evaluation & Selection]
    
    F --> G[Save Best Model (.pkl)]
    
    G --> H[Application Development]
    
    H --> H1[Build Flask Backend]
    H --> H2[Build HTML/CSS Frontend]
    
    H1 --> I
    H2 --> I[Integrate & Test]
    
    I --> J[Deployment / Run Application]
    J --> K[End: Conclusion & Impact]
```

## Description of Workflow:
1. **Problem Definition:** Establish the objective of recommending the optimal crop based on environmental parameters.
2. **Data Collection:** Source a reliable agricultural dataset (`Crop_recommendation.csv`).
3. **Data Preprocessing & EDA:** Clean the data, identify patterns through univariate, bivariate, and multivariate analysis, and prepare it for modeling.
4. **Model Building:** Train K-Means to understand natural groupings of crops, and train Logistic Regression for final crop classification.
5. **Model Selection:** Evaluate the accuracy of the supervised models and save the best-performing model.
6. **Application Development:** Wrap the model in a Flask web application with a beautiful and user-friendly interface.
