# About
This is an API project that delivers the RESTful endpoints that power the [Property Management](https://github.com/jmgjuezan/property).

## Built using
* Python
* FastAPI
* Pydantic
* Uvicorn

## Installation
Using HTTP
```git clone https://github.com/jmgjuezan/property-be.git```

## Project structure
property-be/\
├── app/\
│   ├── \_\_init\_\_.py\
│   ├── main.py\
│   ├── controller/\
│   │   ├── \_\_init\_\_.py\
│   │   └── (model)_controller.py\
│   ├── model/\
│   │   ├── \_\_init\_\_.py\
│   │   └── (name)_model.py\
│   ├── schema/\
│   │   ├── \_\_init\_\_.py\
│   │   └── (model)_schema.py\
│   ├── db/\
│   │   ├── \_\_init\_\_.py\
│   │   └── database.py\
│   └── util/\
│       ├── \_\_init\_\_.py\
│       └── response_wrapper.py\
└── requirements.txt

main.py - contains base REST APIs as well as import controllers

Controller - contains REST APIs separated into models

Model - database collection representations

Schema - API body representations

DB - handles database connection

Util - common code snippet or functions

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
