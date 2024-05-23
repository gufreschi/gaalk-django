# GAALK

- ## Descrição do projeto:
Queria criar um site para catálogo de filmes com algumas opções de interação, para que os usuários possam ter uma ferramenta filtrada e que ajude-os a se organizar e expor opiniões.

- ## Funcionalidades:
O projeto atualmente conta com a página inicial, que servirá para mostrar algumas opções de filmes para o usuário. Também tem o cadastro e login, que faz a autenticação do usuário no back-end.
E por fim tem a barra de pesquisa de filmes trazendo todas as buscas encontradas na API. Todas contam com um menu lateral de navegação.

- ### Implementações futuras:
1. Página descobrir, com a possibilidade de navegar por filmes de gêneros específicos escolhidos pelo usuário.

1. Página biblioteca organizada, onde o usuário pode classificar de 3 formas: O que já assistiu, o que ainda não assistiu e o que está próximo de ser assistido.

2. Uma parte de 'comentários' em cada filme, aonde os usuários logados podem publicar o que acharam e etc.

- ## Tecnologias utilizadas:
Por enquanto o projeto conta com HTML, CSS e JavaScript para o front-end. Em futuras atualizações pretendo usar um framework (bem provável que eu use Vue.js).
O back-end foi feito com Python e seu framework Django.

# Configuração do ambiente
Nessa parte você encontrará o necessário para rodar o projeto em sua máquina.

- ## Baixar e instalar:
1. Python em sua última versão. É recomendável que você execute o download no site oficial do python e busque por um passo à passo para não deixar passar nenhuma opção.
2. Com o python instalado, você deve agora baixar o seu framework Django. No prompt de comando execute o comando `pip install django`.
3. Com o framework Django instalado, clone este repositório em sua máquina e abra o conteúdo em alguma IDE (exemplo: Visual Studio Code).
4. Com o projeto aberto, execute o comando `CTRL + J` para abrir o terminal para instalar um pacote do Django para lidar com a API com o comando `pip install requests`.
5. Rode o comando `pip install whitenoise` também no terminal, que instalará a biblioteca responsável por carregar os arquivos static.
6. Agora, digite `cd .\projeto_GAALK\` para acessar a pasta com o arquivo `manage.py`.
7. Por fim, rode o comando `python .\manage.py runserver` e a sua máquina estará rodando o projeto, caso não houver nenhum erro.
8. Abra o link da porta local pelo terminal com `CTRL + Click` ou diretamente no navegador com a URL padrão: `http://127.0.0.1:8000/`.

# Imagens

![image](https://github.com/gufreschi/gaalk-django/assets/142360744/cda686a2-abd9-4b5c-bea5-96e329c72505)

![image](https://github.com/gufreschi/gaalk-django/assets/142360744/398bb163-e43b-41e3-9780-01d741fa7f8a)

![image](https://github.com/gufreschi/gaalk-django/assets/142360744/93e8e749-28fd-401e-ba66-4040d1885f9f)

![image](https://github.com/gufreschi/gaalk-django/assets/142360744/ee6b193f-66bc-4f90-9825-46961acc6f29)

![image](https://github.com/gufreschi/gaalk-django/assets/142360744/3c347244-1b33-462f-9364-ed3ac6baaf37)

![image](https://github.com/gufreschi/gaalk-django/assets/142360744/f51e908a-29b6-4168-8ac6-87523d5f16df)
