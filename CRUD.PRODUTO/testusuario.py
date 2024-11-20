import json
import os
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'usuario.json')
def carregar_usuario():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)  # Inicializa como lista vazia

    with open(arquivo, 'r') as f:
        return json.load(f)

def adicionar_usuario(nome,idade,cpf):
    usuarios = carregar_usuario()
    usuarios.append({'NOME':nome, 'IDADE':idade, 'CPF':cpf})

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    print("USUÁRIO ADICIONADO COM SUCESSO!")

def listar_usuario():
    usuarios = carregar_usuario()
    if usuarios:
        print("LISTA DE USUÁRIOS:")
        for usuario in usuarios:
            print(f"NOME: {usuario.get('NOME')}")
            print(f"IDADE: {usuario.get('IDADE')}")
            print(f"CPF: {usuario.get('CPF')}")
    else:
        print("LISTA VAZIA!")

def atualizar_usuario(nome_antigo, nome_novo, idade_novo, cpf_novo):
    usuarios = carregar_usuario()
    usuario_encontrado = False
    for usuario in usuarios:
        if usuario.get('NOME') == nome_antigo:
            usuario('NOME') == nome_novo
            usuario('IDADE') == idade_novo
            usuario('CPF') == cpf_novo
            usuario_encontrado = True
            break
    if usuario_encontrado:
        with open(arquivo, 'w') as f:
            json.dump(usuario, f, indent=4, ensure_ascii=False)
            print("✅ PRODUTO ATUALIZADO COM SUCESSO!")
    else:
            print("⚠️ PRODUTO NÃO ENCONTRADO PARA ATUALIZAÇÃO.")    

def excluir_usuario(usuario_nome):
    usuarios = carregar_usuario()
    for usuario in usuarios:
        if usuario.get('NOME') == usuario_nome:
            usuarios.remove(usuario)
    print(f"NOME '{usuario_nome}")

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    print("❌ PRODUTO EXCLUÍDO COM SUCESSO!")

def menu_inicial():
    print(" ----FLOWSTOCK---- ")
    print(" 1 - MÓDULO DO USUÁRIO ")
    print(" 2 - SAIR ")

def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIO")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. VOLTAR AO MENU ANTERIOR")     

def main():
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        match opcao_inicial:
            case 1:
                while True:
                    exibir_menu()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        nome = input("INFORME O NOME:\n>>>")
                        idade = int(input("INFORME A IDADE:\n>>>"))
                        cpf = input("INFORME O SEU CPF:\n>>>")
                        adicionar_usuario(nome, idade, cpf)
                    elif opcao == "2":
                        listar_usuario()
                    elif opcao == "3":
                        nome_antigo = input("INFORME O NOME PARA SER ATUALIZADO:\n>>>")
                        nome_novo = input("INFORME UM NOVO NOME:\n>>>")
                        idade_novo = int(input("INFORME A NOVA IDADE :\n>>>"))
                        cpf_novo = input("INFORME O NOVO CPF DO USUÁRIO:\n>>>")
                        atualizar_usuario(nome_antigo, nome_novo, idade_novo, cpf_novo)
                    elif opcao == "4":
                        usuario_nome = input("DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>>")
                        excluir_usuario(usuario_nome)
                    elif opcao == "5":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print("⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 2:
                print("🚀 SAINDO...")
                sleep(3)
                break
            case _:
                print("⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()        
                




