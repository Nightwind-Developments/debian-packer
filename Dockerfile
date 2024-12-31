FROM ubuntu:24.04

# Sets the Virtual Environment path as an environment variable
ENV VENV=/opt/venv

# Copies the required files
COPY entrypoint.sh /entrypoint.sh
COPY debianpacker.py /usr/bin/debpack
COPY requirements.txt /requirements.txt

# Makes the entrypoint.sh Script an executable and sets it as an Entrypoint
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# Installs Python and VENV and creates a Python Virtual Environment (venv)
ENV PATH="$VENV/bin:$PATH"
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv && ln -s python3 /usr/bin/python && python3 -m venv $VENV
RUN pip install -r /requirements.txt
