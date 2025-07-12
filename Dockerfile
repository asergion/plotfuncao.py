# Use uma imagem base oficial do Python. A versão 'slim' é menor.
FROM python:3.10-slim

# Instala dependências do sistema necessárias para compilar alguns pacotes Python.
# A imagem 'slim' é mínima e não inclui ferramentas de compilação.
# --no-install-recommends: não instala pacotes recomendados, mantendo a imagem menor.
# && rm -rf /var/lib/apt/lists/*: limpa o cache do apt para reduzir o tamanho da imagem.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências primeiro para aproveitar o cache do Docker.
# Se o requirements.txt não mudar, o Docker não reinstalará as dependências.
COPY requirements.txt .

# Instala as dependências
# --no-cache-dir: Desabilita o cache do pip para manter a imagem menor.
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto para o diretório de trabalho no container
COPY . .

# Expõe a porta padrão do Streamlit para que possamos acessá-la de fora do container
EXPOSE 8501

# Comando para executar a aplicação quando o container iniciar.
# Usamos --server.address=0.0.0.0 para que o Streamlit seja acessível externamente.
CMD ["streamlit", "run", "View/app_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]