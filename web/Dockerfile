FROM python:3.9.7-slim

COPY . /app
WORKDIR /app

# Download Package Information
RUN apt-get update -y
#RUN apt-get update -y  &&  apt-get upgrade -y

# Install Tkinter
RUN apt-get install tk -y



RUN python3 -m venv /opt/venv


RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]