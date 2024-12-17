FROM nginx

# Copia os arquivos do host para o contêiner
COPY ./index.html /usr/share/nginx/html

# Tráfego externo
EXPOSE 80

# Comando para iniciar o Nginx quando o contêiner for iniciado
CMD ["nginx", "-g", "daemon off;"]
