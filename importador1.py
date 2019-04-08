#!/usr/bin/python

import os, sys

import psycopg2
con = psycopg2.connect(host='107.161.191.50', database='STOP-SCHIN', user='postgres', password='!@#$1234abcd', port='5432')
cur = con.cursor()
# Open a file
path = "/usr/txt/"
dirs = os.listdir( path )
i = 1
# This would print all the files and directories
for file in dirs:
   
   if file == "PEDIDOS.CSV":
      sql1 = "DELETE FROM TB_PEDIDO_CONTROL WHERE DT_PEDIDO LIKE'%/12/2016'"
      cur.execute(sql1)
      con.commit()
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy tb_pedido_control from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'PEDIDOS IMPORTADOS'
   if file == "compra.csv":
      sql1 = "DELETE FROM COMPRAS WHERE MES='12'"
      cur.execute(sql1)
      con.commit()
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy compras from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'COMPRAS IMPORTADAS'
   if file == "meta_bk.csv":
      sql1 = "DELETE FROM meta_bk WHERE MES='12'"
      cur.execute(sql1)
      con.commit()
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy meta_bk from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'METAS BK IMPORTADAS'
   if file == "PRODUTOS.CSV":
      sql1 = "DELETE FROM PRODUTO"
      cur.execute(sql1)
      con.commit()
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy produto from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'PRODUTOS IMPORTADOS'
   if file == "tit_pagar.csv":
      sql1 = "DELETE FROM tit_pagar"
      cur.execute(sql1)
      con.commit()
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy tit_pagar(dt_entrada, tp, documento, parc, camp, cod_forn, razao_social, valor, dt_vencimento, dt_pagamento, banco, camp1) from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'TITULOS_PAGAR IMPORTADOS'
   if file == "tit_receber.csv":
      sql1 = "DELETE FROM tit_receber"
      cur.execute(sql1)
      con.commit()
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy tit_receber(dt_lancamento, documento, cod_cliente, razao_social, valor, contabil, dt_vencimento, dt_pagamento, banco) from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'TITULOS_RECEBER IMPORTADOS'
   if file == "fornecedor.csv":
      sql1 = "DELETE FROM fornecedor"
      cur.execute(sql1)
      con.commit()
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy fornecedor(razao, cod_forn, cpf, fantasia, conta_contabil, status)  from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'FORNECEDORES IMPORTADOS'
   if file == "CLIENTES.CSV":
      sql1 = "DELETE FROM TB_CLIENTE_CONTROL"
      cur.execute(sql1)
      con.commit()
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy tb_cliente_control from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'CLIENTES IMPORTADOS'
   if file == 'cev.csv':
      sql1 = "DELETE FROM COMODATO_ATIVOS"
      cur.execute(sql1)
      con.commit()
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy comodato_ativos from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'CEVS IMPORTADOS'
   if file == 'vdgr091.CSV':
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy meta(produto, umb, vendedor, mes, ano) from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'METAS IMPORTADOS'
   if file == "visita.csv":
      sql1 = "DELETE FROM visita"
      cur.execute(sql1)
      con.commit()
      sql2 = "SET CLIENT_ENCODING TO 'latin8';"
      cur.execute(sql2)
      con.commit()
      sql = "copy visita from '/usr/txt/"+file+"' delimiter ';'"
      cur.execute(sql)
      con.commit()
      print 'DEDO DURO IMPORTADO'
   arquivo,teste = file.split('.')   
   if teste == 'TXT':
      sql = "copy import1(txt) from '/usr/txt/"+file+"'"
      cur.execute(sql)
      con.commit()   
      print 'arquivo '+file+' importado'		         
      sql2 = "update tb_pedido set total=0 where ocorencia = '002' or ocorencia = '003' or ocorencia = '004'"
      cur.execute(sql2)
      con.commit()
   
	  
	  
	  
con.close()
