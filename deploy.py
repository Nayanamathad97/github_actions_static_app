
import paramiko, os

HOST = "43.205.125.124"
USER = "ubuntu"
KEY = "June-2026.pem"
PEM_DIR = "C:/Users/FWFQWT2/Desktop/PEMs"
DIR = os.path.dirname(os.path.abspath(__file__));

pem_file_path = os.path.join(PEM_DIR,KEY)

print(pem_file_path)


key = paramiko.RSAKey.from_private_key_file(pem_file_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=HOST,
    username=USER,
    pkey=key,
    look_for_keys=False,
    allow_agent=False
)

def run(cmd):
    _, out, err = ssh.exec_command(cmd)
    print(out.read().decode(), err.read().decode())


# 1. Install nginx if not installed
run("which nginx || (sudo apt-get update && sudo apt-get install -y nginx)")

# Upload files to /tmp first (no root needed there)
sftp = ssh.open_sftp()
sftp.put(os.path.join(DIR, "nayanap.site.conf"), "/tmp/nayanap.site.conf")
sftp.put(os.path.join(DIR, "index.html"), "/tmp/index.html")
sftp.close()


# 2. Setup Nginx config for it-defined.com (and remove default site)
run("sudo mv /tmp/nayanap.site.conf /etc/nginx/sites-available/nayanap.site")
run("sudo ln -sf /etc/nginx/sites-available/nayanap.site /etc/nginx/sites-enabled/nayanap.site")
run("sudo rm -f /etc/nginx/sites-enabled/default")


# 3. Copy the code to /var/www/it-defined.com
run("sudo mkdir -p /var/www/nayanap.site")
run("sudo mv /tmp/index.html /var/www/nayanap.site/index.html")


# Reload nginx
run("sudo nginx -t && sudo systemctl reload nginx")

ssh.close()
print("Done")