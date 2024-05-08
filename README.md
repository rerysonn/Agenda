# Agenda Django

Um projeto de agenda desenvolvido em Python utilizando o framework Django. Este projeto inclui várias funcionalidades do Django, como autenticação de usuários, CRUD de contatos na agenda, registro de novos usuários e segurança para garantir que os usuários só possam modificar os contatos que criaram.

## Índice

1. [Visão Geral](#visão-geral)
2. [Funcionalidades](#funcionalidades)
3. [Instalação e Execução Local](#instalação-e-execução-local)
4. [Utilização](#utilização)
5. [Tecnologias Utilizadas](#tecnologias-utilizadas)
6. [Contribuição](#contribuição)
7. [Licença](#licença)
8. [Capturas de Tela](#capturas-de-tela)


## Visão Geral

O projeto **Agenda Django** é uma aplicação web desenvolvida para gerenciamento de contatos. Ele fornece uma interface intuitiva para os usuários criarem, visualizarem, editarem e excluírem contatos em uma agenda pessoal. Além disso, a aplicação possui um sistema de autenticação robusto para garantir a segurança das informações dos usuários.

## Funcionalidades

- Autenticação de usuários: Os usuários podem se cadastrar, fazer login e logout.
- CRUD de contatos: Os usuários podem adicionar, visualizar, editar e excluir contatos na agenda.
- Restrição de acesso: Cada usuário só pode visualizar, editar e excluir os contatos que criou.
- Campo de pesquisa de usuários existentes.

## Instalação e Execução Local

Para executar este projeto localmente, siga estas etapas:

1. Certifique-se de ter Python e pip instalados em seu sistema.

2. Clone este repositório para o seu ambiente local usando o Git:
```git clone https://github.com/seu-usuario/nome-do-repositorio.git```

3. Navegue até o diretório do projeto:
```cd nome-do-repositorio```

4. Crie e ative um ambiente virtual:
```python -m venv .venv```

5. Ative o ambiente virtual:  
  * Windows
  ```.\.venv\Scripts\activate```
  * Linux/Mac
  ```source .venv/bin/activate ```

6. Instale as dependências necessárias usando pip:
```pip install -r requirements.txt```

7. Execute as migrações do banco de dados:
```python manage.py migrate```

8. Inicie o servidor de desenvolvimento:
```python manage.py runserver```

9. Abra seu navegador e acesse a aplicação em [http://localhost:8000/](http://localhost:8000/).

## Utilização

### Cabeçalho de usuário não logado:

- **Login**: Permite que os usuários entrem em suas contas.
- **Register**: Permite que novos usuários se cadastrem na plataforma.

![image](https://github.com/rerysonn/Django_Agenda/assets/119504068/9ba89cb7-c186-43d5-9b10-aec1eb3d2be9)


Os contatos existentes estão disponíveis para visualização.

### Cabeçalho de usuário logado:

- **Create contact**: Permite que os usuários criem novos contatos na agenda.
- **Profile**: Permite que os usuários visualizem e atualizem seu perfil.
- **Logout**: Permite que os usuários saiam de suas contas.

![image](https://github.com/rerysonn/Django_Agenda/assets/119504068/14791bef-7b96-4cf9-8577-b3945d0a051c)


Os contatos podem ser visualizados, e apenas o criador do contato pode atualizá-lo ou excluí-lo.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do backend.
- **Django**: Framework utilizado para o desenvolvimento da aplicação web.
- **HTML e CSS**: Utilizados para o desenvolvimento do frontend da aplicação.

---

### Capturas de Tela

![image](https://github.com/rerysonn/Django_Agenda/assets/119504068/c02e9143-612d-492e-8cfe-f3c6fc912c1f)

*Figura 1: Página inicial da Agenda*

![image](https://github.com/rerysonn/Django_Agenda/assets/119504068/12d4c909-5e37-4ea5-9603-7098c7e7ff81)

*Figura 2: Adicionar um novo contato*

* **Atenção:**
Os contatos existentes estão disponíveis para visualização. É importante observar que os contatos mostrados nas imagens e na base de dados são fictícios e foram gerados automaticamente através da biblioteca Faker.

---

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, por favor, siga estas etapas:

1. Faça um fork do repositório e clone-o em seu ambiente local.
2. Crie uma branch para sua nova feature: `git checkout -b feature-nova`.
3. Faça suas alterações e comite-as: `git commit -am 'Adicione sua nova feature'`.
4. Envie para o repositório original: `git push origin feature-nova`.
5. Crie um novo Pull Request.
   

Além disso, se você deseja entrar em contato:

- Nome: Reryson Farinha
- Linkedin: www.linkedin.com/in/reryson-farinha


## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).



