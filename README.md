# Comp3211 Coursework 2

This project consists of three RESTFul Web Services - two OWN web services and one external API call. The services are developed using Python [Flask-RESTFul](https://flask-restful.readthedocs.io/en/latest/) and the integrated web client is developed using Python [Flask](https://flask.palletsprojects.com/en/2.2.x/).

## Files and Their Purpose

- [ ] AccountAPI.py - The first web service, displaying bank accounts owned by the user
- [ ] ProfileAPI.py - The second web service, displaying stock profiles held by each account
- [ ] testAccounts.py - The client for testing the first web service
- [ ] testProfiles.py - The client for testing the second web service
- [ ] client.py - The integrated **testing client** which can be run through a command line interface 
- [ ] testExternal.py - The client for testing the external API web service

- [ ] ./app - Directory containing files to deploy the integrated client as a Flask web service
- [ ] config.py - Configuration of the Flask web service

## Requirements

Any necessary modules are included in the __requirements.txt__ file.
```bash
pip install -r requirements.txt
```
***

## Running the Integrated Client

First, run the first web service in a terminal.
```bash
python AccountAPI.py
```

Next, run the second web service in a terminal.
```bash
python ProfileAPI.py
```

Now, execute the integrated client web service using flask.
```
FLASK_APP=run.py
FLASK_ENV=development
flask run
```

The integrated client can be viewed as a web service on the local host through port 5000.

## Running the Tests

To execute the first web services' client for testing use the following command:
```bash
python testAccounts.py
```

To execute the second web services' client for testing use the following command:
```bash
python testProfiles.py
```

To execute the External web services' client for testing use the following command:
```bash
python testExternal.py
```

***

## Student Names and Contact
Shruti Rajesh Naik - sc20srn@leeds.ac.uk

Keegan Afonso - ed19kja@leeds.ac.uk

## References

1. The files base.html, base2.html and base3.html in the app directory are used from my (Shruti's) previous module coursework, namely COMP2011 - Web Application Development.

2. Flask-RESTful documentation used for implementation (linked below)
https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example



