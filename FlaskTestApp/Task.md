# Automation

## Introduction

Hello, 

Your assignment is to create a test framework for testing a dockerized application and its API.
The framework should allow developers to add new tests in a simple way.

In addition, you should create documentation that will allow any user to take the code, create the container and run the tests.

## Tasks

### Application
Create a Docker container with Python HTTP application which will provide 2 REST APIs 

API 1: `/reverse`  
The API should receive as string via "in" query parameter using GET HTTP request, and return a response JSON with a field named "result" and its value should be the string provided with the words in reverse order.

For example:
Where in value of:
```
The quick brown fox jumps over the lazy dog"
```
Result value should be:
```
dog lazy the over jumps fox brown quick The
```

API 2: `/restore`  
The API will return the last result from API 1.

### Testing framework
Create a testing framework in Python using pytest which:

* Starts the application container created above
* Run tests to ensure the API conforms to the Application requirements listed above.
* Shuts down the application container when test is completed or on error.
* Publishes the result as JUnit file.

The framework should be designed in a way that allows developers to easily add additional API tests on their own.

## Deliverables
A link to your GitHub repository (or other Git repository provider), containing:

* Application code
* Dockerfile
* Tests written using pytest
* A README file with instructions about this assignment, how to build the container, how to run tests and what should be a successful test result.
