import csv
import random

# Função para carregar identificadores de CPF do arquivo de leads
def carregar_cpfs(arquivo_leads):
    identificadores_cpf = []

    # Carregar identificadores de CPF do arquivo de leads
    with open(arquivo_leads, 'r') as leads_file:
        leads_reader = csv.DictReader(leads_file)
        for linha in leads_reader:
            identificadores_cpf.append(linha['identificador_cpf_cnpj'])  # Adicionar o CPF à lista

    return identificadores_cpf

# Função para gerar o arquivo de interações de leads
def gerar_interacoes_leads(arquivo_leads, arquivo_saida):
    identificadores_cpf = carregar_cpfs(arquivo_leads)

    with open(arquivo_saida, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['identificador_cpf_cnpj', 'frequencia_visitas', 'tempo_total_navegacao'])

        # Garantir que todos os CPFs sejam utilizados e simular interações
        for cpf in identificadores_cpf:
            visitas = random.randint(1, 10)  # Frequência de visitas simulada
            tempo_navegacao = random.randint(5, 200)  # Tempo total de navegação simulada (em minutos)
            writer.writerow([cpf, visitas, tempo_navegacao])

# Chamada da função para gerar o arquivo
arquivo_leads = '../../data/ruptura_leads.csv'
arquivo_saida = '../../data/interacoes_leads2.csv'

gerar_interacoes_leads(arquivo_leads, arquivo_saida)
