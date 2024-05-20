# Exercise_2_Solution
Exercise_2-Solution_Reverse

### Application

The application provides two APIs: API Reverse and API Restore:

#### API 1: /reverse

Receive as string via "in" query parameter using GET HTTP request, and return a response JSON with a field named "result" and its value should be the string provided with the words in reverse order.

For example: Where in value of:

http://host_machine_IP:5000/reverse?in=eli basson

Result value should be:basson eli

#### API 2: /restore

http://host_machine_IP:5000/restore

The API will return the last result from API 1.

Result value should be: eli basson

#### Notes

if your host machine's IP is 192.168.1.2

[http://192.168.1.2:5000/reverse?in=eli basson](<http://192.168.1.2:5000/reverse?in=eli basson>)
and http://192.168.1.2:5000/restore.

I used Flask to build the Python application.

The application itself includes explanations of the different commands

-------------------------------------------------------------------------------------------------------------------------------
#### Docker File 

Dockerfile is used to create a Docker image for a Python application.

FROM ubuntu:22.04: This line specifies the base image to use for the Docker image. In this case, it's Ubuntu 22.04.

WORKDIR /app: Sets the working directory within the container to /app. This is where the application code and files will be placed.

RUN apt-get update && apt-get install -y python3 python3-pip: Updates the package lists and installs Python 3 and pip inside the Docker image.

COPY requirements.txt .: Copies the requirements.txt file from the host machine to the /app directory in the container.

RUN pip3 install --no-cache-dir -r requirements.txt: Installs the Python dependencies specified in requirements.txt inside the container.

COPY . .: Copies the entire content of the current directory (where the Dockerfile is located) to the /app directory in the container. This assumes that your application code is in the same directory as the Dockerfile.

EXPOSE 5000: Informs Docker that the application inside the container will use port 5000. This does not actually publish the port; it is more of a documentation feature.

CMD ["python3", "app.py"]: Specifies the default command to run when the container starts. In this case, it runs the app.py file using Python 3.

-------------------------------------------------------------------------------------------------------------------------------

#### How to use :

To use this Dockerfile, you would typically build the Docker image using the following command:

docker build -t your_image_name .

**Please note : that currently the Docker name must be 'elib' It's important to use this name for now."**

-------------------------------------------------------------------------------------------------------------------------------

#### Test File :

The test file contains only four tests. It is possible to extend these tests to cover additional cases, but this is the base that I am currently working with.

The following is a list of the tests:

* test_reverse_valid_input : Tests the ability to reverse a valid input string.
* test_restore_valid_input :Tests the ability to restore a valid input string from its reverse.
* test_reverse_empty_input : Tests the ability to reverse an empty input string.
* test_restore_empty_input : Tests the ability to restore an empty input string from its reverse.

-------------------------------------------------------------------------------------------------------------------------------

#### Run the test file : 

To run the test file for the application, navigate to the directory where the test file is located.

Then, run the following command:

pytest test_app.py -v -s -rA --junit-xml=JunitRepot.xml

The results of the run will be saved in the JunitRepot.xml file in the directory where the test file is located.
