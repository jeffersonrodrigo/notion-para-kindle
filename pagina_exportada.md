[https://mylearn.oracle.com/ou/ekit/148111/35644/90da110a-5f86-4d90-af98-37230bb9a5b3/course](https://mylearn.oracle.com/ou/ekit/148111/35644/90da110a-5f86-4d90-af98-37230bb9a5b3/course)

### **Arquitetura Física do OCI (Core Constructs)**

### **1. Conceitos Fundamentais (A Hierarquia)**

A arquitetura física do OCI é construída em três níveis, um dentro do outro. É crucial entender a função de cada um.

- **Região (Region):**
  - **O que é?** A camada mais alta. Uma área geográfica específica no mundo (ex: Leste dos EUA, São Paulo, Frankfurt).
  - **Composição:** Contém um ou mais *Availability Domains*.
  - **Ponto Chave:** É o primeiro nível de isolamento geográfico.

- **Availability Domain (AD):**
  - **O que é?** Um ou mais data centers independentes e tolerantes a falhas, localizados *dentro de uma Região*.
  - **Principal Característica:** São **totalmente isolados** uns dos outros. Não compartilham energia, refrigeração ou rede interna.
  - **Benefício:** Uma falha em um AD (como uma queda de energia no data center) **não afetará** os outros ADs na mesma região. Isso garante alta disponibilidade.

- **Fault Domain (FD):**
  - **O que é?** A camada mais granular. É um agrupamento de hardware e infraestrutura *dentro de um Availability Domain*.
  - **Analogia Fácil:** Pense no AD como um prédio (data center) e os FDs como 3 "racks" ou conjuntos de servidores separados em andares diferentes. Cada FD tem sua própria energia e switches.
  - **Regra de Ouro:** Cada Availability Domain possui **3 Fault Domains**.
  - **Benefício:** Protege contra falhas de hardware dentro de um mesmo AD. Se um rack falhar, sua aplicação continua rodando nos outros FDs.

### **2. Como Escolher uma Região? (3 Critérios Essenciais)**

Você precisa escolher a região certa para sua aplicação com base em:

1. **Latência:** Escolha a região mais próxima dos seus usuários para obter o melhor desempenho e a menor latência.

1. **Soberania de Dados (Data Residency) e Compliance:** Leis locais podem exigir que os dados dos seus clientes permaneçam em um país específico.

1. **Disponibilidade de Serviços (Service Availability):** Nem todos os serviços do OCI estão disponíveis em todas as regiões, especialmente os mais novos.

### **3. Como Usar esses Conceitos para Alta Disponibilidade (High Availability - HA)**

O objetivo é **evitar Pontos Únicos de Falha** (*Single Points of Failure*).

- **Estratégia 1 (Dentro de 1 AD):**
  - Distribua as instâncias da sua aplicação (ex: 2 servidores web) em **Fault Domains diferentes**.
  - Se o hardware do FD1 falhar, a instância no FD2 continua operando.

- **Estratégia 2 (Entre ADs - Máxima Proteção):**
  - Replique sua arquitetura inteira em um **segundo Availability Domain**.
  - Você terá a aplicação e o banco de dados rodando no AD1 (distribuídos entre FDs) e uma cópia exata rodando no AD2.
  - Para sincronizar os bancos de dados, use ferramentas como o **Oracle Data Guard**.
  - Isso protege até mesmo contra a falha completa de um data center.

**Resumo para Memorizar:**

- **Região > Availability Domain > Fault Domain**

- **Fault Domain (FD):** Protege contra falha de **hardware** (dentro de um AD).

- **Availability Domain (AD):** Protege contra falha de um **data center inteiro** (dentro de uma Região).

- **Região (com outra Região par):** Protege contra **desastres geográficos**.

---

### **Um Tour pela Console do OCI**

A Console do OCI é a interface web para gerenciar todos os seus recursos na nuvem. Entender sua estrutura é fundamental.

### **1. Acesso e Página Inicial**

- **URL de Acesso:** `cloud.oracle.com`

- **Login:** Requer seu **Nome da Tenancy** (Cloud Account Name), **Usuário** e **Senha**.

- **Página Inicial (Dashboard):** É a primeira tela que você vê. Oferece:
  - Links de "Início Rápido" (Quick Starts).
  - Atalhos para criar os recursos mais comuns (instâncias, redes, etc.).

### **2. Navegação Principal (Menu "Hambúrguer" ☰)**

- **Localização:** Ícone com três linhas no canto superior esquerdo.

- **Função:** É a principal forma de encontrar **todos os serviços** do OCI.

- **Organização:** Os serviços são agrupados em categorias lógicas para facilitar a localização:
  - *Core Infrastructure:* Compute, Storage, Networking.
  - *Database:* Oracle Database, MySQL, etc.
  - *Identity & Security*, *Developer Services*, etc.

### **3. Barra de Ferramentas Global (Topo da Página)**

Esta barra contém ferramentas essenciais que funcionam de forma global, independentemente do serviço que você está visualizando.

- **Busca (Search):**
  - Permite procurar por recursos que você já criou (ex: uma instância específica).
  - Mostra links diretos para a documentação e para as páginas de serviço.
  - **Ponto Importante:** Suporta "Busca Avançada de Recursos" (*Advanced Resource Query*) para fazer consultas detalhadas (ex: `search resources where type = 'instance' and lifecycleState = 'RUNNING'`).

- **Regiões (Regions):**
  - Mostra em qual região você está trabalhando atualmente (ex: `us-ashburn-1`).
  - Permite **trocar de região** facilmente. Ao trocar, toda a console passa a exibir os recursos da nova região selecionada.
  - Permite **gerenciar e se inscrever** em novas regiões para sua tenancy.

- **Anúncios (Announcements - Ícone de Megafone):**
  - Informa sobre novos recursos, atualizações de serviços e manutenções programadas. É o canal oficial de comunicação da Oracle dentro da console.

- **Ajuda (Help - Ícone de "?")**
  - Oferece links para a documentação, centro de suporte e fóruns.
  - Permite **abrir um chamado de suporte (Service Request)**.
  - Permite solicitar **aumento de limites de serviço (Service Limit Increase)**.
  - Inclui um **Assistente de Chat ao Vivo (Live Chat Assistant)**.

- **Ferramentas de Desenvolvedor (Developer Tools)**
  - **Cloud Shell (>_):**
    - **O que é?** Um **terminal Linux gratuito** que roda diretamente no navegador, dentro da console.
    - **Vantagem Principal:** Já vem com as ferramentas mais importantes pré-instaladas e **automaticamente autenticadas** (OCI CLI, Git, Java, Python, etc.). Elimina a necessidade de configurar tudo no seu computador.
  - **Code Editor:**
    - **O que é?** Um editor de código integrado à console.
    - **Utilidade:** Ótimo para fazer edições rápidas em scripts (ex: Terraform para o Resource Manager, código de Functions) sem precisar sair da console.

### **4. Outras Áreas Importantes**

- **Painel de Saúde (Health Dashboard):** Link na parte de baixo da página. Mostra o status operacional de todos os serviços OCI em todas as regiões. Use-o para verificar se há alguma instabilidade geral.

- **Informações da Tenancy e Custo:** No menu do seu perfil (canto superior direito), você pode ver o nome da sua tenancy e acessar relatórios de custo e uso.

**Resumo para Memorizar:**

- **Menu Hambúrguer ☰:** A porta de entrada para **todos os serviços**.

- **Seletor de Região:** Ferramenta **global** para trocar o contexto geográfico.

- **Cloud Shell (>_):** Seu **terminal Linux na nuvem**, já configurado e pronto para usar.

- **Code Editor:** Edição de código **rápida** sem sair do navegador.

- **Barra de Busca:** Encontra recursos e permite **consultas avançadas**.

---

# **Identity and Access Management**

## **Visão Geral de Identity and Access Management (IAM)**

O serviço de IAM é a base da segurança no OCI. Ele controla de forma granular **quem** pode fazer **o quê**.

### Os 2 Pilares Fundamentais do IAM 🔐

Todo o serviço se baseia em dois conceitos centrais:

- **Autenticação (Authentication - AuthN):**
  - **Pergunta que responde:** "Quem é você?" 🤔
  - **Função:** É o processo de **verificar a identidade** de um usuário ou serviço. Geralmente, isso é feito através de um nome de usuário e senha, chaves de API, ou outros métodos de verificação.

- **Autorização (Authorization - AuthZ):**
  - **Pergunta que responde:** "O que você tem permissão para fazer?" ✅
  - **Função:** Ocorre **após** a autenticação. É o processo de definir quais ações um usuário já identificado pode realizar e em quais recursos (ex: "O usuário 'Bob' pode iniciar e parar instâncias, mas não pode deletá-las").

> Analogia Simples: Autenticação é mostrar seu crachá para entrar no prédio. Autorização é o que está escrito no seu crachá que diz quais portas você pode abrir lá dentro.

---

### Como o IAM Funciona na Prática: Os Componentes

O IAM utiliza alguns componentes chave para organizar o acesso:

- **Identity Domain:** Pense nisso como um **"contêiner" para seus usuários e grupos**. É a estrutura que representa uma população de usuários e suas configurações de segurança associadas (como políticas de senha e MFA).

- **Usuários e Grupos (Users & Groups):**
  - **Usuários:** As identidades individuais (sejam pessoas ou aplicações).
  - **Grupos:** Coleções de usuários. A **melhor prática** é sempre dar permissões a **grupos**, e não a usuários individuais, para facilitar o gerenciamento.

- **Compartimentos (Compartments):** São como **"pastas" lógicas** para organizar e isolar seus recursos na nuvem (VMs, bancos de dados, redes). O acesso aos recursos é controlado no nível do compartimento.

- **Políticas (Policies):** São as **regras que unem tudo**. Uma política determina qual `**Grupo**` tem qual tipo de `**Permissão**` em qual `**Compartimento**`.

### OCID (Oracle Cloud ID): A "Placa de Identidade" dos Recursos 🆔

- **O que é?** Um identificador **único e universal** que a Oracle atribui automaticamente a **TODO** e qualquer recurso criado na nuvem (instâncias, redes, volumes, e até mesmo sua conta, que é a *tenancy*).

- **Quando você o usa?** Você raramente o usa diretamente na console web, mas ele é **essencial** ao interagir com a nuvem via **CLI (Command Line Interface)** ou **SDKs (Software Development Kits)**.

- **Sintaxe do OCID:**`ocid1.<tipo_do_recurso>.<realm>.[região].<id_único>`
  - `**tipo_do_recurso**`: Define o que é o recurso (ex: `instance`, `volume`, `tenancy`).
  - `**realm**`: Um conjunto de regiões. `oc1` é o *realm* comercial padrão.
  - `**região**`: O código da região onde o recurso existe. É opcional para recursos globais como a *tenancy*.
  - `**id_único**`: A parte final que garante que o ID seja exclusivo.

---

## **Compartimentos (Compartments) no OCI**

Compartimentos são a principal forma de **organizar e isolar** seus recursos na nuvem do OCI.

### O Que São Compartimentos? 📁

Pense neles como **pastas lógicas** dentro da sua conta (Tenancy). Quando você cria uma conta, ela já vem com um compartimento principal chamado **Compartimento Raiz (Root Compartment)**.

Embora você *possa* colocar todos os seus recursos no compartimento *Root*, a **melhor prática é criar seus próprios compartimentos** para separar e organizar os recursos (ex: um compartimento para a equipe de rede, outro para a de desenvolvimento, etc.).

---

### Por Que Usar Compartimentos? (Os 2 Motivos Principais)

1. **Controle de Acesso:** É a razão fundamental. Você usa **Políticas (Policies)** para dar a um **Grupo** de usuários permissões para gerenciar recursos dentro de um **Compartimento** específico.
  - *Exemplo:* O grupo `NetworkAdmins` só pode gerenciar recursos no compartimento `Networking`.

1. **Organização e Isolamento Lógico:** Permite agrupar recursos relacionados, facilitando a gestão. Isso ajuda a espelhar a estrutura da sua empresa ou de seus projetos.

---

### Características e Regras Essenciais 🧠

- **Um Recurso, Um Compartimento:** Um recurso (como uma VM) só pode estar em **um** compartimento por vez.

- **Recursos Podem Ser Movidos:** Você pode mover a maioria dos recursos de um compartimento para outro, se necessário.

- **Interação entre Compartimentos:** Recursos em compartimentos diferentes **podem se comunicar** normalmente, desde que as políticas de segurança e de rede permitam. Uma VM no compartimento `App` pode usar uma rede (VCN) que está no compartimento `Network`.

- **Compartimentos são GLOBAIS:** Isso é **muito importante!** Um compartimento não pertence a uma região específica. Ele está visível e disponível em **todas as regiões** da sua tenancy.

- **Aninhamento (Nesting):** Você pode criar uma hierarquia de compartimentos, um dentro do outro, com até **6 níveis de profundidade**.

---

### Governança com Compartimentos 💰

Compartimentos também são a base para aplicar controles de governança:

- **Cotas (Quotas):** Permitem limitar o uso de recursos.
  - *Exemplo:* "No compartimento `Test`, só é permitido criar no máximo 10 VMs do tipo `VM.Standard.E4.Flex`."

- **Orçamentos (Budgets):** Permitem monitorar os gastos e definir alertas.
  - *Exemplo:* "Me avise por e-mail se o custo dos recursos no compartimento `Development` ultrapassar R$ 500,00 este mês."

---

### **Demo: Criando Compartimentos e Identity Domains**

Esta demo mostra o processo prático de criação de um compartimento para organizar recursos e um *Identity Domain* para gerenciar usuários de forma isolada.

## Revisão Rápida dos Conceitos 🎯

- **Compartimentos:** Contêineres lógicos para seus **recursos** (VMs, redes, bancos de dados).

- **Identity Domains:** Contêineres para seus **usuários, grupos e configurações de segurança** (como MFA e políticas de senha).

---

## Passo a Passo: Criando um Compartimento 🧑‍💻

A demonstração mostra como criar um compartimento chamado `sandbox`.

1. **Navegação:** Vá para o menu principal ☰ **Identity & Security** e clique em **Compartments**.

1. **Ação:** Clique no botão **Create Compartment**.

1. **Preenchimento:**
  - **Name:** Dê um nome claro (ex: `sandbox`).
  - **Description:** Adicione uma descrição para explicar o propósito do compartimento.
  - **Parent Compartment:** Escolha onde ele ficará na hierarquia (geralmente sob o compartimento *Root* ou outro já existente).

1. **Confirmação:** Clique em **Create Compartment**.

> Dica da Demo: Para visualizar todos os recursos que existem dentro de um compartimento, você pode usar a ferramenta Tenancy Explorer.

---

### Passo a Passo: Criando um Identity Domain 🔑

O objetivo é criar um domínio chamado `sandbox domain` para isolar um conjunto de usuários.

1. **Navegação:** Vá para o menu principal ☰ **Identity & Security** e clique em **Domains**.

1. **Ação:** Clique no botão **Create domain**.

1. **Preenchimento:**
  - **Display Name:** Dê um nome (ex: `sandbox domain`).
  - **Domain type:** Escolha o tipo. A opção **Free** é a padrão e suficiente para os estudos da certificação.
  - **Compartment:** Escolha em qual compartimento o próprio recurso do *Identity Domain* será criado (na demo, foi mantido no *Root*).

1. **Confirmação:** Clique em **Create domain**.

---

### Pontos Chave e Melhores Práticas 💡

- **Hierarquia é Tudo:** A demo reforça que compartimentos podem ser aninhados (até **6 níveis**), permitindo que você crie uma estrutura que reflita perfeitamente sua organização.

- **Isolamento de Identidades:** Criar um novo *Identity Domain* é a forma ideal de separar completamente os usuários de um ambiente (ex: produção vs. teste). Um domínio recém-criado sempre começa com **zero usuários e zero grupos**.

- **Caso de Uso Prático:** Um time de projeto temporário pode ter seus usuários criados em um *Identity Domain* separado. Quando o projeto termina, o domínio pode ser desativado ou removido, limpando todos os acessos de uma só vez.

---

## **Autenticação e Autorização no OCI**

### Principals: Quem Pode Agir no OCI? 👤

Primeiro, vamos definir quem precisa de acesso. Um **Principal** é qualquer entidade do IAM que pode interagir com os recursos do OCI.

- **Tipos de Principals:**
  - **Usuários (Users):** Pessoas (humanos) que acessam a console, CLI ou SDKs.
  - **Instance Principals:** Um recurso agindo como um principal. O exemplo clássico é uma **instância de compute (VM)** que recebe permissão para fazer chamadas de API a outros serviços (ex: uma VM lendo um arquivo do Object Storage sem precisar de credenciais de um usuário).

- **Grupos (Groups):** São coleções de *principals* (geralmente usuários). São a base para a autorização, pois as permissões são concedidas a grupos, e não a usuários individuais.

---

## Autenticação (AuthN): Provando Quem Você É 🧐

O OCI precisa verificar a identidade de um *principal* antes de permitir qualquer acesso. Existem três métodos principais para isso:

1. **Nome de Usuário e Senha:** O método clássico, usado principalmente para o login na **console web**.

1. **Chaves de API (API Signing Keys):** Um par de chaves criptográficas RSA (pública/privada). É o método padrão para autenticar chamadas feitas pela **CLI (Command Line Interface)** ou por **SDKs (Software Development Kits)**, ideal para automação.

1. **Tokens de Autenticação (Auth Tokens):** São "senhas" específicas geradas pela Oracle. São usadas para autenticar com serviços de terceiros que não suportam o modelo de autenticação padrão do OCI.

---

## Autorização (AuthZ): Definindo o Que Você Pode Fazer ✅

Depois que um *principal* é autenticado, a autorização define o que ele pode fazer. No OCI, isso é controlado exclusivamente por **Políticas (Policies)**.

- **Princípio Fundamental:** **Negação por padrão (Deny by default)**. Ninguém tem permissão para nada até que uma política explicitamente permita.

### A Sintaxe da Policy Descomplicada

As políticas são frases simples e legíveis que seguem uma estrutura clara:

`Allow group <nome-do-grupo> to <verbo> <tipo-de-recurso> in <localização>`

- `**Allow**`: Toda política começa com `Allow`. Não existe a instrução `Deny`.

- `**group <nome-do-grupo>**`: Políticas são sempre aplicadas a **grupos**, nunca a usuários individuais.

- `**<verbo>**`: Define o nível de permissão (veja abaixo).

- `**<tipo-de-recurso>**`: O recurso que a política afeta (ex: `all-resources`, `instance-family`, `databases`).

- `**<localização>**`: Onde a política é válida: em toda a `**tenancy**` (a conta inteira) ou em um `**compartment <nome-do-compartimento>**` específico.

### Os 4 Verbos de Permissão (Do Menos para o Mais Poderoso)

- `inspect`: Permite listar recursos e ver seus metadados, mas sem acessar os dados em si.

- `read`: Inclui `inspect` + a permissão para ler os dados do recurso (ex: baixar um arquivo do Object Storage).

- `use`: Inclui `read` + a permissão para trabalhar com recursos existentes (ex: iniciar/parar uma VM), mas não para criar ou deletar.

- `manage`: Permissão total. Inclui `use` + permissão para criar e deletar recursos.

---

### **O Ciclo Completo de AuthN e AuthZ**

Esta demonstração prática mostra a diferença fundamental entre Autenticação (provar quem você é) e Autorização (o que você pode fazer).

## 1. Preparação: Criando o Usuário e o Grupo 🧑‍🔧

O primeiro passo é configurar as identidades dentro do **Identity Domain** `Sandbox Domain`.

1. **Criar o Usuário:**
  - Navegação: `Identity & Security` -> `Domains` -> `Sandbox Domain` -> `Users`.
  - Ação: Clicar em **Create user**.
  - Dados: Preencher nome (`OCI Admin`) e e-mail.
  - **Ponto Chave:** O usuário é criado, mas ainda não pertence a nenhum grupo.

1. **Criar o Grupo e Adicionar o Usuário:**
  - Navegação: Na mesma tela do domínio, ir para `Groups`.
  - Ação: Clicar em **Create group**.
  - Dados: Dar um nome (`OCI Admin group`).
  - **Ação Crucial:** Durante a criação do grupo, adicionar o usuário `OCI Admin` como membro. **Lembre-se: permissões são dadas a grupos, não a usuários.**

## 2. Autenticação (AuthN): O Login do Novo Usuário 🔑

Agora, o usuário `OCI Admin` precisa acessar o sistema pela primeira vez.

1. **Ativação:** O usuário recebe um e-mail para **ativar a conta**.

1. **Definir Senha:** Ao clicar no link, o usuário é direcionado para criar sua senha. A tela de login já mostra que ele pertence ao `sandbox-domain`.

1. **Processo de Login:**
  - Acessar a URL da console (`cloud.oracle.com`).
  - Digitar o **Nome da Tenancy**.
  - **Selecionar o Identity Domain correto (**`**sandbox domain**`**)**.
  - Digitar o nome de usuário (`ociadmin`) e a senha recém-criada.

Ao final, o usuário está logado. O perfil no canto superior direito confirma a identidade. **Isso completa o processo de Autenticação.**

## 3. A Realidade Pós-Login: Autenticado, Mas Sem Permissão 🚫

Este é o ponto mais importante da demo:

- O usuário `ociadmin` consegue ver a console e a lista de serviços.

- Porém, ao tentar listar ou criar qualquer recurso (instâncias, buckets, etc.), ele recebe uma **mensagem de erro de autorização**.

- **Lição:** Apenas se autenticar não dá direito a fazer nada. Por padrão, um usuário novo tem **zero permissões**.

## 4. Autorização (AuthZ): Dando Poder com uma Policy ✍️

Para resolver isso, o administrador da tenancy cria uma política de permissão.

1. **Navegação:** `Identity & Security` -> `Policies`. (Note que as políticas são criadas fora dos *Identity Domains*).

1. **Ação:** Clicar em **Create Policy**.

1. **Usando o Policy Builder (o jeito fácil):**
  - **Identity Domain:** Selecionar `sandbox domain`.
  - **Group:** Selecionar `OCI Admin group`.
  - **Location:** Selecionar o `sandbox` **compartment**.
  - **Policy Use Case:** Escolher um modelo, como `Storage Management`, que gera as permissões automaticamente.

1. **Resultado:** O construtor gera a política:
`Allow group sandbox-domain/OCI-Admin-group to manage object-family in compartment sandbox`

1. A política é criada e ativada.

## 5. A Prova Final: Testando as Permissões ✅

De volta à sessão do usuário `ociadmin`:

- **Teste Negativo:** Tentar acessar recursos de *Compute* continua falhando, pois a política não deu essa permissão.

- **Teste Positivo:**
  - Ir para `Storage -> Object Storage`.
  - **Mudar o escopo do compartimento** para `sandbox` no menu à esquerda.
  - Agora, o botão **Create Bucket** funciona, e o usuário consegue criar um bucket com sucesso **apenas neste compartimento**.
  - Tentar criar um bucket no compartimento *Root* falha, provando que a política está corretamente limitada ao compartimento `sandbox`.

---

### **Configurando sua Tenancy (Melhores Práticas)**

Configurar sua tenancy (sua conta OCI) corretamente desde o início é crucial para a segurança e a governança. A Oracle recomenda três práticas fundamentais.

## As 3 Melhores Práticas de Segurança para sua Conta OCI 🛡️

1. **Não use o Administrador da Tenancy para o dia a dia.**
  - O usuário que cria a conta (o "root") é extremamente poderoso. Ele não deve ser usado para tarefas administrativas rotineiras.
  - **Ação:** Crie um grupo separado (ex: `OCI-Admins`) para as tarefas do dia a dia e guarde o usuário administrador principal para emergências.

1. **Crie Compartimentos Dedicados.**
  - **Nunca** coloque todos os seus recursos no compartimento *Root*. Isso dificulta o controle de acesso e a organização.
  - **Ação:** Use compartimentos para **isolar e organizar** seus ambientes (produção, desenvolvimento), projetos ou unidades de negócio.

1. **Exija a Autenticação Multifator (MFA).**
  - Adicione uma camada extra de segurança ao processo de login.
  - **Ação:** Ative o MFA para que os usuários precisem de um segundo fator de verificação (como um código no celular) além da senha para acessar a conta.

---

## Delegando Poder: Políticas Essenciais para o Grupo de Administradores ✍️

Para que o novo grupo `OCI-Admins` possa, de fato, administrar a conta, ele precisa de permissões específicas. E aqui está o ponto mais importante da aula:

### Permissão para Gerenciar Recursos Gerais

Primeiro, o grupo precisa de permissão para gerenciar os recursos da nuvem (VMs, redes, storage, etc.). Isso é feito com uma política ampla:

`Allow group OCI-Admins to manage all-resources in tenancy`

*(Lembre-se: essa política pode ser mais restrita, aplicando-se a um compartimento específico em vez de a toda a tenancy, se necessário).*

### Permissão para Gerenciar o Próprio IAM (Ponto Crítico!)

A permissão `all-resources` **NÃO** inclui a capacidade de gerenciar usuários, grupos ou as próprias políticas. O serviço de IAM (Identity and Access Management) possui tipos de recursos separados que precisam ser permitidos explicitamente.

**Não existe um tipo de recurso agregado para o IAM.** Você precisa criar uma política para cada tipo de recurso que o grupo de administradores precisa gerenciar. As políticas essenciais são:

- `Allow group OCI-Admins to manage users in tenancy`

- `Allow group OCI-Admins to manage groups in tenancy`

- `Allow group OCI-Admins to manage policies in tenancy`

- `Allow group OCI-Admins to manage domains in tenancy`

- `Allow group OCI-Admins to manage compartments in tenancy`

Sem essas políticas, seu novo grupo de administradores não conseguirá criar novos usuários, gerenciar grupos ou delegar permissões a outros.

---

# **Networking**

## **Introdução à Virtual Cloud Network (VCN)**

### O que é uma VCN? 🌐

A **Virtual Cloud Network (VCN)** é a sua **rede privada e customizável** na nuvem da Oracle. Pense nela como uma versão virtual do seu data center tradicional, mas definida por software.

- **Características Principais:**
  - É um serviço **Regional** (vive dentro de uma única região do OCI).
  - É usada para **comunicação segura** entre seus recursos.
  - É altamente disponível e escalável por padrão; você não precisa se preocupar com isso.

---

### A Estrutura de uma VCN: Do Geral para o Específico

1. **Espaço de Endereços (CIDR Block):** Ao criar uma VCN, o primeiro passo é definir um intervalo de endereços IP privados para ela (ex: `10.0.0.0/16`). Esse será o "endereço" principal da sua rede.

1. **Sub-redes (Subnets):** Você não usa o bloco inteiro de uma vez. Você o divide em pedaços menores chamados *subnets* (ex: `10.0.1.0/24` e `10.0.2.0/24`). É como dividir um grande terreno em lotes menores para construir as casas.

1. **Instâncias (Compute Instances):** Seus recursos, como máquinas virtuais, são criados **dentro das subnets**. Cada instância recebe um endereço IP privado do intervalo daquela subnet para poder se comunicar.

---

### Os Portões de Saída e Entrada da VCN (Gateways) 🚪

Gateways são roteadores virtuais que controlam como o tráfego entra e sai da sua VCN. Cada um tem uma função muito específica e é crucial saber a diferença entre eles.

### Internet Gateway (IGW) ↔️ Internet Pública

- **Função:** Permite comunicação **bidirecional** (ida e volta) entre suas instâncias e a internet.

- **Caso de Uso:** Essencial para um servidor web que precisa ser acessado por usuários da internet e também acessar a internet.

### NAT Gateway (NAT) ➡️ Internet Pública

- **Função:** Permite que suas instâncias iniciem conexões **de saída** para a internet, mas **bloqueia** qualquer conexão que seja iniciada pela internet. O tráfego é **unidirecional**.

- **Caso de Uso:** Perfeito para um banco de dados em uma subnet privada que precisa baixar atualizações de segurança (`yum update`), mas não deve ser acessível publicamente de forma alguma.

### Service Gateway (SGW) ➡️ Serviços Oracle

- **Função:** Permite que suas instâncias acessem serviços públicos do OCI (como Object Storage, Autonomous Database) **sem que o tráfego precise passar pela internet pública**. A comunicação acontece de forma privada, pela rede interna da Oracle.

- **Caso de Uso:** Uma aplicação em uma subnet privada enviando backups para o Object Storage de forma segura e com melhor performance.

### Dynamic Routing Gateway (DRG) ↔️ Sua Rede On-Premises

- **Função:** É o portão para tráfego **privado** entre sua VCN e outras redes fora da internet.

- **Caso de Uso:** É o componente que você usa para conectar sua VCN ao seu data center físico (on-premises) através de uma VPN ou FastConnect.

---

### **Demo: Criando uma VCN com o Wizard**

## O Que o VCN Wizard Faz por Você? 🧙‍♂️

O **VCN Wizard** é a forma mais **rápida e fácil** de criar uma VCN funcional no OCI. Ele automatiza a criação não apenas da rede em si, mas de todos os componentes essenciais (subnets, gateways, tabelas de rota) com uma configuração padrão e segura. É a ferramenta ideal para começar e evita erros comuns de configuração manual.

---

## Passo a Passo: Usando o VCN Wizard 🧑‍💻

1. **Navegação:** Vá para o menu ☰ **Networking** -> **Virtual Cloud Networks**.

1. **Ação Principal:** Clique no botão azul **Start VCN Wizard**.

1. **Escolha do Modelo:** Selecione a opção **"VCN with Internet Connectivity"**. Este é o modelo mais comum, que cria uma subnet pública e uma privada prontas para uso.

1. **Configuração:**
  - Dê um **nome** para a sua VCN.
  - Escolha o **compartimento** onde ela será criada.
  - Revise os **blocos CIDR** para a VCN e as subnets. Os valores padrão sugeridos pelo wizard (como `10.0.0.0/16` para a VCN e `/24` para as subnets) são adequados para a maioria dos casos de estudo e teste.

1. **Revisão e Criação:** O wizard mostrará um resumo de todos os componentes que serão criados. Apenas confirme clicando em **Create**.

---

## O Resultado: O Que Foi Criado Automaticamente? ✅

Em segundos, o wizard cria uma arquitetura de rede completa e pronta para usar. A lista de componentes criados é um ponto muito importante para a prova:

- ✅ A **VCN** principal.

- ✅ Uma **Subnet Pública**.

- ✅ Uma **Subnet Privada**.

- ✅ Um **Internet Gateway (IGW)**, associado à subnet pública.

- ✅ Um **NAT Gateway**, associado à subnet privada.

- ✅ Um **Service Gateway (SGW)**, também associado à subnet privada.

- ✅ Duas **Tabelas de Rota (Route Tables)**, uma para cada subnet, já configuradas com as rotas corretas para os gateways.

- ✅ Duas **Listas de Segurança (Security Lists)**, uma para cada subnet, com regras de firewall básicas.

## Dica da Demo: Visualizando sua Rede 📈

Após a criação, a melhor forma de entender a topologia é usando o **Network Visualizer** (encontrado em *Network Command Center*). Esta ferramenta mostra um **diagrama visual** da sua VCN, mostrando como as subnets estão conectadas aos gateways. Isso facilita muito a compreensão do fluxo de tráfego.

---

## **Roteamento na VCN (Route Tables & Peering)**

<!-- Bloco do tipo 'image' não suportado -->

## O que são Route Tables (Tabelas de Rota)? 🗺️

As **Route Tables** funcionam como o "GPS" da sua VCN. Elas contêm regras que dizem para onde enviar o tráfego que **precisa sair da VCN** (para a internet, para sua rede on-premises, ou para outra VCN).

- **Componentes de uma Route Table:**
  - **Regra de Rota (Route Rule):** Cada regra na tabela é composta por duas partes:
    1. **Destination CIDR:** O intervalo de endereços IP de destino do tráfego.
    1. **Route Target:** O "próximo salto" ou o gateway que o tráfego deve usar para chegar ao seu destino (ex: Internet Gateway, NAT Gateway, DRG).

- **Ponto Importante:** O tráfego **entre subnets dentro da mesma VCN** é roteado automaticamente pelo que chamamos de "roteamento local". Você **não precisa** criar uma regra para isso.

---

## A Regra de Ouro: A Rota Mais Específica Vence 🏆

Quando um pacote de dados precisa sair e seu destino corresponde a mais de uma regra na tabela, o OCI sempre usa a regra **mais específica**. Isso é conhecido como **"longest prefix match"** (correspondência de prefixo mais longo).

- **Exemplo da Aula:** Uma subnet privada tem duas regras de rota:
  1. **Regra 1 (Geral):** `0.0.0.0/0` (qualquer lugar na internet) -> `NAT Gateway`
  1. **Regra 2 (Específica):** `192.168.0.0/16` (sua rede on-premises) -> `Dynamic Routing Gateway`

- **Como funciona:**
  - Se o tráfego for para `192.168.10.5` (on-premises), ele corresponde a ambas as regras. Mas `/16` é mais específico que `/0`, então a **Regra 2 é escolhida**, e o tráfego vai para o DRG.
  - Se o tráfego for para o Google (`8.8.8.8`), apenas a **Regra 1** corresponde. Portanto, ele vai para o NAT Gateway.

---

## Conectando VCNs umas às Outras (Peering)

- **Local Peering (Mesma Região):**
  - **Quando usar:** Para conectar duas VCNs que estão na **mesma região** do OCI.
  - **Componente:** Usa um **Local Peering Gateway (LPG)** em cada VCN para estabelecer a conexão.

- **Remote Peering (Regiões Diferentes):**
  - **Quando usar:** Para conectar duas VCNs em **regiões diferentes** do OCI.
  - **Componente:** Usa um **Dynamic Routing Gateway (DRG)** em cada VCN.

---

## Escalando a Conectividade: O DRG como Roteador Central 🚀

Conectar muitas VCNs com *peering* ponto a ponto (um a um) é complexo e não escala bem. A solução moderna para isso é usar o **DRG (v2)** como um **roteador central (hub)**, criando uma topologia conhecida como *hub-and-spoke*.

- **Como funciona:** Em vez de conectar as VCNs umas às outras, você conecta todas elas a um único DRG. O DRG então gerencia o roteamento de tráfego entre todas as VCNs conectadas a ele, de forma centralizada.

- **Escala:** Um único DRG pode conectar até **300 VCNs**, simplificando enormemente arquiteturas complexas.

---

## **Segurança na VCN (Security Lists vs. NSGs)**

O OCI oferece duas maneiras de implementar regras de firewall virtuais para controlar o tráfego na sua VCN.

## O Firewall da Subnet: Security Lists (SLs) 🛡️

Pense nas *Security Lists* como o firewall principal que protege o "bairro" inteiro (a subnet).

- **O que são?** São um conjunto de **regras de firewall** virtuais.

- **Como são aplicadas?** Uma *Security List* é associada a uma **Subnet** inteira.

- **Escopo:** As regras se aplicam a **TODAS as instâncias** (VNICs) que estão ou que venham a ser criadas dentro daquela subnet, sem exceção.

- **Regras Stateful (Padrão):** Por padrão, as regras são *Stateful*. Isso significa que se você permitir tráfego de **entrada** (ingress) em uma porta, a resposta de **saída** (egress) é automaticamente permitida. Você só precisa escrever a regra de entrada.

- **Fonte/Destino na Regra:** A origem ou o destino do tráfego é sempre definido por um **bloco CIDR** (ex: `0.0.0.0/0` para a internet ou `10.0.2.0/24` para outra subnet).

---

## O Firewall da Instância: Network Security Groups (NSGs) ➡️ 🖥️

Pense nos NSGs como um segurança particular para um grupo específico de "casas" (instâncias), mesmo que elas estejam no mesmo bairro.

- **O que são?** Também são um conjunto de regras de firewall, mas com uma abordagem mais granular e flexível.

- **Como são aplicadas?** Um NSG é associado diretamente a uma **VNIC** (a "placa de rede" virtual de uma instância). Uma instância pode pertencer a vários NSGs.

- **Escopo:** As regras se aplicam **apenas às VNICs** que você explicitamente adicionou ao grupo.

- **Principais Vantagens sobre as SLs:**
  1. **Granularidade:** Você pode ter duas instâncias **na mesma subnet** com regras de firewall completamente diferentes. Isso é impossível de fazer apenas com *Security Lists*.
  1. **Fonte/Destino flexível:** Nas regras de um NSG, a origem ou o destino do tráfego pode ser **outro NSG**. Isso é muito poderoso, pois a regra se adapta automaticamente se os IPs das instâncias no outro NSG mudarem.

---

## Tabela Comparativa: SL vs. NSG (Essencial para a Prova!) ⚔️

<!-- Bloco do tipo 'table' não suportado -->

---

### **OCI Load Balancer**

## Por que Usar um Load Balancer? 🤔

Um *Load Balancer* atua como um "controlador de tráfego" na entrada da sua aplicação. Ele recebe as requisições dos clientes e as distribui de forma inteligente entre vários servidores de backend.

- **Principais Benefícios:**
  - **Alta Disponibilidade (High Availability):** Se um dos seus servidores de backend falhar, o *Load Balancer* detecta a falha e para de enviar tráfego para ele, redirecionando para os servidores que continuam saudáveis. Sua aplicação continua no ar!
  - **Escalabilidade (Scalability):** Se o tráfego na sua aplicação aumentar muito, você pode simplesmente adicionar mais servidores ao backend, e o *Load Balancer* começa a distribuir a carga para eles também, sem que o usuário perceba.

---

## Os Tipos de Load Balancer no OCI

O OCI oferece dois tipos principais de Load Balancer, cada um operando em uma "camada" diferente do modelo de rede OSI e com propósitos distintos.

### 1. Load Balancer (Layer 7 - HTTP/S) 🧠

- **Camada:** Opera na **Camada 7** (Aplicação).

- **O que ele entende?** Protocolos **HTTP** e **HTTPS**. Ele consegue "ler" o conteúdo das requisições (como URLs, headers e cookies).

- **Visibilidade:** Pode ser **Público** (com um endereço IP acessível pela internet) ou **Privado** (para balancear tráfego interno entre as camadas da sua aplicação, ex: da camada web para a de aplicação).

- **Principal Vantagem: Inteligência.** Por entender HTTP, ele pode tomar decisões de roteamento avançadas com base no conteúdo da requisição. Também oferece recursos como terminação SSL.

- **Shapes (Tamanhos):** Oferece *shapes* **Flexíveis** (você define uma faixa de banda mínima e máxima) ou **Dinâmicos** (tamanhos pré-definidos como pequeno, médio, grande).

### 2. Network Load Balancer (Layer 4 - TCP/UDP) ⚡

- **Camada:** Opera nas **Camadas 3 e 4** (Rede/Transporte).

- **O que ele entende?** Protocolos de transporte como **TCP**, **UDP** e também **ICMP**. Ele não inspeciona o conteúdo HTTP dos pacotes.

- **Visibilidade:** Também pode ser **Público** ou **Privado**.

- **Principal Vantagem: Performance Extrema e Baixa Latência.** Como ele não precisa inspecionar os pacotes a fundo, ele é muito mais rápido e eficiente na entrega do tráfego.

---

## Qual Escolher? A Tabela de Decisão ⚔️

<!-- Bloco do tipo 'table' não suportado -->

---

### **Demo: Configurando um Load Balancer do Zero**

Esta demo mostra o processo completo para configurar um Load Balancer público que distribui tráfego para servidores web em uma subnet privada.

## 1. Preparação do Terreno (Rede e Segurança) 🏗️

Antes de tudo, precisamos criar o ambiente de rede.

1. **Criar a VCN:** Usando o **VCN Wizard**, crie uma nova VCN com o modelo **"VCN with Internet Connectivity"**. Isso irá gerar automaticamente uma **Subnet Pública** e uma **Subnet Privada**.

1. **Liberar o Firewall (Passo Essencial):** Por padrão, a VCN bloqueia o tráfego web. Precisamos liberá-lo:
  - Vá para a **Security List** associada à **Subnet Pública**.
  - Adicione uma nova **Ingress Rule (Regra de Entrada)**.
  - Configure a regra para permitir tráfego da internet (Source CIDR: `0.0.0.0/0`) na porta de destino `80` (HTTP).

---

## 2. Construindo os Servidores (Backends) 🖥️

Agora, criamos os servidores web que receberão o tráfego do Load Balancer.

1. **Criar duas Instâncias de Compute** (ex: `web-server-1` e `web-server-2`).

1. **Localização Estratégica:** Durante a criação, certifique-se de colocar ambas as instâncias na **Subnet Privada**. Isso garante que elas não terão um IP público e estarão protegidas.

1. **Automação com Startup Script:** Na seção de opções avançadas, use um **startup script** para cada instância. O script deve:
  - Instalar um servidor web (como o Apache `httpd`).
  - Criar uma página `index.html` personalizada (ex: "Olá, sou o Web Server 1") para que possamos identificar qual servidor está respondendo durante o teste.

---

## 3. Instalando o "Controlador de Tráfego" (Load Balancer) 🚦

Com a rede e os servidores prontos, é hora de criar o Load Balancer.

1. **Navegação:** Vá para `Networking` -> `Load Balancers` e clique em `Create Load Balancer`. Escolha o tipo **Load Balancer (Layer 7)**.

1. **Passo 1: Detalhes**
  - **Visibilidade:** Escolha **Public**.
  - **Rede:** Associe o Load Balancer à **Subnet Pública**.

1. **Passo 2: Configuração dos Backends**
  - **Política de Balanceamento:** Escolha o algoritmo. A demo usa **Weighted Round Robin**, que distribui o tráfego sequencialmente para cada servidor.
  - **Adicionar Backends:** Selecione as duas instâncias (`web-server-1` e `web-server-2`) que você criou.
  - **Health Check:** Mantenha a verificação de saúde (health check) padrão, que irá testar se os servidores estão respondendo na porta `80`.

1. **Passo 3: Configuração do Listener**
  - O *Listener* é a "porta de entrada" do Load Balancer, que "escuta" o tráfego vindo da internet.
  - **Protocolo e Porta:** Configure o listener para "escutar" tráfego **HTTP** na porta **80**.

---

## 4. O Teste Final e a Verificação ✅

1. **Aguardar Saúde (Health):** Após criar o Load Balancer, aguarde o status do **Backend Set Health** mudar de `Pending` para **OK** (verde). Isso confirma que ele conseguiu se comunicar com os servidores e que eles estão saudáveis.

1. **Copiar o IP Público:** Copie o endereço IP público que foi atribuído ao Load Balancer.

1. **Testar no Navegador:** Cole o IP no seu navegador.

1. **Verificar o Round Robin:** Ao atualizar a página (`F5`) repetidamente, você verá a mensagem alternando entre "Olá, sou o Web Server 1" e "Olá, sou o Web Server 2", provando que o balanceamento de carga está funcionando perfeitamente.

---

# Introdução ao OCI Compute

O OCI Compute fornece servidores virtuais e físicos para rodar suas aplicações, destacando-se por sua escalabilidade, alta performance e baixo custo.

## Os Tipos de "Servidores" no OCI Compute 🖥️

O OCI oferece diferentes tipos de instâncias para atender a qualquer necessidade, desde pequenos testes até cargas de trabalho de altíssima performance.

### Bare Metal (Metal "Nu")

- **O que é?** Um **servidor físico inteiro** dedicado exclusivamente a você. Sem a camada de virtualização (hypervisor) da Oracle, garantindo zero sobrecarga e sem "vizinhos barulhentos".

- **Ideal para:** Máxima performance, workloads que precisam de acesso direto ao hardware ou que possuem licenças restritivas (BYOL - Bring Your Own License).

### Virtual Machines (VMs)

- **O que é?** A máquina virtual tradicional, a opção mais comum. Vários clientes (tenants) compartilham o mesmo hardware físico, mas são mantidos em total isolamento de segurança uns dos outros.

- **Ideal para:** A grande maioria das aplicações, oferecendo um ótimo balanço entre custo, flexibilidade e performance.

### Dedicated Virtual Machine Host (Host Dedicado)

- **O que é?** O melhor dos dois mundos. Você recebe um **servidor Bare Metal dedicado**, mas com a capacidade de rodar **suas próprias VMs** nele.

- **Ideal para:** Situações onde você precisa da flexibilidade das VMs, mas com a garantia de que nenhum outro cliente está no mesmo hardware físico, seja por compliance, segurança ou licenciamento.

## Os Diferenciais do OCI Compute ⭐

### Shapes Flexíveis: Servidores Sob Medida

Em vez de se prender a tamanhos fixos (Pequeno, Médio, Grande), o OCI permite que você **escolha a quantidade exata de OCPUs e Memória RAM** para sua VM.

- **Benefício:** Isso evita o desperdício de recursos (overprovisioning) e otimiza os custos, permitindo que você pague apenas pelo que realmente precisa.

### Poder de Escolha: Processadores Intel, AMD e ARM

O OCI oferece instâncias com diferentes arquiteturas de processadores para se adequar melhor à sua carga de trabalho.

- **Destaque para o ARM (Ampere A1):** Para workloads de alta vazão como servidores web, APIs e microserviços, as instâncias ARM oferecem uma **relação performance/preço (price-performance) significativamente melhor** que as alternativas.

### Otimização de Custos: Preemptible VMs (Instâncias Interrompíveis)

- **O que são?** São VMs de **curta duração e baixíssimo custo** que podem ser terminadas (interrompidas) pelo OCI a qualquer momento com um aviso prévio curto, caso a capacidade seja necessária para outros clientes.

- **Benefício:** Custam **50% menos** que as VMs normais sob demanda.

- **Ideal para:** Cargas de trabalho que toleram interrupções, como processamento em lote (*batch jobs*), renderização de vídeos, testes em larga escala ou aplicações projetadas para serem tolerantes a falhas.

---

## O Básico sobre Instâncias

---

## O Que é uma Instância e do que ela precisa para viver? 🌱

Uma **instância** é o termo que usamos para um **servidor (host)** no OCI, seja ele uma Máquina Virtual (VM) ou um servidor Bare Metal. Para que uma instância possa ser criada e funcionar, ela depende de outros dois serviços essenciais: **Rede (Networking)** e **Armazenamento (Storage)**.

---

## Dependência #1: Rede (VCN, Subnet e VNIC) 🌐

Antes de sequer pensar em criar uma instância, você **precisa ter** uma **Virtual Cloud Network (VCN)** e uma **Subnet** já configuradas.

- **Como a conexão funciona?**
  1. O servidor físico no data center da Oracle tem uma placa de rede (NIC).
  1. O OCI cria uma versão virtual dessa placa, chamada **VNIC (Virtual Network Interface Card)**, para sua instância.
  1. Essa **VNIC é "colocada" virtualmente dentro da Subnet** que você escolheu durante a criação da instância.
  1. A instância recebe seu **endereço IP Privado** do intervalo de IPs definido naquela Subnet.

---

## Dependência #2: Armazenamento Remoto (Block Volume) 💾

Os discos de uma instância do OCI **não são locais** (não estão fisicamente dentro do servidor que a hospeda). Eles são volumes de armazenamento que vivem na rede e são fornecidos pelo serviço de **Block Volume**.

- **Boot Volume (Disco de Boot):**
  - É o disco que contém a **Imagem** do sistema operacional (Linux, Windows) e outros softwares básicos.
  - Quando a instância é ligada, ela "dá o boot" a partir deste volume de rede, que funciona como o "C:" do seu servidor.

- **Block Volume (Disco de Dados):**
  - São discos de dados adicionais que você pode anexar à sua instância para armazenar arquivos, bancos de dados, etc.
  - Pense neles como "HDs externos" de altíssima performance conectados pela rede.

---

## Um Recurso Chave para Alta Disponibilidade: Live Migration ✈️

- **O problema:** O hardware físico onde sua VM está rodando pode precisar de manutenção ou, em casos raros, falhar.

- **A solução do OCI:** O OCI pode **migrar sua VM em execução** de um host físico para outro **sem a necessidade de reiniciá-la (reboot)**.

- **Benefício:** O processo é transparente para você e sua aplicação, garantindo que ela continue no ar mesmo durante eventos de manutenção planejada na infraestrutura da Oracle.

---

## Demo: Usando o Cloud Shell para Gerar Chaves SSH

### Revisão Rápida: O Que é Cloud Shell e Para Que Servem as Chaves SSH? 🤔

- **Cloud Shell (>_)**
É um **terminal Linux completo e gratuito** que roda diretamente no seu navegador, dentro da console do OCI.
  - **Principal Vantagem:** Já vem com a **OCI CLI pré-autenticada** e outras ferramentas úteis (Git, Python, etc.), eliminando a necessidade de instalar e configurar tudo na sua máquina local.

- **Chaves SSH 🔑**
SSH (Secure Shell) é o protocolo padrão para **acessar servidores Linux remotamente de forma segura**. As chaves de acesso sempre vêm em um **par**:
  - **Chave Pública (**`**.pub**`**):** Você a instala no servidor que quer acessar. É como instalar a **fechadura** na porta.
  - **Chave Privada:** Fica guardada em segredo com você (no Cloud Shell, neste caso). É a sua **chave** pessoal que abre a fechadura.

---

## Passo a Passo: Gerando seu Par de Chaves no Cloud Shell 🧑‍💻

1. **Abra o Cloud Shell:** Clique no ícone `**>_**` no menu superior da console do OCI.

1. **(Opcional, mas recomendado) Organize seus arquivos:**
  - Crie um diretório para guardar as chaves: `mkdir ssh-keys`
  - Entre no diretório recém-criado: `cd ssh-keys`

1. **Execute o Comando de Geração:**
  - Digite o comando: `ssh-keygen -t rsa -b 2048 -f MinhaChave`
  - **O que significa cada parte?**
    - `ssh-keygen`: A ferramenta para gerar chaves.
    - `t rsa`: Define o tipo de algoritmo (RSA é o mais comum).
    - `b 2048`: Define o tamanho da chave em bits (2048 é um padrão seguro).
    - `f MinhaChave`: Define o nome do arquivo para as suas chaves.

1. **Passphrase (Frase Secreta):** O terminal pedirá uma *passphrase*. Esta é uma senha opcional para proteger sua chave privada com uma camada extra de segurança. Para a demo (e muitos casos de uso), você pode deixar em branco pressionando **Enter** duas vezes.

1. **Verifique o Resultado:** Use o comando `ls` para listar os arquivos no diretório. Você verá dois novos arquivos:
  - `MinhaChave` (a chave privada 🤫)
  - `MinhaChave.pub` (a chave pública 🌍)

## A Lição Mais Importante da Demo 💡

O Cloud Shell é a maneira mais **conveniente e integrada** de gerar as chaves SSH que você precisará para se conectar às suas instâncias de compute. Você não precisa de nenhuma ferramenta externa como o PuTTYgen ou de configurar nada no seu computador pessoal.

---

### **Demo: Criando uma Instância de Compute (Método Manual)**

## Fase 1: Construindo a Rede Manualmente 🏗️

Diferente do VCN Wizard, aqui criamos cada componente da rede passo a passo para entender a lógica por trás da conectividade.

1. **Criar a VCN:**
  - Vá para `Networking` -> `Virtual Cloud Networks` e clique em **Create VCN**.
  - Defina um nome e o bloco CIDR principal (ex: `10.0.0.0/16`).

1. **Criar a Subnet:**
  - Dentro da VCN recém-criada, clique em **Create Subnet**.
  - Dê um nome, escolha o tipo **Regional** e defina o CIDR da subnet (ex: `10.0.0.0/24`).
  - Marque a opção **Public Subnet**.
  - Associe a subnet à **Default Route Table** e à **Default Security List**.

1. **Criar o Internet Gateway (IGW):**
  - No menu de `Networking`, vá para **Internet Gateways** e crie um novo.
  - Dê um nome e associe-o à sua VCN.

1. **Configurar a Rota (o "GPS" da rede):**
  - Volte para a sua VCN e vá para a **Default Route Table**.
  - Adicione uma **Route Rule** com as seguintes configurações:
    - **Target Type:** `Internet Gateway`.
    - **Destination CIDR Block:** `0.0.0.0/0` (esta é a "rota padrão", significando "qualquer tráfego destinado à internet").
    - **Target:** Selecione o IGW que você acabou de criar.

1. **Configurar o Firewall (o "Porteiro"):**
  - Volte para a sua VCN e vá para a **Default Security List**.
  - Adicione uma **Ingress Rule** (Regra de Entrada):
    - **Source CIDR:** `0.0.0.0/0` (de qualquer lugar da internet).
    - **Destination Port:** `80` (para permitir tráfego web HTTP).

---

## Fase 2: Lançando a Instância de Compute 🚀

Com a rede pronta, agora podemos criar o servidor.

- **Navegação:** `Compute` -> `Instances` -> **Create Instance**.

- **Imagem e Shape:** Escolha o Sistema Operacional (**Image**) e o hardware (**Shape**). A demo destaca o uso de um **Shape Flexível**, que permite customizar a quantidade de OCPUs e Memória RAM.

- **Rede:** Na seção de networking, selecione a **VCN** e a **Subnet Pública** que você acabou de criar. Garanta que a opção de **atribuir um IP público** esteja marcada.

- **Chave SSH:** Use o **Cloud Shell** para visualizar (`cat`) o conteúdo da sua **chave pública** (`.pub`) e cole a string completa na configuração da instância. Isso permitirá o acesso seguro.

---

## Fase 3: Acessando e Configurando o Servidor 👨‍💻

1. **Obtenha o IP Público:** Após a instância ser criada e estar no estado "Running", copie seu IP Público na página de detalhes.

1. **Conecte-se via SSH (pelo Cloud Shell):**
  - Use o comando `ssh -i <arquivo_da_chave_privada> opc@<IP_Público_da_instância>`

1. **Instale o Servidor Web:** Uma vez conectado, execute os comandos para instalar o Apache, iniciar o serviço, abrir o firewall do próprio sistema operacional e criar uma página `index.html` de teste.

---

## Fase 4: O Teste Final ✅

Abra um navegador e acesse o **IP Público** da sua instância. A página de teste do Apache que você configurou deve ser exibida, confirmando que tudo, da rede ao servidor, está funcionando corretamente.

## Resumo: Manual vs. Wizard ⚔️

O método **manual** dá controle total e é ótimo para aprender, mas exige que você configure cada componente separadamente (Subnet, IGW, Route Table, Security List). O **Wizard** automatiza todos esses passos, sendo mais rápido e menos propenso a erros para cenários padrão.

---

## Escalabilidade no OCI Compute

Escalabilidade é a capacidade do seu sistema de crescer (ou encolher) para atender à demanda. No OCI, existem duas formas principais de fazer isso.

## Os Dois Tipos de Escalabilidade ⚖️

### Escalabilidade Vertical (Scaling Up/Down) 💪

- **O que é?** Aumentar ou diminuir os recursos de **uma única instância** existente. É como trocar o motor de um carro por um mais potente.

- **O que você muda?** O número de OCPUs e a quantidade de Memória RAM (alterando o *shape* da instância).

- **Ponto Crítico:** Exige **downtime (parada)**. A instância precisa ser reiniciada para que a mudança de *shape* seja aplicada, pois ela pode ser movida para outro hardware físico.

- **Melhor prática:** Pare a instância (`Stop`) antes de alterar seu *shape*.

### Escalabilidade Horizontal / Autoscaling (Scaling Out/In) ↔️

- **O que é?** Adicionar ou remover **mais instâncias** idênticas a um grupo. É como adicionar mais carros a uma frota para lidar com mais passageiros.

- **O que você muda?** O **número** de instâncias, não o tamanho individual de cada uma.

- **Principais Benefícios:**
  - **Alta Disponibilidade:** Se uma instância falhar, as outras no grupo continuam operando e atendendo ao tráfego.
  - **Elasticidade:** Ajusta-se automaticamente à demanda. Mais tráfego, mais servidores são adicionados. Menos tráfego, servidores são removidos, **economizando custos**.
  - **Custo:** O recurso de Autoscaling em si é **gratuito**. Você paga apenas pelas instâncias que estão em execução.

---

## Como Configurar o Autoscaling (Processo de 3 Passos) ⚙️

Configurar o *Autoscaling* é um processo lógico que envolve a criação de três componentes em sequência:

### 1️⃣ Passo: Criar uma **Instance Configuration**

- **O que é?** Um **"template"** ou um "carimbo" da sua instância modelo.

- **O que contém?** Todas as especificações necessárias para criar uma instância: a imagem do SO, o *shape* (tamanho), a configuração de rede (VCN/Subnet), armazenamento, metadados, etc.

- **Como criar?** Geralmente, você cria este template a partir de uma instância já configurada que servirá de modelo para todas as outras.

### 2️⃣ Passo: Criar um **Instance Pool**

- **O que é?** Um **grupo de instâncias** que serão gerenciadas como uma unidade única. Todas as instâncias do *pool* são criadas a partir da mesma *Instance Configuration* do passo anterior.

- **Função:** Permite iniciar, parar ou terminar todas as instâncias do grupo de uma vez. Também é responsável por distribuir as instâncias entre diferentes Domínios de Disponibilidade (ADs) e Domínios de Falha (FDs) para garantir alta disponibilidade.

### 3️⃣ Passo: Criar a **Configuração de Autoscaling**

- **O que é?** O conjunto de **regras** que vai controlar o *Instance Pool* de forma automática.

- **O que você define?**
  - **Tamanhos:** Número **inicial**, **mínimo** e **máximo** de instâncias no *pool*.
  - **Política de Scaling:** Uma regra baseada em uma métrica de performance (CPU ou Memória).

- **Exemplo de Política:** "Se a média de uso de **CPU** do *pool* ultrapassar **70%**, adicione mais **2 instâncias** (*scale-out*). Se o uso de CPU cair abaixo de **25%**, remova **2 instâncias** (*scale-in*)."

---

## Oracle Container Engine for Kubernetes (OKE)

### O Básico: VMs vs. Contêineres 🥊

Para entender o OKE, primeiro precisamos diferenciar contêineres de máquinas virtuais.

<!-- Bloco do tipo 'table' não suportado -->

A principal vantagem dos contêineres é a **portabilidade**, o que os torna ideais para aplicações nativas da nuvem e microserviços.

---

## O Desafio da Escala e a Solução: Kubernetes (K8s) 🤖

Contêineres são ótimos, mas gerenciar centenas ou milhares deles (implantar, conectar em rede, escalar, consertar falhas) é um grande desafio. O processo de automatizar tudo isso é chamado de **Orquestração de Contêineres**.

- **Kubernetes:** É o sistema de código aberto que se tornou o **padrão mundial** para orquestração. Ele automatiza todo o ciclo de vida das aplicações em contêineres, oferecendo auto-reparação (*self-healing*), escalabilidade automática e implantações sem downtime.

---

## OKE: O Kubernetes Gerenciado pela Oracle ⚙️

**Oracle Container Engine for Kubernetes (OKE)** é o serviço da Oracle que oferece um **Kubernetes totalmente gerenciado, escalável e de alta disponibilidade**.

- **Modelo de Responsabilidade Compartilhada:**
  - **Control Plane (O Cérebro):** Gerencia o estado do cluster, agenda os contêineres, etc. **É 100% gerenciado pela Oracle e não tem custo para você.**
  - **Worker Nodes (Os Músculos):** São as instâncias de compute (VMs ou Bare Metal) onde seus contêineres (dentro de *Pods*) efetivamente rodam. **Você gerencia e paga por esses nós.**

---

## As Opções do OKE (Essencial para a Prova!) ⭐

Ao criar um cluster OKE, você precisa fazer duas escolhas importantes:

### 1. Tipos de Cluster: Enhanced vs. Basic

- **Enhanced Cluster (Avançado):** A opção completa, recomendada para produção. Suporta **TODOS** os recursos do OKE e vem com um **SLA** (acordo de nível de serviço com garantia financeira).

- **Basic Cluster (Básico):** Uma opção mais limitada, ideal para aprendizado e testes. Suporta apenas funcionalidades essenciais e vem com um **SLO** (objetivo de nível de serviço, sem garantia financeira).

### 2. Tipos de Nós (Worker Nodes): Managed vs. Virtual

<!-- Bloco do tipo 'table' não suportado -->

---

