FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    USER=compiler

RUN apt-get update
RUN apt-get install -y ruby-full && gem install bundler
RUN python -m pip install --upgrade pip

RUN useradd --create-home --shell /bin/bash $USER && \
    mkdir /home/$USER/site && \
    chown -R $USER /home/$USER

WORKDIR /home/$USER/site

COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock
RUN bundle install

USER $USER
ENV PATH "$PATH:/home/$USER/.local/bin"

COPY LICENSE pyproject.toml README.md ./
RUN pip install -e .[dev,qr_codes]
