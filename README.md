## Automacom Lists Generator

#

### Overview
CLI (_Command Line Interface_) que, com base no comando e informações executados pelo usuário, percorre planilhas específicas do Excel (_.xslx_) e gera um arquivo de texto (_.txt_) com as informações solicitadas.

#

### Execução

O programa pode ser executado através do seu terminal de preferência. Basta ter o Python 3 instalado em seu ambiente e, nevegando até o diretório do programa, executar `python main.py` (Windows) ou `python3 main.py` (Linux).
&nbsp;

Pode ser criado também um executável com o **pyinstaller**. Basta instalá-lo (`pip install pyinstaller`) e executar `pyinstaller --onefile main.py` no diretório do programa. Você encontrará o executável na pasta **dist**. Com o executável, não é necessário que o usuário tenha o Python instalado em seu ambiente.
&nbsp;

Lembrando que as 3 planilhas do Excel são necessárias para o funcionamento do programa. Caso contrário, um erro será exibido e o programa não será executado. Estas planilhas devem estar em um diretíorio anterior à onde encontra o arquivo main.py (ou o executável). Exemplo: se o diretório do programa é `user/programs/automacomcli`, as planilhas devem estar em `user/programs`.

#

### Comandos

#### ac [_command_]

• ac é o comando que deve preceder os outros comandos específico. Use interrogação (_?_) para ver quais comandos disponível.

```
$~  ac ?

>> Possible arguments: emerg | servs | login | times | ic
```
&nbsp;

#### ac emerg [_code_] [_id_customer_]

• Gera informações de um cliente específico para um chamado emergencial (para o dia vigente).

**code**: c - para problemas relacionados a verificação de conexão | r - para serviço de retirada de equipamentos
&nbsp;
**id_customer**: id do cliente o qual o chamado é destinado

```
$~  ac emerg c 358

>>  Chamado gerado para Fulano da Silva
```
&nbsp;

#### ac servs

• Gera uma lista com as informações necessárias todos os chamados (exceto instalação) que estão marcado para o dia seguinte.

```
$~  ac servs

>>  14 Chamados Gerados!
```
&nbsp;

#### ac login

• Gera uma lista com o nome dos clientes de instalação e seus respectivos possíveis logins (para configuração de conexão no sistema) e emails (para cadastro do app mobile).

```
$~  ac login

>>  7 Logins Gerados!
```
&nbsp;

#### ac times

• Gera duas planilhas Excel, separados por região de zona, com os chamados já agendados, o qual é possível ver, em ordem de período (manhã, tarde ou horário comercial) quais lugares e quais tipos de chamado serão realizados.

```
$~  ac times

>>  Lista Horários dos Chamados Gerada!
```
&nbsp;

#### ac ic [_id_customer_]

• Exibe informações de um cliente específico. Não é gerado um arquivo de texto; as informações são exibidas no próprio terminal.

**id_customer**: id do cliente o qual se deseja exibir as informações

```
$~  ac ic 358

>>  Customer Infos:
    358 - Fulano
    Condomínio - Bloco 00 - Apto 00
    Celular
    Login - Banda
```
&nbsp;

#### hist

• Exibe o histórico das mensagens exibidas no terminal (mensagens essas que são os resultados dos comandos executados). Não é necessário o ac inicial.
```
$~  hist

    Chamado gerado para Fulano da Silva
    
    14 Chamados Gerados!
    
    7 Logins Gerados!

    Customer Infos:
    358 - Fulano
    Condomínio - Bloco 00 - Apto 00
    Celular
    Login - Banda
```
&nbsp;

#### clear

• Limpa as exibições e códigos digitados no termnal. Não é necessário o ac inicial.
```
$~  clear
```
&nbsp;

#### exit

• Fecha o terminal, finalizando o programa. Não é necessário o ac inicial.
```
$~  exit
```
