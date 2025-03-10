# Importa o módulo http.client para realizar solicitações HTTP e HTTPS
import http.client

# Importa o módulo json para manipular dados no formato JSON
import json

def obter_dados_empresa_por_cnpj(cnpj):
    
    """
    Esta função consulta a API do ReceitaWS para obter informações
                sobre uma empresa com base em seu CNPJ.
    
    Parâmetros:
    cnpj (str): O CNPJ para o qual as informações da empresa 
                devem ser consultadas.
    
    Retorna:
    dict ou str: Retorna um dicionário contendo as informações da 
                empresa, ou uma mensagem de erro se o CNPJ não for encontrado.
    """
    
    # Cria uma conexão HTTPS com o servidor 'www.receitaws.com.br', que hospeda a API do ReceitaWS.
    conexao = http.client.HTTPSConnection("www.receitaws.com.br")
    
    # Formata e envia uma requisição GET ao servidor ReceitaWS.
    # A requisição inclui o CNPJ fornecido na URL.
    # '/v1/cnpj/{cnpj}' especifica o formato da API que inclui o
    # CNPJ e espera a resposta em formato JSON.
    # O método 'request' realiza a solicitação ao servidor
    # com o método HTTP 'GET'.
    conexao.request("GET", f"/v1/cnpj/{cnpj}")
    
    # Aguarda a resposta do servidor à solicitação feita
    # anteriormente e armazena essa resposta no objeto 'resposta'.
    resposta = conexao.getresponse()
    
    # Lê o conteúdo completo da resposta HTTP, que é
    # enviado pelo servidor em formato de bytes.
    dados = resposta.read()
    
    # Decodifica os bytes recebidos para uma string usando UTF-8.
    # Converte a string JSON decodificada em um dicionário Python
    # usando o método 'loads' do módulo json.
    empresa = json.loads(dados.decode("utf-8"))
    
    # Encerra a conexão HTTPS com o servidor ReceitaWS.
    conexao.close()
    
    # Verifica se a chave 'status' no dicionário de empresa indica erro.
    if empresa.get('status', '') == 'ERROR':
        
        # Se houver erro, retorna uma mensagem de erro, que é
        # de CNPJ não encontrado ou serviço indisponível.
        return empresa.get('message', 'Erro desconhecido.')
        
    else:
        
        # Se não houver erro, retorna o dicionário contendo as
        # informações da empresa.
        return empresa

# Exemplo de uso da função

# Especifica um CNPJ exemplo para consulta
cnpj_exemplo = "06947283000160"

# Utiliza a função para obter as informações da empresa relacionada ao CNPJ
dados_empresa = obter_dados_empresa_por_cnpj(cnpj_exemplo)

# Exibe as informações da empresa ou a mensagem de erro resultante
print(dados_empresa)
