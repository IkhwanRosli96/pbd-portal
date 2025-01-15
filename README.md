# PBD API User and Documentation Portal

PBD API User and Documentation Portal is  Web Application created by PND UTM Researcher. This application was created to manage API user and the documentation of the APi. This portal also will be used to analyse the usage of the API.

## File Structure

```
├── apps
│   ├── admin
│   │   ├── __init__.py
│   │   └── routes.py
|   |
│   ├── database
│   │   ├── db.py
│   │   ├── models.py
│   │   └── util.py
|   |
│   ├── api_request
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── util.py
|   |
│   ├── documentation
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── util.py
|   |
│   ├── user
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── util.py
|   |
│   ├── login
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── util.py
|   |
│   ├── logout
│   │   ├── __init__.py
│   │   └── routes.py
│   │  
│   ├── static
│   │  
│   ├── templates
|   |
|   |
│   ├── config.py
│   ├── __init__.py
|   |
├── flask_session
├── log
├── README.md
├── requirements.txt
└── run.py
