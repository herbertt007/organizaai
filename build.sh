#!/usr/bin/env bash
# Script de build para o Render
set -o errexit

# Instala dependências
pip install -r requirements.txt

# Entra na pasta do projeto Django
cd organizaai

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Roda migrações do banco de dados
python manage.py migrate
