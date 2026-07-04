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
2. **Navigate to the Development folder:**
   ```bash
   cd "5. Project Development Phase"
   ```
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Train the Model (Optional, model is pre-trained):**
   ```bash
   python model_pipeline.py
   ```
5. **Run the Application:**
   ```bash
   python app.py
   ```
6. **Access the Application:**
   Open a web browser and go to `http://127.0.0.1:5000/`

## Vercel Deployment Notes
When deploying to Vercel, make sure to set the **Root Directory** in the Vercel project settings to `5. Project Development Phase` so it can find the `vercel.json` and `app.py`.

## Project Structure

This repository follows the structured AI/ML Track template:
- `1. Brainstorming & Ideation/`
- `2. Requirement Analysis/`: Business requirements and problem definition
- `3. Project Design Phase/`: Entity Relationship and Workflow diagrams
- `4. Project Planning Phase/`
- `5. Project Development Phase/`: All source code, models, UI (`app.py`, HTML/CSS), and dataset
- `6.Project Testing/`
- `7.Project Documentation/`
- `8.Project Demonstration/`

## Authors
- **Team Lead:** Deepak Jaggupalli
- **Members:** Abhinav Tarigoppula, Revan Edupuganti, Kritik Kumar, Jahnavi Potnuri
