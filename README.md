# OptiCrop Smart Agricultural Production Optimization Engine

![Demo Link](https://img.shields.io/badge/Live_Demo-Coming_Soon-brightgreen?style=for-the-badge)
![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge)

The project **Smart Agricultural Production Optimization Engine (OptiCrop)** aims to develop an advanced software system that utilizes data-driven insights to optimize agricultural production for different crops. By integrating key environmental factors such as Nitrogen (N), Phosphorous (P), Potassium (K) levels, soil temperature, humidity, pH, rainfall, and crop types, OptiCrop seeks to provide intelligent recommendations to farmers for maximizing yields and resource efficiency. 

## Features
- **Smart Crop Recommendation:** Farmers enter soil and environmental details and receive recommendations on the most suitable crop.
- **Crop Suitability & Environmental Assessment:** Evaluation of inputs for crop compatibility.
- **Agricultural Research:** Insights and data relationships mapped to support researchers and policymakers.

## Technical Architecture
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Backend Framework:** Flask
- **Frontend:** HTML5, CSS3 (Glassmorphism design aesthetic), JS
- **Machine Learning Models:** K-Means Clustering, Logistic Regression

## Project Setup Instructions

### Prerequisites
- Python 3.10+

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/DeepakJaggupalli/Opticrop.git
   cd Opticrop
   ```
2. **Install the dependencies:**
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn flask joblib
   ```
3. **Train the Model (Optional, model is pre-trained):**
   ```bash
   python model_pipeline.py
   ```
4. **Run the Application:**
   ```bash
   python app.py
   ```
5. **Access the Application:**
   Open a web browser and go to `http://127.0.0.1:5000/`

## Project Status

This repository fulfills all the Epics and tasks defined in the project board:
- `ER_Diagram.md`: Entity Relationship documentation
- `Business_Requirements.md`: Business requirements and problem definition
- `Project_Flow.md`: Complete workflow diagram
- `model_pipeline.py`: Comprehensive Exploratory Data Analysis (EDA) and Model building pipeline
- `app.py`: Backend Flask application serving ML models
- `templates/` & `static/`: High-end CSS & HTML interface for interacting with the engine.

## Authors
- **Team Lead:** Deepak Jaggupalli
- **Members:** Abhinav Tarigoppula, Revan Edupuganti, Kritik Kumar, Jahnavi Potnuri
