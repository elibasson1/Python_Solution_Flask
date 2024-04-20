import subprocess
import time
import pytest
import socket

pytest.global_var = None


@pytest.fixture(scope="class")
def setup(request):
    local_ip_address = get_local_ip()
    request.cls.local_ip_address = local_ip_address

    # Start the Docker container before the test class
    container_id = start_docker_container()
    request.cls.container_id = container_id

    # Wait for the container to be up and running (adjust as needed)
    time.sleep(5)

    yield
    # Cleanup: Stop and remove the Docker container after the test class
    stop_docker_container(container_id)


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Connect to an external server (doesn't actually send any data)
    s.connect(("8.8.8.8", 80))
    # Get the local IP address from the connected socket
    ip_address = s.getsockname()[0]
    return ip_address


def start_docker_container():
    # Start your Docker container and get the container ID
    # You may need to replace "your_docker_image" with the actual name or ID of your Docker image
    cmd = "docker run -d -p 5000:5000 elib"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        container_id = result.stdout.strip()
        return container_id
    else:
        # Handle the case when the command fails
        print("Failed to start Docker container. Check your Docker setup.")
        return None


def stop_docker_container(container_id):
    # Stop and remove the Docker container
    cmd_stop = f"docker stop {container_id}"
    cmd_remove = f"docker rm {container_id}"
    subprocess.run(cmd_stop, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(cmd_remove, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
