# Reverie Challenge

## Usage

Docker:
```
docker build -t nishant-challenge:latest .
docker run -d -p 5000:5000 nishant-challenge
```

and then navigate to http://127.0.0.1:5000/

Local Development
```
conda create -n reverie python=3.7
source activate flask-template
pip install -r requirements.txt
pre-commit install
python app.py
```
