FROM ubuntu:22.04
# Set the working directory in the container
WORKDIR /app

# Update package lists and install necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy requirements.txt and install dependencies
COPY requirements.txt .
COPY static .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port on which the application will run
EXPOSE 5000
CMD ["python3", "app.py"]