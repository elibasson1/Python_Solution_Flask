FROM alpine:3.14

# Set the working directory in the container
WORKDIR /app

# Update package lists and install necessary packages
RUN apk add --no-cache python3 py3-pip && pip install --upgrade pip

# Copy requirements.txt and install dependencies
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy rest of the application code
COPY . .

# Expose the port on which the application will run
EXPOSE 5000

# Run the application
CMD ["python3", "app.py"]