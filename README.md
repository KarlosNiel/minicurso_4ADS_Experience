# minicurso_4ADS_Experience
Esse Projeto foi realizada como parte da explicação teórica do minicurso de "Criação de APIs REST com Django" no 4° evento do ADS Experience.

### Configurações do projeto
- Crie um novo ambiente virtual dentro da pasta raiz do projeto para o projeto e o ative:
```powershell
python -m venv venv  # Criando o ambiente virtual.

.\venv\Scripts\activate # Ativando no Windows
source venv/bin/activate # Ativando no Linux
```
 ### Instalando as dependências 
- Instale as dependências necessárias para o projeto usando o requirements.txt com a venv ativada:
```powershell
pip install -r requirements.txt # vai instalar todas as dependências listadas dentro do arquivo requirements.txt
```

### Fazendo as migrações
- Faça as migrações necessárias para o banco de dados:
```powershell
python manage.py makemigrations # Cria as migrações
python manage.py migrate # Aplica as migrações
```

### Criando um superusuário
- Crie um superusuário para acessar o admin do Django e realizar a autenticação com a API:
```
python manage.py createsuperuser
```

### Material e guia prático
- Material didático: https://www.canva.com/design/DAGmCmMCz_k/cLpKoZi2eg7Aop6SQAIYXg/view?utm_content=DAGmCmMCz_k&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h985414fa34

- Guia prático: https://rough-hall-caf.notion.site/Criando-uma-REST-API-com-Django-1d7f2f35e352805d8314d71d1b951c0d
