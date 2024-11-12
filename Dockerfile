# Gitlab docker builder image
# Gitlab docker builder image
# contemporary version of skopeo needed
FROM docker:20.10

ENV DOCKER_TLS_CERTDIR "/certs"
ENV DOCKER_CLI_EXPERIMENTAL enabled
ENV BUILDX_URL https://github.com/docker/buildx/releases/download/v0.8.2/buildx-v0.8.2.linux-amd64

# Install necessary dependencies
RUN apk add --no-cache \
    wget git bash findutils curl g++ libmagic skopeo jq \
    python3 python3-dev libffi-dev openssl-dev

# Create directory for docker CLI plugins
RUN mkdir -p $HOME/.docker/cli-plugins/

# Download and install Buildx
RUN wget -q -O $HOME/.docker/cli-plugins/docker-buildx $BUILDX_URL && \
    chmod a+x $HOME/.docker/cli-plugins/docker-buildx

# Set up Python and pip
RUN python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools

# Ensure `python` and `pip` commands are accessible
RUN ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

# Copy Poetry configuration files
COPY pyproject.toml /root/
COPY poetry.lock /root/

# Set working directory
WORKDIR /root

# Environment variables for Python and Poetry
ENV PIP_DISABLE_PIP_VERSION_CHECK=true
ENV VIRTUAL_ENV_DISABLE_PROMPT=1
ENV PATH="/root/.local/bin:$PATH"

# Install Poetry and dependencies
RUN pip install poetry==1.2 && \
    poetry config virtualenvs.create true --local && \
    poetry config virtualenvs.in-project true --local && \
    poetry install --no-interaction -vv

# Link virtual environment to a known path
RUN ln -s $(poetry env info --path) /root/cuda_manager_env

# Clean up project files to keep image size smaller
RUN rm /root/pyproject.toml /root/poetry.lock

# Add virtual environment activation to bash startup
RUN echo 'source /root/cuda_manager_env/bin/activate' >> ~/.bashrc

# Entry point to run bash with virtual environment activated
CMD ["/bin/bash"]

