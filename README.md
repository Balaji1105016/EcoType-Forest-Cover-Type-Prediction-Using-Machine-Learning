# EcoType-Forest-Cover-Type-Prediction-Using-Machine-Learning
Machine Learning project for multiclass forest cover prediction using Random Forest with SMOTE, feature engineering, hyperparameter tuning, and model evaluation.
🔥 Key Highlights
Performed complete EDA and data preprocessing
Handled class imbalance using SMOTE
Applied One-Hot Encoding and Label Encoding
Trained and evaluated multiple ML models
Selected Random Forest as the final model based on balanced multiclass performance
Achieved ~95% accuracy
Evaluated models using Classification Report and Confusion Matrix
Implemented Hyperparameter Tuning for optimization
Deployment-ready preprocessing pipeline with saved encoders and model files
🛠️ Tech Stack
Python, Pandas, NumPy, Scikit-Learn, XGBoost, Matplotlib, Seaborn, Joblib




📌 Project Statement:
To develop a machine learning classification model that predicts the type of forest cover in a given geographical area based on cartographic variables like elevation, soil type, slope, and wilderness area information. The goal is to assist in environmental monitoring, forestry management, and land use planning by providing automated, reliable forest cover type identification.




📌 Real-World Use Cases:
Forest Resource Management: Assist forestry departments in identifying and classifying forest areas for planning, conservation, and logging.
Wildfire Risk Assessment: Combine vegetation type with fire risk models to predict high-risk zones.
Land Cover Mapping: Used by environmental scientists and geospatial analysts for mapping and monitoring land usage patterns.
Ecological Research: Support studies in biodiversity, soil conservation, and habitat analysis.


Column Name
Elevation: Height of the land above sea level, measured in meters. Higher elevation often affects vegetation type and climate.
Aspect: Direction the slope faces, measured in degrees (0–360). It influences sunlight exposure (e.g., north-facing slopes get less sunlight).
Slope: Steepness of the terrain, measured in degrees. Higher slope means steeper terrain.
Horizontal_Distance_To_Hydrology: Horizontal distance (in meters) to the nearest surface water source (stream, river, lake).
Vertical_Distance_To_Hydrology: Vertical distance (in meters) to the nearest surface water source. Negative values indicate the point is below the water level.
Horizontal_Distance_To_Roadways: Horizontal distance (in meters) to the nearest roadway.
Hillshade_9am: Illumination index of the terrain at 9:00 AM, ranging from 0 (dark) to 255 (bright).
Hillshade_Noon: Illumination index of the terrain at 12:00 PM (noon), ranging from 0 to 255.
Hillshade_3pm: Illumination index of the terrain at 3:00 PM, ranging from 0 to 255.
Horizontal_Distance_To_Fire_Points: Horizontal distance (in meters) to the nearest wildfire ignition point.
Wilderness_Area: Categorical feature indicating the designated wilderness area the location belongs to 
Soil_Type: Categorical feature representing the soil classification at the location
Cover_Type: Target variable indicating the dominant forest cover type (e.g., spruce/fir, pine, hardwood).


