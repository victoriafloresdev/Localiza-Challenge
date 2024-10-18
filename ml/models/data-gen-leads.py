import csv
import random

# Função para carregar identificadores de um arquivo CSV
def carregar_identificadores(arquivo_veiculos, arquivo_leads):
    identificadores_placa = set()
    identificadores_cpf = set()

    # Carregar identificadores de placa do arquivo de veículos
    with open(arquivo_veiculos, 'r') as veiculos_file:
        veiculos_reader = csv.DictReader(veiculos_file)
        for linha in veiculos_reader:
            identificadores_placa.add(linha['identificador_placa'])

    # Carregar identificadores de CPF do arquivo de leads
    with open(arquivo_leads, 'r') as leads_file:
        leads_reader = csv.DictReader(leads_file)
        for linha in leads_reader:
            identificadores_cpf.add(linha['identificador_cpf_cnpj'])

    return list(identificadores_placa), list(identificadores_cpf)

# Função para gerar o arquivo de interações com identificadores de placa e CPF dos arquivos de entrada
def gerar_interacoes(arquivo_veiculos, arquivo_leads, arquivo_saida, num_interacoes=1000):
    identificadores_placa, identificadores_cpf = carregar_identificadores(arquivo_veiculos, arquivo_leads)

    with open(arquivo_saida, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['identificador_cpf_cnpj', 'identificador_placa', 'clique', 'favoritou'])

        # Gerar interações de forma aleatória sem garantir que todos os CPFs e placas sejam usados
        for _ in range(num_interacoes):
            cpf = random.choice(identificadores_cpf)
            placa = random.choice(identificadores_placa)
            clique = random.choice([0, 1])
            favoritou = random.choice([0, 1]) if clique else 0
            writer.writerow([cpf, placa, clique, favoritou])

# Chamada da função para gerar o arquivo
arquivo_veiculos = '../../data/ruptura_vehicles.csv'
arquivo_leads = '../../data/ruptura_leads.csv'
arquivo_saida = '../../data/interacoes_clientes.csv'

# Gerar interações aleatórias (ajustável por num_interacoes)
gerar_interacoes(arquivo_veiculos, arquivo_leads, arquivo_saida, num_interacoes=1000)
