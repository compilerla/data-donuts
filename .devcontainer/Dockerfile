FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    USER=compiler

ENV WORK_DIR=/home/$USER/site \
    MISE_DIR=/home/$USER/mise

RUN useradd --create-home --shell /bin/bash $USER && \
    mkdir $WORK_DIR && \
    chown -R $USER /home/$USER

# Install rvm (https://rvm.io/rvm/install#install-gpg-keys)
RUN gpg --keyserver keyserver.ubuntu.com --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
RUN curl -sSL https://get.rvm.io | bash -s stable
RUN echo 'source /usr/local/rvm/scripts/rvm' >> /etc/bash.bashrc

WORKDIR $WORK_DIR

# Install Ruby, Bundler, and dependencies
COPY .ruby-version Gemfile Gemfile.lock ./
RUN /bin/bash -l -c 'rvm install $(cat .ruby-version | tr -d "\n") && gem install bundler && bundle install'

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

COPY LICENSE pyproject.toml README.md ./
RUN python -m pip install --upgrade pip
RUN pip install -e .[dev,qr_codes]
