### Descrição do Projeto

# Projeto desenvolvido para o desafio técnico de Auxiliar de Desenvolvimento Jr Frontend.

O objetivo foi criar uma interface para monitoramento de robôs RPA, permitindo visualizar:

- Lista de robôs
- Status do último resultado
- Data da última execução
- Detalhes do robô
- Histórico de execuções
- Logs das execuções

## Tecnologias Utilizadas
- React
- Vite
- React Router Dom
- Axios
- TailwindCSS

## Como Executar

### 1. Tenha Python 3.10+ instalado, não precisa instalar nada — só usa a biblioteca padrão do Python
python --version

### 2. Rode o servidor:
python servidor2.py, baixavel no Github:

A API ficará disponível em http://localhost:8000.
Os dados são fictícios e gerados na inicialização.

### 3. Acesse:  
https://testerpa.netlify.app/ ou


### 4. Permita o site acessar seu localhost:
![permita](docs/permissão.png)

## Estrutura do Projeto
    src
    │
    ├── pages
    │   ├── BotsPage
    │   └── DetailsPage
    │
    ├── components
    │   ├── ui
    │   └── ux
    │
    ├── data
    │   ├── api.js
    │   ├── service.js
    │   └── Routes.jsx
    │
    ├── utils
        └── filterBots.js


## Decisões

### React + Vite

Escolhi React + Vite pela rapidez de configuração e desenvolvimento.

### Axios

Utilizado para facilitar e centralizar todas as chamadas da API em um único serviço.
Isso facilitou:
- manutenção
- reutilização
- legibilidade

### TailwindCSS

Escolhi Tailwind para acelerar a construção da interface e manter os estilos organizados.
A abordagem baseada em utilitários me permitiu ajustar rapidamente:

- Responsividade
- Mudanças e decições Visuais


---

## Planejamento da API

Esse foi um rascunho que fiz antes de começar a implementação para entender melhor como usar o Axios e organizar as chamadas da API.

![Planejamento da API](./docs/apiplan.jpeg)

Nem tudo estava correto na Sintaxe, mas ele me ajudou a visualizar a estrutura antes de começar a codar. Os ajustes foram feitos durante a implementação como o AutoComplete do VSCode.

---

## Primeiras Ideias de Interface

Na primeira conversa com Daniel, anotei algumas informações sobre o funcionamento dos RPAs e sobre a necessidade de acompanhar robôs, execuções e logs. Assim que pude, pesquisei um pouco mais sobre para entender melhor o funcionamento.

![Interface](./docs/Interface1.jpeg)

Oque me ajudou a montar a interface e seus rascunhos para organizar as informações na tela.
A ideia principal foi deixar fácil encontrar um robô, visualizar suas execuções e acessar os logs e dar espaço pra escalabilidade.

---

## Organização Inicial

Também fiz um rascunho da estrutura do projeto antes de começar a implementação.

![Organização](./docs/OrganizaçãoInicial.jpeg)

A estrutura mudou um pouco durante o desenvolvimento, mas serviu como base para organizar páginas, componentes e serviços.

Inicialmente pensei em utilizar uma tabela, já que o próprio desafio menciona uma listagem de robôs.

Durante os rascunhos percebi que os cards facilitavam a identificação visual do status de cada robô e deixavam as informações mais separadas. Para mim ficou mais rápido localizar um robô com problema do que em um formato parecido com planilha.

Por esse motivo optei por utilizar cards na tela principal.

## Dificuldades Encontradas

A principal dificuldade foi entender a organização das chamadas da API utilizando Axios e como distribuir as responsabilidades entre páginas, componentes, serviços, E principalmente na distribuição de rotas que tenho dificuldade em decorar, mas logo matei esses problemas com pesquisas no ChatGPT e com documentos e intruçoes na web.

![Organização](./docs/DuvidaRotas.png)
![Organização](./docs/Axios.png)

Também tive dificuldade inicial para estruturar os componentes React, principalmente entendendo quando criar componentes separados e quando manter algo na própria página.

Para auxiliar no desenvolvimento, realizei alguns rascunhos antes de iniciar a implementação.
### Após as pesquisas e testes consegui separar de forma mais organizada:
- configuração da API
- serviços
- componentes

Componentização

Outro desafio foi decidir:

quando criar um componente
quando manter a lógica dentro da página

### Durante o desenvolvimento algumas partes foram refatoradas para componentes específicos:

- CardBot
- ExecutionList
- ExecutionItem
- LogsList
- RobotInfo

Isso deixou o código mais reutilizável e fácil de manter num modelo:
### UX (Experiência do Usuário) e UI (Interface do Usuário)
Nunca vi alguem utilizar, mas funcionou bem para mim

## Ajustes e Validações

Durante o desenvolvimento realizei diversos testes visuais para verificar:

- alinhamentos
- status
- responsividade
- legibilidade
- Ajuste dos Status

---

# Resultado Final
## Tela Principal
![Tela](docs/TelaPrincipalD.png)

## Tela de Detalhes
![Tela](docs/DetailsD.png)

---

# Uso de Inteligência Artificial

## Durante o desenvolvimento utilizei ChatGPT e Gemini como ferramenta de apoio e usos:

- esclarecimento de dúvidas sobre React Router
- organização de componentes
- validação de ideias de arquitetura
- auxílio na resolução de erros
- consulta de boas práticas

## Todas as decisões finais de implementação, estrutura e interface foram revisadas e adaptadas por mim durante o desenvolvimento.
## Além do ChatGPT, também utilizei pesquisas em documentações oficiais e buscas na web para confirmar comportamentos e sintaxes.

---

# Melhorias Futuras

## Caso o projeto continuasse evoluindo ou tivesse mais tempo, eu adicionaria:

- filtros avançados por status(com um icone rápido)
- tema escuro
- robos com erros aparecerem no topo da lista
- gráficos
- notificações de falhas