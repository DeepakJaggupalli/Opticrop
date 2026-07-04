# Entity Relationship Diagram

```mermaid
erDiagram
    FARMER {
        int farmer_id PK
        string name
        string location
        string contact_info
    }
    
    SOIL_DATA {
        int record_id PK
        int farmer_id FK
        float nitrogen
        float phosphorus
        float potassium
        float ph
        float temperature
        float humidity
        float rainfall
        date date_recorded
    }
    
    CROP_RECOMMENDATION {
        int recommendation_id PK
        int record_id FK
        string crop_predicted
        date prediction_date
    }
    
    FARMER ||--o{ SOIL_DATA : "records"
    SOIL_DATA ||--|| CROP_RECOMMENDATION : "generates"
```

## Description
- **FARMER**: Represents the user (farmer) interacting with the application.
- **SOIL_DATA**: Represents the environmental parameters (N, P, K, pH, temp, humidity, rainfall) provided by the farmer.
- **CROP_RECOMMENDATION**: Represents the ML model's output predicting the most suitable crop based on the soil data.
