> 565. Criando o projeto e-commerce no VSCode
* Criar um novo projeto
* Criar um novo ambiente virtual
- Ativar o ambiente virtual
* Instalar o django
* Instalar as bibliotecas do django
- pip install pillow  - importar e redimensionar as imagens
- pip install django-crispy-forms
* Ativar o ambiente virtual
* Criar o projeto loja .
* Criar os apps (pedido, perfil e produto)
* Utilizar o `python manage.py migrate`
* Utilizar o `python manage.py createsuperuser`
- Informar o username padrao
- Informar o e-mail padrão
- Informar a senha padrao
* Utilizar o `pip install pylint-django`
* Rodar o projeto no servidor
- ir na /admin
- digitar o seu username
- digitar o seu password
- ir no settings no projeto e alterar para a LANGUAGE CODE = 'pt-br' e TIME_ZONE = 'America/Sao_Paulo'
- depois de STATIC_URL = '/static/' incluir o STATIC_ROOT = os.path.join(BASE_DIR, 'static')
- depois o STATICFILES_DIRS = [ps.path.join('templates/static')]
- depois o MEDIA_URL = '/media/'
- depois o MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
- instalar o pylint ( dentro do vscode)
* Colar o script messenges do roteiro e colocar no settings.py (no final)
* Colar o script no sessions
*Se der algum erro na hora de rodar, criar uma pasta chamada templates na raiz e dentro dela outra pasta chamada static
- 
# Sessão em dias: 60s * 60m * 24h * 1d - [Quero que a sessao dure por 7 dias]
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7

# Salvar a cada requisição [Normalmente já é false por padrao, mas eu quero formalizar. Cada vez que você manipular a sessao, ela não vai ser salva automaticamente, eu vou ter que pedir para
que essa sessão seja salva dentro da base de dados]
SESSION_SAVE_EVERY_REQUEST = False

# Serializer - Padrão JSON [Para que eu possa incluir os objetos[produtos] dentro da base de dados, ao inves de incluir nas sessoes]
# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Para sessions em arquivos ao invés da base de dados
# SESSION_ENGINE = "django.contrib.sessions.backends.file"
# SESSION_FILE_PATH = '/home/luizotavio/Desktop/temp'
______________________________________________________________________________________________
> 566. Criando os models Produto e Variação
Criar os models do produto
incluir somente o do produto
incluir o app produtos no settings
colocar o produto no admin do app
após, utilizar o comando python manage.py makemigrations
depois, python manage.py migrations
