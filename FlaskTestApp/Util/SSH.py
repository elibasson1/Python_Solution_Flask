import paramiko as paramiko

from FlaskTestApp.Util.Read_INI_File import read_config_ini


def establish_ssh_connection():
    config = read_config_ini()['Server']

    username = config['user']
    private_key_path = config['private_key_path']
    host = config['host']
    port = config['port']

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # key_filename: This parameter specifies the path to the private key file that will be used for authentication.
    # In SSH, instead of using passwords for authentication, it's common to use key pairs, consisting of a public key
    # and a private key. The private key stays on your local machine, and the public key is stored on the server.
    # When you connect to the server, your SSH client (in this case, paramiko) uses your private key to prove your
    # identity.

    ssh.connect(host, port, username, key_filename=private_key_path)
    return ssh
