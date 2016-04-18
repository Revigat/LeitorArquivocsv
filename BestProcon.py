import csv
import sqlite3

def criar_tabela():
	'''
	doc_string
	Executar via Terminal 
	sqlite3 dados.db '.tables' # VERIFICA DE A TABELA FOI CRIADA
	sqlite3 dados.db 'PRAGMA table_info(dados)' # VERIFICA OS CAMPOS DA TABELA
	
	''' 
	try:
		query = """ 
			CREATE TABLE atendimentos (
			AnoAtendimento INT, 
			TrimestreAtendimento INT,
			MesAtendimento INT,
			DataAtendimento CHARACTER(10),
			CodigoRegiao CHARACTER(2),
			Regiao CHARACTER(15),
			UF CHARACTER(2),
			CodigoTipoAtendimento INT,
			DescricaoTipoAtendimento VARCHAR(50),
			CodigoAssunto INT,
			DescricaoAssunto VARCHAR(150),
			GrupoAssunto VARCHAR(160),
			CodigoProblema INT,
			DescricaoProblema CHARACTER(160),
			GrupoProblema VARCHAR(160),
			SexoConsumidor VARCHAR(1),
			FaixaEtariaConsumidor VARCHAR(20),
			CEPConsumidor VARCHAR(8),
			TipoFornecedor INT,
			RazaoSocialSindec VARCHAR(100),
			NomeFantasiaSindec VARCHAR(100),
			CNPJ VARCHAR(14),
			RadicalCNPJ VARCHAR(8),
			RazaoSocialRFB VARCHAR(150),
			NomeFantasiaRFB VARCHAR(55),
			CodigoCNAEPrincipal VARCHAR(7),
			DescricaoCNAEPrincipal VARCHAR(250)
			);
		"""
		cone = sqlite3.connect('atendimentos.db') #Abre Conexão e cria o banco
		cone.execute(query) #executa a query
		cone.commit()
		cone.close() #Fecha conexão

		#print("Criada com suecesso")

	except Exception as e:
		print(str(e))

def inserir_dados():
	try:
		inserir = '''INSERT INTO atendimentos (AnoAtendimento, TrimestreAtendimento, MesAtendimento, DataAtendimento, CodigoRegiao,
		Regiao, UF, CodigoTipoAtendimento, DescricaoTipoAtendimento, CodigoAssunto, DescricaoAssunto, GrupoAssunto, CodigoProblema,
		DescricaoProblema, GrupoProblema, SexoConsumidor, FaixaEtariaConsumidor, CEPConsumidor, TipoFornecedor, RazaoSocialSindec,
		NomeFantasiaSindec, CNPJ, RadicalCNPJ, RazaoSocialRFB, NomeFantasiaRFB, CodigoCNAEPrincipal, DescricaoCNAEPrincipal)
		VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

		with open('boletim_2015.csv','r', encoding='utf-8', errors='ignore') as arquivocsv: # Faz leitura linha a linha sem colocar na memoria primeiro, codifica o arquivo para UTF-8

			leitura = csv.reader(arquivocsv, delimiter=';')

			for linhas in leitura:
				dados = [(linhas)]
				cone = sqlite3.connect('atendimentos.db', timeout=5)
				cone.executemany(inserir,dados)
				cone.commit()
				cone.close() #Fecha conexão
				#print("Dados inseridos com sucesso")
			arquivocsv.close() #Fecha arquivo

	except Exception as e:
		print(str(e))
	
def selecionar_dados():
	try:
		cone = sqlite3.connect('atendimentos.db', timeout=5)

		selecionar = cone.execute('select * from atendimentos')
			
		linhas = selecionar.fetchall()
		cone.close() #Fecha conexão	

		for row in linhas:
			print(row)
	except Exception as e:
	print(str(e))

if __name__ == "__main__": # Executa tanto como Linha de comando quanto por Programa
	criar_tabela()
	inserir_dados()
	selecionar_dados()
