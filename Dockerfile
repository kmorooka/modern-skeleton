FROM python:3.8.12-slim-bullseye

RUN apt update  && \
  apt install -y git curl && \
  git clone https://github.com/kmorooka/modern-skeleton.git && \
  pip install --upgrade pip && \
  pip install -r /modern-skeleton/requirements.txt && \
  rm -rf ~/.cache

WORKDIR /modern-skeleton

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
