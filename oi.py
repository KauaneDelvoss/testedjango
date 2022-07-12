
#endereco_ip = str(input(f"Endereço de IP: "))
#mascara_ip = str(input(f"Máscara do Endereço: "))
#contagem_em_bits = int(input(f"Contagem em bits da mascara de rede desejada: "))



endereco_ip = str('192.128.32.0')
mascara_ip = str('255.255.255.0')
contagem_em_bits = 26



soma = contagem_em_bits - 24

hosts = 0
redes = 2 ** soma

for a in reversed(range(8)) :
    if soma != 0 :
        hosts += 2 ** a
    else : 
        break
    soma -= 1

    enderecos_redes = []
    broadcasts_redes = []

    endereco = endereco_ip.split('.')
    mascara = mascara_ip.split('.')
    r = 0
    b = 0

    for i in range(redes)  :
        
        r += 2 ** a
        b += 2 ** a
        enderecos_redes.append(endereco[0] + '.' + endereco[1] + '.' + endereco[2] + '.' + str(r))
        broadcasts_redes.append(endereco[0] + '.' + endereco[1] + '.' + endereco[2] + '.' + str(b))
        

    print(f'enderecos_redes : {enderecos_redes}')
    print(f'broadcasts_redes : {broadcasts_redes}')
print(f"NÚMERO DE HOSTS POR REDE: {hosts - 2} \nNÚMERO DE REDES DISPONÍVEIS: {redes}")

#--------------------------------------------------------------------------------------------



