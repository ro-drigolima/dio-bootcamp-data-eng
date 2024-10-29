import re
from datetime import datetime

# Funções de Validação
def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  # Remove qualquer caractere que não seja número
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido. Certifique-se de usar 11 dígitos numéricos.")
        return None
    return cpf

def validar_data(data):
    try:
        return datetime.strptime(data, '%d/%m/%Y').date()
    except ValueError:
        print("Data inválida. Use o formato dd/mm/yyyy.")
        return None

# Funções de Operações Bancárias
def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato, numero_saques

    valor = float(input("Informe o valor do saque: "))
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def visualizar_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Funções de Criação de Usuários e Contas
def criar_usuario(usuarios):
    cpf = validar_cpf(input("Digite o CPF: "))
    if cpf is None or any(u["CPF"] == cpf for u in usuarios):
        print("CPF inválido ou já cadastrado.")
        return None
    nome = input("Nome completo: ")
    data_nascimento = validar_data(input("Data de nascimento (dd/mm/yyyy): "))
    if data_nascimento is None:
        return None

    endereco = {
        "logradouro": input("Logradouro: "),
        "nro": input("Número: "),
        "bairro": input("Bairro: "),
        "cidade": input("Cidade: "),
        "sigla_estado": input("Sigla Estado: ").upper()
    }
    novo_usuario = {"nome": nome, "CPF": cpf, "data_nascimento": data_nascimento, "endereco": endereco}
    return novo_usuario

def criar_conta_corrente(contas, usuarios):
    cpf = validar_cpf(input("Digite o CPF do titular para a nova conta: "))
    if cpf is None or not any(u["CPF"] == cpf for u in usuarios):
        print("Cliente não cadastrado. Faça o cadastro antes.")
        return None
    numero_conta = len(contas) + 1
    usuario = next(u for u in usuarios if u["CPF"] == cpf)
    conta = {"numero_conta": numero_conta, "agencia": "0001", "cliente_dono_da_conta": usuario}
    contas.append(conta)
    print(f"Conta criada com sucesso para {usuario['nome']}!")
    return conta

# Função Principal
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Criar usuário
    [f] Criar conta corrente
    [q] Sair
    => """

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)
        elif opcao == "s":
            if numero_saques < LIMITE_SAQUES:
                saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite,
                                                      numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
            else:
                print("Operação falhou! Número máximo de saques excedido.")
        elif opcao == "e":
            visualizar_extrato(saldo, extrato=extrato)
        elif opcao == "c":
            usuario = criar_usuario(usuarios)
            if usuario:
                usuarios.append(usuario)
        elif opcao == "f":
            criar_conta_corrente(contas, usuarios)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente.")

if __name__ == "__main__":
    main()
