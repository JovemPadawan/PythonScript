import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3e0564c05c68e811feafe66433ca217b"
# Your Auth Token from twilio.com/console
auth_token  = "5a0d862706736537f5fe679e386ab4d3"
client = Client(account_sid, auth_token)


#Abrir os arquivos em excell

#DICA: toda lista no PYTHON fica entre colchetes []
#DICA: comando 'for' repete "para cada ### executar CODIGO" / "for VARIAVEL in [LISTA]
#DICA:f = formatar /.format
#DICA: quando der o comando .loc ele mostra uma tabela, ao colocar .values [0] voce diz que quer somente os numeros 

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    #print (mes) Para nao printar todos os meses
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print (tabela_vendas) Para nao printar todos os meses
    
    #Para cada arquivo:
        #Verificar se algum valor na coluna (B) VENDAS daquele arquivo e maior que 55.00;
        
    if (tabela_vendas ['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc [tabela_vendas ['Vendas'] > 55000, 'Vendedor'].values [0]
        vendas = tabela_vendas.loc [tabela_vendas ['Vendas'] > 55000, 'Vendas'].values [0]
        print (f'Encontramos o colaborador que fez um número de vendas maior do que 55.000 no mês de {mes}.\nFuncionário: {vendedor}\nNúmero de vendas: {vendas}')
        message = client.messages.create(
            to="+5519987500504", 
            from_="+13856007038",
            body= f'Encontramos o colaborador que fez um número de vendas maior do que 55.000 no mês de {mes}.\nFuncionário: {vendedor}\nNúmero de vendas: {vendas}')        
        print(message.sid)
           







        
        
        
    
    
    
    
        #Se for maior que 55.000 --> Envia um SMS com o Nome, o mes e as vendas do colaborador;
        
        #Caso nao seja >55.000 nao fazer nada;