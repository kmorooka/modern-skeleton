# Up to latest container base images due to 3.8.12 security issues.
# c.f. iContainer base images - https://hub.docker.com/_/python
# FROM python:3.8.12-slim-bullseye
FROM python:3.10.5-slim-bullseye

RUN apt update  && \
  apt install -y git curl && \
  git clone https://github.com/kmorooka/modern-skeleton.git && \
  pip install --upgrade pip && \
  pip install -r /modern-skeleton/requirements.txt && \
  rm -rf ~/.cache

WORKDIR /modern-skeleton

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
