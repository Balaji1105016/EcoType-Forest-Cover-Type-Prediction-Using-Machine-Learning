import streamlit as st
import pandas as pd
import pickle
import joblib

# Load Model
with open("random_forest_model.pkl", "rb") as file: 
    model = pickle.load(file)
    
le = joblib.load("label_encoder.pkl")
ohe = joblib.load("onehot_encoder.pkl")

st.title("Forest Cover Type Prediction")

# CSV Upload
uploaded_file = st.file_uploader("Upload File",type=["csv","xlsx","json"])

if uploaded_file is not None:
    file_name = uploaded_file.name
    #CSV:
    if file_name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    #Excel
    elif file_name.endswith(".xlsx"): 
        data = pd.read_excel(uploaded_file)
    #Json
    elif file_name.endswith(".json"):
        data = pd.read_json(uploaded_file)
    # Invalid File
    else:
        st.error("Unsupported File Format")

    st.write("Uploaded Data")
    st.dataframe(data)
    # Prediction
    encoded_arr = ohe.transform(data[["Soil_Type", "Wilderness_Area"]])
    encoded_df = pd.DataFrame(encoded_arr,columns=ohe.get_feature_names_out(["Soil_Type", "Wilderness_Area"]))
    # Drop Original Columns
    data = data.drop(["Soil_Type", "Wilderness_Area"],axis=1)
    # Combining DataFrames
    data = pd.concat([data.reset_index(drop=True),encoded_df.reset_index(drop=True)],axis=1)
    # Prediction
    prediction = model.predict(data)
    le_pred = le.inverse_transform(prediction)
    # Output
    data["Cover_Type_Prediction"] = le_pred
    st.write("Prediction Output")
    st.dataframe(data)
    
    # File Download:
    csv = data.to_csv(index=False).encode("utf-8")
    st.download_button(label="Download Prediction Output CSV",data=csv,file_name="Forest_cover_predictions.csv")