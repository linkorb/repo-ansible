# Use the official Python 3.12 image
FROM python:3.12

# Set the working directory to /opt/repo-ansible
WORKDIR /opt/repo-ansible

# Copy the current directory (repo-ansible repository) into the container
COPY . /opt/repo-ansible

# Install Ansible and other Python dependencies
RUN pip install --no-cache-dir -r /opt/repo-ansible/requirements.txt
RUN pip install --no-cache-dir ansible

# Set the working directory to /app where your target repository will be mounted
WORKDIR /app

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the default command to run when the container starts
CMD ["/entrypoint.sh"]