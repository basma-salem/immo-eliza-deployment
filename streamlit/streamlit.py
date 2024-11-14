import streamlit as st
import requests

# Define the FastAPI endpoint
API_URL = "https://immo-eliza-deployment-m5tq.onrender.com/predict"

# Define options for dropdowns
property_types = ['APARTMENT', 'HOUSE']
provinces = ['Brussels', 'East Flanders', 'Flemish Brabant', 'Hainaut', 'Limburg',
             'Liège', 'Luxembourg', 'Namur', 'Walloon Brabant', 'West Flanders', 'Antwerp']
state_buildings = ['AS_NEW', 'JUST_RENOVATED', 'GOOD', 'TO_RESTORE', 'TO_BE_DONE_UP', 'TO_RENOVATE']
heating_types = ['GAS', 'ELECTRIC', 'SOLAR', 'CARBON', 'WOOD', 'PELLET', 'FUELOIL']


# Display title and header image
st.title("🏠 Property Price Prediction Tool")
st.subheader("Estimate the market value of your property with AI")




property_type = st.selectbox("🏢 Property Type", property_types, help="Select the type of property.")
province = st.selectbox("🌍 Province", provinces, help="Choose the province where the property is located.")
zip_code = st.number_input("📍 Zip Code", min_value=0, value=1000, help="Enter the postal code for the property.")



total_area_sqm = st.number_input("📏 Total Area (sqm)", min_value=0, value=100, help="Enter the total area of the property.")
nbr_bedrooms = st.number_input("🛌 Number of Bedrooms", min_value=0, value=1, help="Specify the number of bedrooms.")
surface_land_sqm = st.number_input("🌱 Surface Land (sqm)", min_value=0.0, value=100.0, help="Enter the land area size if applicable.")



state_building = st.selectbox("🏗️ State of Building", state_buildings, help="Choose the current state of the building.")
heating_type = st.selectbox("🔥 Heating Type", heating_types, help="Select the heating type used in the building.")
primary_energy_consumption_sqm = st.number_input("⚡ Energy Consumption", min_value=0, value=100, help="Enter the Energy Consumption if applicable.")
nbr_frontages = st.number_input("🚪 Number of Frontages", min_value=0, value=0, help="Number of building sides exposed to the outside.")



terrace_sqm = st.number_input("🌅 Terrace Size (sqm)", min_value=0.0, value=0.0, help="Size of the terrace area if any.")
garden_sqm = st.number_input("🌳 Garden Size (sqm)", min_value=0.0, value=0.0, help="Size of the garden area if any.")

# Collect input data for the API
input_data = {
    "property_type": property_type,
    "province": province,
    "zip_code": zip_code,
    "total_area_sqm": total_area_sqm,
    "nbr_bedrooms": nbr_bedrooms,
    "surface_land_sqm": surface_land_sqm,
    "state_building": state_building,
    "heating_type": heating_type,
    "primary_energy_consumption_sqm" : primary_energy_consumption_sqm,
    "nbr_frontages": nbr_frontages,
    "terrace_sqm": terrace_sqm,
    "garden_sqm": garden_sqm,
}
# Submit button
st.markdown("---")
if st.button("💰 Get Price Estimate"):
    try:
        response = requests.post(API_URL, json=input_data)
        
        if response.status_code == 200:
            #prediction = response.json()
            prediction = response.json().get("prediction")
            st.success(f"💵 Estimated Property Price: {prediction}")
        else:
            st.error(f"❌ Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Connection error: {e}")

# Footer note for user guidance
st.markdown("---")
st.write("ℹ️ Ensure the FastAPI server is running and accessible at the configured endpoint.")
