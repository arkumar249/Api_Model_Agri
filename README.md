# 🌱 Agri API Model

A FastAPI-based backend providing agricultural intelligence tools to support farmers with data-driven decisions.

**Features include:**

* Crop Recommendation
* Fertilizer Recommendation
* Plant Disease Detection
* Irrigation Planning
* User Authentication & AI Chat Support

---

## 🚀 Features

* **Crop Recommendation:** Suggests the best crops based on soil nutrients (N, P, K), temperature, humidity, pH, and rainfall.
* **Fertilizer Recommendation:** Uses ensemble ML models to recommend fertilizers.
* **Plant Disease Detection:** Detects plant diseases from images.
* **Irrigation Planning:** Provides water scheduling guidance.
* **Authentication & User Management:** Secure JWT-based authentication.
* **Chat Assistance:** Interactive chat support for agricultural queries.

---

## 📂 Project Structure

```
api-agri/
│── Models/                 
│   ├── Fertilizer_Recommender/   # Fertilizer ML training & models
│   │   ├── models/               # Saved models (.pkl, encoders, etc.)
│   │   ├── train.py              # Training script for fertilizer recommender
│   │   ├── utils.py              # Helper functions
│   │   └── fertilizer_recommender.py
│   ├── crop_recommendation.py    # Crop recommendation model
│   ├── plant_disease_detector.py # Plant disease detection model
│
│── core/                   # Core utilities (e.g., database)
│── routers/                # FastAPI route handlers
│── schemas/                # Pydantic schemas
│── utilities/              # Helper functions
│── main.py                 # FastAPI entry point
│── .env                    # Environment variables (not pushed)
│── requirements.txt        # Python dependencies
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/arkumar249/Api_Model_Agri.git
cd Api_Model_Agri/api-agri
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv

# Activate:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
```

```bash
pip install fastapi uvicorn pandas scikit-learn xgboost matplotlib pillow python-multipart pydantic
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the project root:

```env
SUPABASE_URL=<YOUR_SUPABASE_URL>
SUPABASE_KEY=<YOUR_SUPABASE_KEY>
GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
```

---

## ▶️ Running the API Server

```bash
uvicorn main:app --reload
```

Access the API at:

```
http://127.0.0.1:8000
```

## 🤖 Running & Training ML Models

### 1️⃣ Crop Recommendation

* File: `Models/crop_recommendation.py`
* Input features: N, P, K, temperature, humidity, pH, rainfall
* Test standalone:

```bash
python Models/crop_recommendation.py
```

### 2️⃣ Fertilizer Recommendation

* Directory: `Models/Fertilizer_Recommender/`
* Training script: `train.py`
* Trained models stored in `Models/Fertilizer_Recommender/models/`

Run training:

```bash
python Models/Fertilizer_Recommender/train.py
```

Generates/overwrites:

* `ensemble_model.pkl`
* `rf_model.pkl`
* `xgb_model.pkl`
* `label_encoder.pkl`
* `feature_columns.json`

### 3️⃣ Plant Disease Detection

* File: `Models/plant_disease_detector.py`
* Accepts image input for classification.
* Test standalone:

```bash
python Models/plant_disease_detector.py
```

### 4️⃣ Irrigation Planning

* File: `routers/irrigationPlan.py`
* Provides API endpoint for irrigation scheduling.
* Can be tested through API request.


### 5️⃣ AI Chat Router

* File: routers/chats.py

 * Provides AI-powered chat endpoints
---

## 🧪 Example API Requests



### Crop Recommendation

```http
POST http://127.0.0.1:8000/api_model/crop_recommendations
Content-Type: application/json

{
  "N": 90,
  "P": 40,
  "K": 40,
  "temperature": 25,
  "humidity": 80,
  "ph": 6.5,
  "rainfall": 200
}
```

### Fertilizer Recommendation

```http
POST http://127.0.0.1:8000/api_model/fertilizer_recommendation
Content-Type: application/json

{
  "N": 90,
  "P": 40,
  "K": 40,
  "temperature": 25,
  "humidity": 80,
  "ph": 6.5,
  "rainfall": 200,
  "crop": "rice"
}
```

### Plant Disease Detection

```http
POST http://127.0.0.1:8000/api_model/pest_detection_and_analyze
Content-Type: multipart/form-data
file: <image_file>
```

---

## 📦 Deployment

For production:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Deploy on **Render, Railway, Heroku, or Docker**.

---


🔗 [GitHub](https://github.com/arkumar249)
