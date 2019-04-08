#!/usr/bin/python

import os, sys
import pymssql
import psycopg2


conn = pymssql.connect("#############", "#############", '#############', '#############')#criando conexção com servidor Postgresql.

cursor = conn.cursor()





con = psycopg2.connect(host='#############', database='#############', user='#############', password='#############', port='5432')#criando conexção com servidor SQL Server.
cur = con.cursor()

#comando para limpar da base de dados as informações referente ao ultimo mês fechado e o mês atual.
sql1 = "DELETE FROM tb_Vendas where Extract('Month' from cast(data_nf as date)) = Extract('Month' from Now()) or Extract('Month' from cast(data_nf as date)) = Extract('Month' from Now())-1"
cur.execute(sql1)
con.commit()
sql2 = "SET CLIENT_ENCODING TO 'latin8';"
cur.execute(sql2)
con.commit()
     
cursor.execute('SELECT B.CODPDD AS PED,B.CODCET AS CLIENTE, B.DATETGPDD AS DATA_PED, B.NUMDOCPDD AS NF,B.DATEMSDOCPDD AS DATA_NF, A.NUMVRSVLDTABVRS AS VERSAO, A.NUMTABPRMPRE AS TABELA, A.CODCATITE,(A.QTDITEPDD/C.QTDUNICXACATITE) AS QUANT,A.VALTOTITEPDD,B.CODCNDPGTRVD AS COND_PAS,     B.CODVEC AS VEICULO, B.NUMVIAVEC AS VIAGEM, B.CODCFO,B.INDSTUMVTPDD,B.CODMTCEPG AS VEND,B.CODTPOMTV ,B.CODMTV,B.DATEMSDVLPDD FROM FLEXX00111200.DBO.IBETITEPDD AS A INNER JOIN FLEXX00111200.DBO.IBETPDD AS B ON A.CODPDD = B.CODPDD INNER JOIN FLEXX00111200.DBO.IBETCATITE AS C ON A.CODCATITE = C.CODCATITE WHERE (DATEPART(mm,B.DATEMSDOCPDD) = DATEPART(mm,GETDATE()) OR DATEPART(mm,B.DATEMSDOCPDD) = DATEPART(mm,GETDATE())-1) AND DATEPART(yyyy,B.DATEMSDOCPDD) = DATEPART(yyyy,GETDATE())');
cursor.fetchone()
for row in cursor:
    cur.execute("INSERT INTO tb_Vendas(ped,cliente,data_ped,nf,data_nf,versao,tabela,codcatite,quant, valtotitepdd, cond_pag, veiculo, viagem, codcfo, indstumvtpdd,vend,codtpomtv, codmtv, datemsdvlpdd) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)

sql1 = "DELETE FROM tb_cliente"
cur.execute(sql1)
con.commit()
sql2 = "SET CLIENT_ENCODING TO 'latin8';"
cur.execute(sql2)
con.commit()
      
cursor.execute('SELECT DISTINCT a.CODCET AS CLIENTE,a.NOMRAZSCLCET AS RAZAO,a.NOMFTSCET AS FANTASIA,a.CODCGCCPFCET AS CPF_CNPJ,a.CODCTI AS CANAL,a.NUMICCETACET AS INSCRICAO,a.VALSLDCET AS LIMITE_CONS ,a.VALLMTCDTCET AS LIMITE,a.DATCADCET AS DIA_CAD,a.TPOSTUCET AS STATUS,a.DESEMLCET AS EMAIL,a.LATCET AS LATITUDE,a.LONCET AS LONGE,b.CODMTCEPGVDD AS VENDEDOR,c.CODDIASMN AS DIA_VISITA,c.NUMSEQVST AS SEQ_VISITA,c.DESCCOVSTCET AS CICLO_VISITA,d.INDTPOLGR  AS TIPO,d.DESLGRCET  AS ENDE,(SELECT e.DESBRO FROM FLEXX00111200.dbo.IBETBRO AS e WHERE e.CODBRO = d.CODBRO AND e.CODCDD = d.CODCDD) AS BAIRRO,f.DESCDD  AS CIDADE,d.CODCEPCET  AS CEP,a.BOLBLDCET AS BLOQUEIO ,H.DESCNDPGT AS COND_PAGAMENTO FROM FLEXX00111200.dbo.IBETCET as a  JOIN FLEXX00111200.dbo.IBETPDRGPOCMZMRCCET AS b ON a.CODCET = b.CODCET JOIN FLEXX00111200.dbo.IBETVSTCET AS c ON a.CODCET = c.CODCET JOIN FLEXX00111200.dbo.IBETEDRCET as d ON a.CODCET = d.CODCET JOIN FLEXX00111200.dbo.IBETCDD AS f ON f.CODCDD = d.CODCDD join FLEXX00111200.DBO.Ibetpdrgpocmzmrccet AS G ON A.CODCET = G.CODCET INNER JOIN FLEXX00111200.DBO.IBETCNDPGT AS H ON B.CODCNDPGTRVD = H.CODCNDPGT');
cursor.fetchone()
for row in cursor:
    cur.execute("INSERT INTO tb_cliente(cliente, razao, fantasia, cpf_cnpj, canal, inscricao, limit_cons,limite, dia_cad, status, email, latitude, longe, vendedor, dia_vis,seq_vis, ciclo_visita, tipo, endereco, bairro, cidade, cep, bloqueio, cond_pag) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",row)

sql1 = "DELETE FROM tb_comodato"
cur.execute(sql1)
con.commit()
sql2 = "SET CLIENT_ENCODING TO 'latin8';"
cur.execute(sql2)
con.commit()
      
cursor.execute('SELECT A.CODCET, A.NUMMDT,B.CODCATITE, B.QTDITEMDT AS QUANT_COMODATADO,B.QTDRLH AS QUANT_RECOLIDA,A.DATEMSMDT AS DATA_COMODATO, A.DATVCMMDT AS VENCIMENTO, A.STUMDT AS STATUS FROM FLEXX00111200.DBO.IBETMDT AS A INNER JOIN FLEXX00111200.DBO.IBETITEMDT AS B ON A.NUMMDT = B.NUMMDT');
cursor.fetchone()
for row in cursor:
    cur.execute("INSERT INTO tb_comodato(codcet, nummdt, codcatite, quant_comodatado, quant_recolida,data_comodato, vencimento, status)VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",row)

sql1 = "DELETE FROM tb_produto"
cur.execute(sql1)
con.commit()
sql2 = "SET CLIENT_ENCODING TO 'latin8';"
cur.execute(sql2)
con.commit()
      
cursor.execute('SELECT A.CODCATITE, A.CODMRC, D.NOMMRC,A.CODFAMITE, E.DESFAMITE,A.DESCATITE,A.QTDUNICXACATITE,A.VALLTOCATITE, B.CODGPOGDDITEPFM, C.DESGPOGDDITEPFM FROM FLEXX00111200.DBO.IBETCATITE AS A INNER JOIN FLEXX00111200.DBO.IBETPGVGPOGDDITEPFMBND AS B ON A.CODCATITE = B.CODCATITE INNER JOIN FLEXX00111200.DBO.IBETGPOGDDITEPFM AS C ON B.CODGPOGDDITEPFM = C.CODGPOGDDITEPFM INNER JOIN FLEXX00111200.DBO.IBETMRC AS D ON A.CODMRC = D.CODMRC INNER JOIN FLEXX00111200.DBO.IBETFAMITE AS E ON A.CODFAMITE = E.CODFAMITE');
cursor.fetchone()
for row in cursor:
    cur.execute("INSERT INTO tb_produto(codcatite, codmrc, nommrc, codfamite, desfamite, descatitte,qtdunicxacatite, valltocatite, codgpogdditepfm, desgpogdditepfm) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)",row)

sql1 = "DELETE FROM tb_entradas"
cur.execute(sql1)
con.commit()
sql2 = "SET CLIENT_ENCODING TO 'latin8';"
cur.execute(sql2)
con.commit()
      
cursor.execute('SELECT A.DATEMSNF_LVRFCL AS DATA_ENTRADA, A.NUMNF_LVRFCL AS NF,A.CODCATITE AS CODIGO, A.VALITENF_ETQFCLITE AS VALOR, A.QTDITENF_ETQFCLITE AS TOTAL,B.CODFND AS FORNECEDOR FROM FLEXX00111200.DBO.IRFTETQFCLITE AS A INNER JOIN FLEXX00111200.DBO.IRFTLVRFCL AS B ON B.NUMNF_LVRFCL = A.NUMNF_LVRFCL AND A.CODSERNF_LVRFCL = B.CODSERNF_LVRFCL');
cursor.fetchone()
for row in cursor:
    cur.execute("INSERT INTO tb_entradas(data_entrada, nf, codigo, valor, total, fornecedor) VALUES (%s, %s, %s, %s, %s, %s)",row)


sql1 = "DELETE FROM tb_fornecedor"
cur.execute(sql1)
con.commit()
sql2 = "SET CLIENT_ENCODING TO 'latin8';"
cur.execute(sql2)
con.commit()
      
cursor.execute('SELECT CODFND AS CODIGO, NOMRAZSCLFND AS RAZAO,NOMFTSFND AS FANTASIA, CODCGCFND FROM FLEXX00111200.DBO.ISPTFND');
cursor.fetchone()
for row in cursor:
    cur.execute("INSERT INTO tb_fornecedor(codigo, razao, fantasia, codcfcfnd) VALUES (%s, %s, %s, %s)",row)

sql1 = "DELETE FROM tb_hierarquia"
cur.execute(sql1)
con.commit()
sql2 = "SET CLIENT_ENCODING TO 'latin8';"
cur.execute(sql2)
con.commit()
      
cursor.execute('SELECT A.CODMTCEPG,A.NOMEPG, A.CODFTRCPLEPG AS COD_FAT,B.CODMTCEPGRPS FROM FLEXX00111200.DBO.IBETCPLEPG  AS A  INNER JOIN FLEXX00111200.DBO.IBETSBN AS B ON A.CODMTCEPG = B.CODMTCEPGSBN');
cursor.fetchone()
for row in cursor:
    cur.execute("INSERT INTO tb_hierarquia(vd, nome, cod_fat, sv)VALUES (%s, %s, %s, %s)",row)

con.commit()
conn.close()

     