# Stage13 — Productization Homework

Overview
--------
This repository contains a minimal example for packaging a trained scikit-learn model and exposing it via a small Flask API. It is intended as a handoff-ready starter for deployment and local testing.

Contents
--------
- `src/app.py` — example Flask application with `/predict` and `/plot` endpoints.
- `model/model.pkl` — serialized model (created by notebook).
- `requirements.txt` — Python dependencies.
- `notebook` — example notebook used to train and save the model.

Prerequisites
-------------
- Python 3.8+
- Windows PowerShell or CMD
- (Optional) virtual environment

Quick setup (Windows)
---------------------
1. Create and activate virtual environment (optional but recommended):
   - python -m venv .venv
   - .venv\Scripts\activate

2. Install dependencies:
   - pip install -r requirements.txt

Run the API
-----------
1. Run the Flask app:
   - python src\app.py

   The server should start on http://127.0.0.1:5000 (or the port configured in the script).

Test endpoints
--------------
- POST /predict
  - curl:
    - curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"features\": [0.1, 0.2]}"
  - Python:
    - ```python
      import requests
      r = requests.post("http://127.0.0.1:5000/predict", json={"features":[0.1,0.2]})
      print(r.json())
      ```

- GET /predict/<input1>
  - http://127.0.0.1:5000/predict/2.0

- GET /predict/<input1>/<input2>
  - http://127.0.0.1:5000/predict/1.0/3.0

- GET /plot
  - Open http://127.0.0.1:5000/plot in a browser to view the example chart.

Project structure
-----------------
Recommended minimal layout:
```
stage13/
  src/
    app.py
  model/
    model.pkl
  requirements.txt
  README.md
  notebooks/
```
Notes and recommendations related to the project
-------------------------
- Replace the placeholder prediction logic in src/app.py with a properly loaded model (joblib or pickle). Load the model once at app startup, not inside each request.
- Validate and sanitize inputs: check feature length, types, ranges and return clear 4xx errors for invalid requests.
- Provide an inference wrapper in src (e.g., src/model.py) that handles preprocessing, prediction and postprocessing so the API file stays thin and testable.
- Add logging (structured logs) and basic error handling to capture failures and stack traces for debugging.
- Configure host/port and other settings via environment variables (e.g., FLASK_ENV, PORT) rather than hard-coding.
- Include a healthcheck endpoint (e.g., /health) for deployment readiness checks.
- For local production testing use gunicorn (or similar) instead of the Flask dev server: gunicorn -w 4 -b 0.0.0.0:$PORT src.app:app
- Pin dependency versions in requirements.txt or use a lock file (pip-tools/poetry) to ensure reproducible installs.
- Add unit tests for the inference wrapper and simple integration tests for API endpoints (pytest + requests).
- Consider security and CORS policies if exposing externally; avoid running without authentication in production.
- Include model metadata (training date, features order, preprocessing steps, model version) next to the serialized model for maintainability.
- Document any manual steps, environment variables and expected input schema in this README for handoff.
- Add a LICENSE and contact/owner information so downstream users know usage and who to
-------------------------
- Replace placeholder prediction logic in `src/app.py` with the actual loaded model (joblib / pickle).
- Do not launch the Flask server inside a notebook thread for long-term testing; run `python src\app.py` in a terminal.
