# Ride Analytics - Plataforma de Avaliação e Rankings de ROMs

![GitHub top language](https://img.shields.io/github/languages/top/nftsz/star-feedback)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/nftsz/star-feedback/main)

**Ride Analytics** é uma plataforma para descobrir, avaliar e (futuramente) compartilhar experiências com ROMs de jogos para consoles e emuladores.
Com ele, você pode visualizar detalhes das ROMs, ver notas médias baseadas em avaliações da comunidade e explorar as mais bem avaliadas ou recém-adicionadas. 

O projeto nasceu com o objetivo acadêmico de criar um sistema de feedback com estrelas, onde usuários poderiam avaliar produtos ou serviços e visualizar uma média dinâmica de notas exibida de forma visualmente atraente com estrelas preenchidas em tempo real.
Decidimos expandir esse conceito para o universo dos jogos, especificamente das ROMs, transformando a aplicação em uma plataforma de avaliações de jogos clássicos.

## 🔨 Funcionalidades

1. Avaliação de ROMs com sistema de estrelas (1 a 5) em tempo real
2. Cálculo automático da média das avaliações e exibição dinâmica com estrelas preenchidas
3. Visualização das ROMs com capa, sinopse, estúdio e galeria de imagens
4. Ranking de **Top Rated** (mais bem avaliadas) e **Recent Added** (recentemente adicionadas)

## ⚙️ Tecnologias Utilizadas

1. **Backend:** Django + Django ORM
2. **Banco de Dados:** PostgreSQL em Docker
3. **Frontend:** HTML5, CSS3 e JavaScript
4. **Imagens:** Gerenciadas com ImageField e organizadas por pasta do jogo
### 🚀 Como Rodar o Projeto

#### 1. Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
#### 2. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/ride-analytics.git
cd ride-analytics
```

#### 3. Subir os containers

```bash
docker-compose up --build
```

Isso vai:

- Criar o container do **PostgreSQL**
- Criar o container do **Django** conectado ao banco
- Rodar o servidor local na porta `8000`

Acesse em: [http://localhost:8000/home/](http://localhost:8000/home/)

## 📃  Próximos Passos

- Sistema de autenticação (login/registro) para avaliações personalizadas
- Sistema de comentários nas ROMs
- Melhorias no design da UI/UX
- Possibilidade de usuários solicitarem suas próprias ROMs

## 💞 Contribuição

Contribuições são super bem-vindas!  
Abra uma issue ou envie um pull request com melhorias, correções ou novas ideias.
