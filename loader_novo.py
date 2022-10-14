import csv
import mysql.connector




mydb = mysql.connector.connect(
  host="172.26.0.151",
  user="glpiplss",
  password="28894jCJ9218jdasdh128addd2",
  database="bdglpiplss"
)

print(mydb)
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

with open('final.csv') as csvfile:
    # Timestamp,nome,atribuido,desejado,Backups,Hospedagem,e-mail,Cloud,DNS,Infraestrutura,Wifi,Estação,Servidor,Firewall,Devops,Monitoramento,ID
    csvfile.seek(0)
    reader = csv.reader(csvfile, delimiter=',')
    mycursor = mydb.cursor()
    with open('SUPERVISORES.csv') as processado:
        linha=0
        a = [None] * 18
        leitor = csv.reader(processado, delimiter=',')
        for row in leitor:
            for x in range(18):
                a[x]=row[x]
            if linha == 0:
                print("nada")
            else:
                # print(a)
                # print(row)
                # print(len(row))
                # print(valores)
                sql2= "INSERT INTO teste.CAP_competencias_respostas (`data`, nome, cat_atribuido, cat_desejado, Backups,Banco_de_dados, Hospedagem, `e-mail`, Cloud, DNS, Infraestrutura, Wifi, Estação, Servidor, Firewall, Devops, Monitoramento, tec_id) VALUES('"+row[0]+"','"+row[1]+"','"+row[3]+"',"+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+"','"+row[2]+")"
                #print("%s" % row[0])
                print(sql2)
                # mycursor.execute(sql, row)
                #mycursor.execute(sql2)
                #mydb.commit()
            linha += 1
    linha=0
    for row in reader:
        if linha != 0:
            print('nome:'+ row[1])
            # teste=array_funções(row[2])
            # print(teste)
        linha += 1

