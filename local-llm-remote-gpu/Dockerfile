FROM python:3.10

# ENV MODEL='orca-mini-3b-gguf2-q4_0.gguf'

WORKDIR /usr/src

RUN apt update && apt install -y libvulkan1 libgl1 libglib2.0-0

RUN wget https://github.com/Juice-Labs/Juice-Labs/releases/latest/download/JuiceClient-linux.tar.gz

WORKDIR /usr/src/JuiceClient

RUN tar -xf ../JuiceClient-linux.tar.gz

WORKDIR /usr/src/JuiceClient/app

COPY requirements.txt .

RUN pip install -r requirements.txt

# COPY download_model.py .

# RUN python download_model.py

# COPY juice.cfg /usr/src/JuiceClient/

COPY llms/yarn-llama-2-13b-64k.Q4_K_M.gguf /usr/src/JuiceClient/app/
COPY chatty.py .

ENV JUICESERVER 127.0.0.1:43210 

CMD /usr/src/JuiceClient/juicify --address ${JUICESERVER} python -u chatty.py