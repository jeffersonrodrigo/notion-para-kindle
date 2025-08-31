[https://mylearn.oracle.com/ou/ekit/148111/35644/90da110a-5f86-4d90-af98-37230bb9a5b3/course](https://mylearn.oracle.com/ou/ekit/148111/35644/90da110a-5f86-4d90-af98-37230bb9a5b3/course)

### **Arquitetura Física do OCI (Core Constructs)**

### **1. Conceitos Fundamentais (A Hierarquia)**

A arquitetura física do OCI é construída em três níveis, um dentro do outro. É crucial entender a função de cada um.

- **Região (Region):**

- **Availability Domain (AD):**

- **Fault Domain (FD):**

### **2. Como Escolher uma Região? (3 Critérios Essenciais)**

Você precisa escolher a região certa para sua aplicação com base em:

1. **Latência:** Escolha a região mais próxima dos seus usuários para obter o melhor desempenho e a menor latência.

1. **Soberania de Dados (Data Residency) e Compliance:** Leis locais podem exigir que os dados dos seus clientes permaneçam em um país específico.

1. **Disponibilidade de Serviços (Service Availability):** Nem todos os serviços do OCI estão disponíveis em todas as regiões, especialmente os mais novos.

### **3. Como Usar esses Conceitos para Alta Disponibilidade (High Availability - HA)**

O objetivo é **evitar Pontos Únicos de Falha** (*Single Points of Failure*).

- **Estratégia 1 (Dentro de 1 AD):**

- **Estratégia 2 (Entre ADs - Máxima Proteção):**

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

### **2. Navegação Principal (Menu "Hambúrguer" ☰)**

- **Localização:** Ícone com três linhas no canto superior esquerdo.

- **Função:** É a principal forma de encontrar **todos os serviços** do OCI.

- **Organização:** Os serviços são agrupados em categorias lógicas para facilitar a localização:

### **3. Barra de Ferramentas Global (Topo da Página)**

Esta barra contém ferramentas essenciais que funcionam de forma global, independentemente do serviço que você está visualizando.

- **Busca (Search):**

- **Regiões (Regions):**

- **Anúncios (Announcements - Ícone de Megafone):**

- **Ajuda (Help - Ícone de "?")**

- **Ferramentas de Desenvolvedor (Developer Tools)**

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

- **Autorização (Authorization - AuthZ):**

> Analogia Simples: Autenticação é mostrar seu crachá para entrar no prédio. Autorização é o que está escrito no seu crachá que diz quais portas você pode abrir lá dentro.

---

### Como o IAM Funciona na Prática: Os Componentes

O IAM utiliza alguns componentes chave para organizar o acesso:

- **Identity Domain:** Pense nisso como um **"contêiner" para seus usuários e grupos**. É a estrutura que representa uma população de usuários e suas configurações de segurança associadas (como políticas de senha e MFA).

- **Usuários e Grupos (Users & Groups):**

- **Compartimentos (Compartments):** São como **"pastas" lógicas** para organizar e isolar seus recursos na nuvem (VMs, bancos de dados, redes). O acesso aos recursos é controlado no nível do compartimento.

- **Políticas (Policies):** São as **regras que unem tudo**. Uma política determina qual `**Grupo**` tem qual tipo de `**Permissão**` em qual `**Compartimento**`.

### OCID (Oracle Cloud ID): A "Placa de Identidade" dos Recursos 🆔

- **O que é?** Um identificador **único e universal** que a Oracle atribui automaticamente a **TODO** e qualquer recurso criado na nuvem (instâncias, redes, volumes, e até mesmo sua conta, que é a *tenancy*).

- **Quando você o usa?** Você raramente o usa diretamente na console web, mas ele é **essencial** ao interagir com a nuvem via **CLI (Command Line Interface)** ou **SDKs (Software Development Kits)**.

- **Sintaxe do OCID:**`ocid1.<tipo_do_recurso>.<realm>.[região].<id_único>`

---

## **Compartimentos (Compartments) no OCI**

Compartimentos são a principal forma de **organizar e isolar** seus recursos na nuvem do OCI.

### O Que São Compartimentos? 📁

Pense neles como **pastas lógicas** dentro da sua conta (Tenancy). Quando você cria uma conta, ela já vem com um compartimento principal chamado **Compartimento Raiz (Root Compartment)**.

Embora você *possa* colocar todos os seus recursos no compartimento *Root*, a **melhor prática é criar seus próprios compartimentos** para separar e organizar os recursos (ex: um compartimento para a equipe de rede, outro para a de desenvolvimento, etc.).

---

### Por Que Usar Compartimentos? (Os 2 Motivos Principais)

1. **Controle de Acesso:** É a razão fundamental. Você usa **Políticas (Policies)** para dar a um **Grupo** de usuários permissões para gerenciar recursos dentro de um **Compartimento** específico.

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

- **Orçamentos (Budgets):** Permitem monitorar os gastos e definir alertas.

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

1. **Confirmação:** Clique em **Create Compartment**.

> Dica da Demo: Para visualizar todos os recursos que existem dentro de um compartimento, você pode usar a ferramenta Tenancy Explorer.

---

### Passo a Passo: Criando um Identity Domain 🔑

O objetivo é criar um domínio chamado `sandbox domain` para isolar um conjunto de usuários.

1. **Navegação:** Vá para o menu principal ☰ **Identity & Security** e clique em **Domains**.

1. **Ação:** Clique no botão **Create domain**.

1. **Preenchimento:**

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

1. **Criar o Grupo e Adicionar o Usuário:**

## 2. Autenticação (AuthN): O Login do Novo Usuário 🔑

Agora, o usuário `OCI Admin` precisa acessar o sistema pela primeira vez.

1. **Ativação:** O usuário recebe um e-mail para **ativar a conta**.

1. **Definir Senha:** Ao clicar no link, o usuário é direcionado para criar sua senha. A tela de login já mostra que ele pertence ao `sandbox-domain`.

1. **Processo de Login:**

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

1. **Resultado:** O construtor gera a política:
`Allow group sandbox-domain/OCI-Admin-group to manage object-family in compartment sandbox`

1. A política é criada e ativada.

## 5. A Prova Final: Testando as Permissões ✅

De volta à sessão do usuário `ociadmin`:

- **Teste Negativo:** Tentar acessar recursos de *Compute* continua falhando, pois a política não deu essa permissão.

- **Teste Positivo:**

---

### **Configurando sua Tenancy (Melhores Práticas)**

Configurar sua tenancy (sua conta OCI) corretamente desde o início é crucial para a segurança e a governança. A Oracle recomenda três práticas fundamentais.

## As 3 Melhores Práticas de Segurança para sua Conta OCI 🛡️

1. **Não use o Administrador da Tenancy para o dia a dia.**

1. **Crie Compartimentos Dedicados.**

1. **Exija a Autenticação Multifator (MFA).**

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

- **Ponto Importante:** O tráfego **entre subnets dentro da mesma VCN** é roteado automaticamente pelo que chamamos de "roteamento local". Você **não precisa** criar uma regra para isso.

---

## A Regra de Ouro: A Rota Mais Específica Vence 🏆

Quando um pacote de dados precisa sair e seu destino corresponde a mais de uma regra na tabela, o OCI sempre usa a regra **mais específica**. Isso é conhecido como **"longest prefix match"** (correspondência de prefixo mais longo).

- **Exemplo da Aula:** Uma subnet privada tem duas regras de rota:

- **Como funciona:**

---

## Conectando VCNs umas às Outras (Peering)

- **Local Peering (Mesma Região):**

- **Remote Peering (Regiões Diferentes):**

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

---

## Tabela Comparativa: SL vs. NSG (Essencial para a Prova!) ⚔️

<!-- Bloco do tipo 'table' não suportado -->

---

### **OCI Load Balancer**

## Por que Usar um Load Balancer? 🤔

Um *Load Balancer* atua como um "controlador de tráfego" na entrada da sua aplicação. Ele recebe as requisições dos clientes e as distribui de forma inteligente entre vários servidores de backend.

- **Principais Benefícios:**

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

---

## 2. Construindo os Servidores (Backends) 🖥️

Agora, criamos os servidores web que receberão o tráfego do Load Balancer.

1. **Criar duas Instâncias de Compute** (ex: `web-server-1` e `web-server-2`).

1. **Localização Estratégica:** Durante a criação, certifique-se de colocar ambas as instâncias na **Subnet Privada**. Isso garante que elas não terão um IP público e estarão protegidas.

1. **Automação com Startup Script:** Na seção de opções avançadas, use um **startup script** para cada instância. O script deve:

---

## 3. Instalando o "Controlador de Tráfego" (Load Balancer) 🚦

Com a rede e os servidores prontos, é hora de criar o Load Balancer.

1. **Navegação:** Vá para `Networking` -> `Load Balancers` e clique em `Create Load Balancer`. Escolha o tipo **Load Balancer (Layer 7)**.

1. **Passo 1: Detalhes**

1. **Passo 2: Configuração dos Backends**

1. **Passo 3: Configuração do Listener**

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

---

## Dependência #2: Armazenamento Remoto (Block Volume) 💾

Os discos de uma instância do OCI **não são locais** (não estão fisicamente dentro do servidor que a hospeda). Eles são volumes de armazenamento que vivem na rede e são fornecidos pelo serviço de **Block Volume**.

- **Boot Volume (Disco de Boot):**

- **Block Volume (Disco de Dados):**

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

- **Chaves SSH 🔑**
SSH (Secure Shell) é o protocolo padrão para **acessar servidores Linux remotamente de forma segura**. As chaves de acesso sempre vêm em um **par**:

---

## Passo a Passo: Gerando seu Par de Chaves no Cloud Shell 🧑‍💻

1. **Abra o Cloud Shell:** Clique no ícone `**>_**` no menu superior da console do OCI.

1. **(Opcional, mas recomendado) Organize seus arquivos:**

1. **Execute o Comando de Geração:**

1. **Passphrase (Frase Secreta):** O terminal pedirá uma *passphrase*. Esta é uma senha opcional para proteger sua chave privada com uma camada extra de segurança. Para a demo (e muitos casos de uso), você pode deixar em branco pressionando **Enter** duas vezes.

1. **Verifique o Resultado:** Use o comando `ls` para listar os arquivos no diretório. Você verá dois novos arquivos:

## A Lição Mais Importante da Demo 💡

O Cloud Shell é a maneira mais **conveniente e integrada** de gerar as chaves SSH que você precisará para se conectar às suas instâncias de compute. Você não precisa de nenhuma ferramenta externa como o PuTTYgen ou de configurar nada no seu computador pessoal.

---

### **Demo: Criando uma Instância de Compute (Método Manual)**

## Fase 1: Construindo a Rede Manualmente 🏗️

Diferente do VCN Wizard, aqui criamos cada componente da rede passo a passo para entender a lógica por trás da conectividade.

1. **Criar a VCN:**

1. **Criar a Subnet:**

1. **Criar o Internet Gateway (IGW):**

1. **Configurar a Rota (o "GPS" da rede):**

1. **Configurar o Firewall (o "Porteiro"):**

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

---

## As Opções do OKE (Essencial para a Prova!) ⭐

Ao criar um cluster OKE, você precisa fazer duas escolhas importantes:

### 1. Tipos de Cluster: Enhanced vs. Basic

- **Enhanced Cluster (Avançado):** A opção completa, recomendada para produção. Suporta **TODOS** os recursos do OKE e vem com um **SLA** (acordo de nível de serviço com garantia financeira).

- **Basic Cluster (Básico):** Uma opção mais limitada, ideal para aprendizado e testes. Suporta apenas funcionalidades essenciais e vem com um **SLO** (objetivo de nível de serviço, sem garantia financeira).

### 2. Tipos de Nós (Worker Nodes): Managed vs. Virtual

<!-- Bloco do tipo 'table' não suportado -->

---