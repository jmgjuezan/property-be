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

Controller - contains REST APIs separated into models, no business logic in this layer

Model - database collection representations, data to pass to the database

Schema - API body representations passed from UI

DB - handles database connection

Util - common code snippet or functions

## Database structure

See https://github.com/jmgjuezan/property-be/tree/master/app/db

## Create virtual environment
```python -m venv .venv```

## Activate virtual environment
```.venv\Scripts\activate```

## Deactivate virtual environment
```deactivate```

## Download and install packages (Run inside active virtual environment)
```pip install -r requirements.txt```

## Force an upgrade and bypass any cached configurations
```pip install --upgrade --force-reinstall -r requirements.txt```

## Save or update packages (Run inside active virtual environment)
```pip freeze > requirements.txt```

## Start the application (Run inside active virtual environment)
```uvicorn app.main:app --reload```

## Local
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## Swagger UI
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
