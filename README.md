# About
This is an API project that delivers the RESTful endpoints that power the [Property Management](https://github.com/jmgjuezan/property).

## Built using
* Python
* FastAPI

## Installation
```git clone https://github.com/jmgjuezan/property-be.git```

## Project structure
property-be/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── controller/
│   │   ├── __init__.py
│   │   └── (model)_controller.py
│   ├── model/
│   │   ├── __init__.py
│   │   └── (name)_model.py
│   ├── schema/
│   │   ├── __init__.py
│   │   └── (model)_schema.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── database.py
│   └── util/
│       ├── __init__.py
│       └── response_wrapper.py
└── requirements.txt

## Create virtual environment
```python -m venv .venv```

## Activate virtual environment
```.venv\Scripts\activate```

## Deactivate virtual environment
```deactivate```

## Download and install packages
```pip install -r requirements.txt```

## Save packages (Run inside active virtual environment)
```pip freeze > requirements.txt```

## Start the application
```uvicorn app.main:app --reload```

## Local
```http://127.0.0.1:8000```

## Swagger UI
```http://127.0.0.1:8000/docs```
