FROM python:3.12-slim-bookworm AS base
# python app are backward compatible

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
# upgrade pip to avoid any issues

RUN pip install --no-cache-dir -r requirements.txt
# install the requirements

COPY . .

ENTRYPOINT ["python", "recommandation_server.py"]
# recommandation_server.py conatins the main code of app