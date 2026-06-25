import subprocess
import shutil
import os

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)
if shutil.which(nginx):
    print("nginx is installed")
else:
    command="sudo apt-get update && suao apt-get install -y nginx"
    run(command)
run("sudo mv nayanap.site /etc/nginx/sites-available/nayanap.site")
run("sudo ln-sf /etc/nginx/sites-available/nayanap.site /etc/nginx/sites-enabled/nayanap.site")
run("sudo rm -f /etc/nginx/sites-enabled/default")
run("sudo mkdir -p /var/www/nayanap.site")
run("sudo mv /tmp/index.html /var/www/nayanap.site/index.html")

run("sudo nginx -t && sudo systemctl reload nginx")

ssh.close()
print("Done")