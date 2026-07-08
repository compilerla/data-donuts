FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    USER=compiler

ENV WORK_DIR=/home/$USER/site \
    MISE_DIR=/home/$USER/mise

RUN useradd --create-home --shell /bin/bash $USER && \
    mkdir $WORK_DIR && \
    chown -R $USER /home/$USER

WORKDIR $WORK_DIR

# Install mise (to manage Node.js) https://mise.jdx.dev/mise-cookbook/docker.html#docker-image-with-mise
ENV MISE_DATA_DIR=$MISE_DIR \
    MISE_CONFIG_DIR=$MISE_DIR \
    MISE_CACHE_DIR="$MISE_DIR/cache" \
    MISE_TRUSTED_CONFIG_PATHS=$WORK_DIR \
    MISE_INSTALL_PATH="/usr/local/bin/mise"

RUN curl https://mise.run | sh

USER $USER
RUN git config --global --add safe.directory $WORK_DIR

# Install Node.js and npm dependencies
COPY mise.toml .node-version package.json package-lock.json ./
RUN mise exec -- npm install -g npm@latest && mise exec -- npm clean-install
ENV PATH="$PATH:$MISE_DIR/shims"

COPY LICENSE pyproject.toml README.md ./
RUN python -m pip install --upgrade pip
RUN pip install -e .[dev,qr_codes]
