banco_dados = []

    
def cadastro_parceiro(nome, end, tel, cid, uf):
    oficina = { #dict_cadastro 
        'Nome': nome,
        'Endereço': end,
        'Telefone': tel,
        'Cidade': cid,
        'Estado': uf
    }
    banco_dados.append(oficina)#armazena o cadastro na lista
    print(f'Oficina {nome} cadastrada com sucesso!')
    #f' - me permite manipular a string e colocar ela em qualque lugar
    
    return True
    
tupla = (MA,CE)

def buscar_parceiro(uf):
    result = []#armazena os estados
    #for váriavel nova in iteravel    
    for parceiro in banco_dados: #aqui a váriavel parceiro vai percorrer cada item da lista
        if parceiro['Estado'].lower() == uf.lower():
            #.lower() transforma as strings em minusculas para facilitar a comparação
            result.append(parceiro)#adiciona parceiro a lista result
            
    return result
                       
print ('Programa de Cadastro Para Parceiros\n')
while True:
    op = int(input('[1] cadastro\n[2] Buscar\n[0] Sair\nopção: '))
    if op == 1:
        print('\t↓ Preencha os dados abaixo ↓\n')
        nome_1 = input("Nome: ")
        end_1 = input("Endereço: ")
        tel_1 = input('Telefone: ')
        cid_1 = input("Cidade: ")
        uf_1 = input("Estado: ")
        cad = cadastro_parceiro(nome_1, end_1, tel_1, cid_1, uf_1)
    elif op == 2:
        estado = input('Digite o UF: ') 
        res = buscar_parceiro(estado)#chamo 
        #tenho que usar um for para percorrer todos os dados
        #structure = for variavel in variavel iterável (qlqr variavel quw da pra percorrer)
        
        for mostrar in res:
            print('\t==== Oficina Credenciada ====\n')
            print(f'Oficina: {nome_1}')
            print(f'Endereço: {end_1}')
            print(f'Telefone: ({tel_1[:2]}) {tel_1[2:7]}-{tel_1[7:]}')
            print(f'Cidade: {cid_1}')
            print(f'Estado: {uf_1}')
    elif op == 0:
        break