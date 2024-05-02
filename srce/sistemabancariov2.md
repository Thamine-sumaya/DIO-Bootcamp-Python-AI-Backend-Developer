# Desafio:

Modularização do código do sistema bancário v1 por meio de funções para as operações existentes: sacar, depositar e visualizar histórico.
Além da criação de duas novas funções: criar usuário(cliente do banco) e criar conta corrente(vincular com usuário)

## Separação em funções

Para exercício do conteúdo aprendido no módulo, cada função vai ter uma regra na passagem de argumentos.

### Saque

- Deve receber argumentos apenas por nome (keyword only);
  Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques;
  Sujestão de retorno: saldo e extrato.

### Depósito

- Deve receber os argumentos apenas por posição (positional only);
  Sugestão de argumentos: saldo, valor, extrato;
  Sujestão de retorno: saldo e extrato.

### Extrato

- Deve receber os argumentos por posição e nome (positional only e keyword only);
  Argumentos posicionais:saldo;
  Argumentos nomeaos: extrato.

## Novas Funções

### Criar usuário

- O programa deve armazenar os usuários em uma lista;
- Composto por: nome, data de nascimento, cpf e endereço;
- Endereço é uma string com formato: logradouro, número, bairro, cidade, estado;
- O CPF deve conter apenas números;
- Deve ser possível cadastrar apenas um usuário por CPF.

### Criar conta corrente

- O programa deve armazenas as contas em uma lista;
- Composta por: agência, número da conta e usuário;
- O número da conta é sequencial iniciando em 1;
- O numero da agência é fixo "0001";
- O usuário pode ter mais de uma conta mas uma conta não pode ser de mais de um usuário.

### Dica:

Para vncular um usuário a uma conta, filtre a lista de usuários usando o cpf informado.
