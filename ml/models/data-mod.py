import csv
import random

# Função para gerar o novo arquivo com as alterações
def modificar_ruptura_leads(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        headers = next(reader)
        # Modificar o header "temos_telefone?" para "temos_login?" e adicionar "whatsapp_ou_ligacao"
        new_headers = ['temos_login?', 'Status', 'CreatedDate', 'InteressesLead__c', 'identificador_placa', 'DataDaUltimaVisitaAgendada__c', 'identificador_cpf_cnpj', 'whatsapp_ou_ligacao']
        writer.writerow(new_headers)

        # Processar cada linha e adicionar a nova coluna "whatsapp_ou_ligacao"
        for row in reader:
            temos_login = row[0]  # Copiamos o valor de "temos_telefone?" para "temos_login?"
            whatsapp_ou_ligacao = random.choice(['w', 'l'])  # Simular escolha de contato (WhatsApp ou Ligação)
            new_row = row[:7] + [whatsapp_ou_ligacao]  # Manter as 7 colunas originais e adicionar a nova
            writer.writerow(new_row)

# Executar a função
modificar_ruptura_leads('../../data/ruptura_leads.csv', 'ruptura_leads_modificado.csv')