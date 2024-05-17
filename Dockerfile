FROM python:3.10.12
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -u ./main.py & 
RUN python -m pytest ./test_nsobot.py