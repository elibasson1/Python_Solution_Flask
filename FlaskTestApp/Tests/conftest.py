import paramiko as paramiko
import time
import pytest

from FlaskTestApp.Util.Logger import getLogger
from FlaskTestApp.Util.SSH import establish_ssh_connection


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    log = getLogger()
    ssh = establish_ssh_connection()

    # Start the Docker container remotely before the test class
    container_id = start_docker_container(ssh)
    request.cls.container_id = container_id

    # Wait for the container to be up and running (adjust as needed)
    log.info("Docker container has started")
    time.sleep(5)

    yield
    # Cleanup: Stop and remove the Docker container after the test class
    stop_docker_container(ssh, container_id)
    log.info("Docker container has been stopped and removed.")

    # Close the SSH connection
    ssh.close()


# Initiates the Docker container remotely via SSH by executing the docker run command.
def start_docker_container(ssh):
    # run commands
    cmd = "docker run -d -p 5000:5000 elib"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    container_id = stdout.read().strip().decode()
    return container_id


# Stops and removes the Docker container remotely via SSH by executing docker stop and then docker rm commands.
def stop_docker_container(ssh, container_id):
    cmd_stop = f"docker stop {container_id}"
    cmd_remove = f"docker rm {container_id}"
    # Execute the 'docker stop' command
    stdin_stop, stdout_stop, stderr_stop = ssh.exec_command(cmd_stop )
    # Wait for the command to finish
    stdout_stop.channel.recv_exit_status()

    # Execute the 'docker rm' command
    stdin_remove, stdout_remove, stderr_remove = ssh.exec_command(cmd_remove)
    # Wait for the command to finish
    stdout_remove.channel.recv_exit_status()