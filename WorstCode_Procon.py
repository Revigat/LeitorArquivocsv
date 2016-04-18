import csv
import sqlite3

def criar_tabela():
	'''
	Executar via Terminal 
	sqlite3 dados.db '.tables' # VERIFICA DE A TABELA FOI CRIADA
	sqlite3 dados.db 'PRAGMA table_info(dados)' # VERIFICA OS CAMPOS DA TABELA

	''' 
	try:
		query = """ 

			CREATE TABLE atendimentos (
			Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
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
		cone = sqlite3.connect('atendimentos.db') 
		cone.execute(query)
		cone.commit()
		cone.close()


		print("Criada com suecesso")

	except Exception as e:
		print(str(e))


def ler_dados():
	'''Faz a Leitura do arquivo csv'''
	#lista = []
	try:

		with open('boletim_2015.csv','r', encoding='utf-8', errors='ignore') as arquivocsv: # Não carrega na memoria
			leitura = csv.reader(arquivocsv, delimiter=';')
			#with open('temp.csv', 'w') as arquivocomirgula:

			for linhas in leitura:
				#arquivocomirgula.write(';'.join(linhas))
					#print(linhas)
					#print(linhas.replace(";" , ","))
					#print(','.join(linha))
					#inserir_dados(linhas)
					#print(linha_virg.split())
					#print(type(linhas))
				break
		return linhas


			#leitura = csv.reader(arquivocsv, delimiter=';')
			
			#for linha in leitura:
				#print(','.join(linha))
				#print(linha)
				#lista.append(linha)
				#break

		#print(lista)
		#inserir_dados(lista)
		arquivocsv.close()

	except Exception as e:
		print(str(e))

#lista_teste = ['2015','2','novemnbro','12/12/2012',1,'Curitiba','PR',1,'TESTE',1,'TESTE','TESTE',1,'F','34','11111111',1,'TESTE','TESTE',
		#'111111111111','TESTE','TESTE','TESTE',1,'TESTE']

def inserir_dados():
	
	dados = [(ler_dados())]

	try:
		cone = sqlite3.connect('atendimentos.db')

		inserir = '''INSERT INTO atendimentos (Id,AnoAtendimento, TrimestreAtendimento, MesAtendimento, DataAtendimento, CodigoRegiao,
		Regiao, UF, CodigoTipoAtendimento, DescricaoTipoAtendimento, CodigoAssunto, DescricaoAssunto, GrupoAssunto, CodigoProblema,
		DescricaoProblema, GrupoProblema, SexoConsumidor, FaixaEtariaConsumidor, CEPConsumidor, TipoFornecedor, RazaoSocialSindec,
		NomeFantasiaSindec, CNPJ, RadicalCNPJ, RazaoSocialRFB, NomeFantasiaRFB, CodigoCNAEPrincipal, DescricaoCNAEPrincipal)
		VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

		cone.executemany(inserir,dados)
		cone.commit()
		print("Dados inseridos com sucesso")
		cone.close()

	except Exception as e:
		print(str(e))
	

def selecionar_dados():

		cone = sqlite3.connect('atendimentos.db')

		selecionar = cone.execute('select * from atendimentos')

		for linhas in selecionar.fetchall():
			print(linhas)


if __name__ == "__main__":
	criar_tabela()
	ler_dados()
	inserir_dados()
	selecionar_dados()
