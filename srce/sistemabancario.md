## Contexto

Um grande Banco decide modernizar suas operações e para isso escolheu a linguagem Python.

## Especificações

O sistema deve conter apenas 3 operações: depósito, saque, extrato.

### Operação de depósito:

- Deve ser possível depositar valores positivos;
- O projeto trabalha apenas com um usuário;
- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de saque:

- Máximo de até 3 saques diários com limite de R$500,00 por saque;
- Em caso de saldo insuficiente o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo;
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de extrato:

- Deve listar todos os depósitos e saques realizados na conta;
- No final da listagem deve ser exibido o saldo final da conta;
- Os valores devem ser exibidos utilizando o formato: R$ xxx.xx.
