FROM python:latest

# Instala o conector MySQL para Python
RUN pip install mysql-connector-python

# Copia o arquivo index.py para dentro do contêiner
COPY index.py /app/index.py

# Define o diretório de trabalho 
WORKDIR /app

# Comando para executar o arquivo index.py
CMD ["python", "index.py"]
