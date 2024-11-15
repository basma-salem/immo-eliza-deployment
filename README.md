# ![House Icon](https://img.icons8.com/ios-filled/32/000000/home.png) immo-eliza-deployment    
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

## 🏢 Description
The immo-eliza-Deployment project deploys a machine learning model to predict property prices through a FastAPI endpoint as the backend. It also features a Streamlit web application, providing an easy and intuitive way for users to interact with the model.
This setup ensures a robust backend for developers and a user-friendly frontend for non-technical users, making the property price prediction model accessible to a broad audience.

## 📦 Repo structure
```
immo-eliza-deployment/
│
├── API/
    └── app.py                          --- main app for FastAPI
    └── predict.py                      --- runs predictions on the new data
    └── preprocessing.py                --- data preprocessing for encode data
    └──xgboost_model.joblib             --- trained models saved in .joblib format to use for predictions
├── streamlit/
    └── streamlit.py                    --- main app for streamlit
├── .Dockerfile                         ---container for prerequestes to deploy on Render
├── .gitignore
├── requirements.txt
└── README.md
```
## 🔍 Quick Preview

You can explore the model through the following platforms:

- **Streamlit Web Application**:  
![Streamlit Icon](https://img.icons8.com/color/16/streamlit.png) <small>[https://immo-eliza-deployment-ajmwrdjt65ayap8caukwz2.streamlit.app/](https://immo-eliza-deployment-ajmwrdjt65ayap8caukwz2.streamlit.app/)</small>

- **FastAPI Documentation**:  
  <img src="https://fastapi.tiangolo.com/img/favicon.png" width="14"/> <small>[https://immo-eliza-deployment-m5tq.onrender.com/docs#/default/predictPrice_predict_post](https://immo-eliza-deployment-m5tq.onrender.com/docs#/default/predictPrice_predict_post)</small>

## 🔧 Local Development
**Follow these steps to set up your project environment:**
- *Clone the repository*
  `git clone https://github.com/basma-salem/immo-eliza-deployment.git`
  
- *Navigate to the project directory*
  `cd immo-eliza-deployment`
  
- *Install the required dependencies*
  `pip install -r requirements.txt`

    ### FastAPI Backend
    To run the FastAPI backend locally for development purposes, navigate to the `API/` directory and use `uvicorn` to serve the application with:
    ```
    uvicorn app:app --reload
    ```
    ### Streamlit Frontend
    To run the Streamlit app locally, navigate to the `streamlit/` directory then, start the Streamlit app with:
    ```
    streamlit run streamlit.py
    ```
## 🔧 Planned upgrade
  Add new features like EPC information and kitchen installation type for better model predictions.
## ⏱️ Timeline
  This project was done in 5 days including studying the theory and implementing the code.
## 📌 Personal Situation
  This project was done as part of my AI training program at [BeCode.org](https://becode.org/).


### Connect with me!
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/basma-salem-ba45a1113)