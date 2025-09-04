# Use the LTS version of the official Ubuntu image
FROM ubuntu

# Install uv package manager and create directories
RUN apt-get update \
  && apt-get install -y curl \
  && su ubuntu -c 'curl -LsSf https://astral.sh/uv/install.sh | sh' \
  && apt purge -y curl \
  && apt -y autoremove \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p /app /opt/repo-ansible \
  && chown -R ubuntu:ubuntu /app /opt/repo-ansible

# Switch to regular user
USER ubuntu

# Copy the current directory (repo-ansible repository) into the container
COPY --chown=ubuntu:ubuntu . /opt/repo-ansible

# Ensure uv and uvx commands are discoverable
ENV PATH="/home/ubuntu/.local/bin:$PATH"

# Remove unnecessary files
# Install Python, Ansible, and other repo-ansible dependencies
RUN cd /opt/repo-ansible \
  && rm -rf .git .venv \
  && uv sync --locked --no-cache

# Set the working directory to /app where your target repository will be mounted
WORKDIR /app

ENV ANSIBLE_DISPLAY_OK_HOSTS=0
ENV ANSIBLE_DISPLAY_SKIPPED_HOSTS=0

# Set the default command to run when the container starts
ENTRYPOINT [ "uv", "run", "--project", "/opt/repo-ansible", "ansible-playbook", "-e", "repo_path=/app", "-i", "localhost", "/opt/repo-ansible/apply.yaml" ]
