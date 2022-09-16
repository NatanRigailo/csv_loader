import csv
# with open('respostas.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
#         for row in spamreader:
#             print(', '.join(row))
def array_funções(fun):
    # print(fun)
    a_fun=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    if 'Backup' in fun:
        a_fun[0]=1
    if 'Banco de dados' in fun:
        a_fun[1]=1
    if 'Hospedagem' in fun:
        a_fun[2]=1
    if 'e-mail' in fun:
        a_fun[3]=1
    if 'Cloud' in fun:
        a_fun[4]=1
    if 'DNS' in fun:
        a_fun[5]=1
    if 'Infraestrutura' in fun:
        a_fun[6]=1
    if 'Wifi' in fun:
        a_fun[7]=1
    if 'Estação' in fun:
        a_fun[8]=1
    if 'Servidor' in fun:
        a_fun[9]=1
    if 'Firewall' in fun:
        a_fun[10]=1
    if 'Devops' in fun:
        a_fun[11]=1
    if 'Monitoramento' in fun:
        a_fun[12]=1
    if 'Suporte' in fun:
        a_fun[13]=1
    if 'Clientes' in fun:
        a_fun[14]=1
    if 'Triagem' in fun:
        a_fun[15]=1

    return(a_fun)

with open('respostas.csv') as csvfile:
    #dialect = csv.Sniffer().sniff(csvfile.read(1024))
    # teste= csv.Sniffer().has_header(csvfile.read(1024))
    # print(teste)
    # Timestamp,nome,atribuido,desejado,Backups,Hospedagem,e-mail,Cloud,DNS,Infraestrutura,Wifi,Estação,Servidor,Firewall,Devops,Monitoramento,ID
    csvfile.seek(0)
    reader = csv.reader(csvfile, delimiter=',')
    i=input("processar?(n/y)")
    if i == 'y':
        with open('novo.csv', mode='w') as novocsv:
            linha=0
            for row in reader:
                if linha == 0:
                    row.append('ID')
                    escritor = csv.writer(novocsv,delimiter=',')
                    escritor.writerow(row)
                else:
                    print('nome:'+ row[1])
                    id = input("ID: ")
                    row.append(id)
                    escritor = csv.writer(novocsv,delimiter=',')
                    escritor.writerow(row)
                linha += 1
    linha=0
    for row in reader:
        if linha != 0:
            #print('nome:'+ row[1])
            # teste=array_funções(row[2])
            # print(teste)
        linha += 1
        