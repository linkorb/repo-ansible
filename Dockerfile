# Use the official Python 3.12 image
FROM python:3.12

# Set the working directory to /opt/repo-ansible
WORKDIR /opt/repo-ansible

# Copy the current directory (repo-ansible repository) into the container
COPY . /opt/repo-ansible

# Install Ansible and other Python dependencies
RUN pip install --no-cache-dir --root-user-action=ignore ansible jsonschema

# Set the working directory to /app where your target repository will be mounted
WORKDIR /app

ENV ANSIBLE_DISPLAY_OK_HOSTS=0
ENV ANSIBLE_DISPLAY_SKIPPED_HOSTS=0

# Set the default command to run when the container starts
CMD ansible-playbook -ilocalhost, /opt/repo-ansible/playbook-cwd.yaml
