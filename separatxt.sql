-- Function: separa_tx()

-- DROP FUNCTION separa_tx();

CREATE OR REPLACE FUNCTION separa_tx()
  RETURNS trigger AS
$BODY$
 declare 
 cnpj varchar(55);
 cli varchar(55);
 reg varchar(55);
tot double precision;
 
	BEGIN
	 IF SPLIT_PART(NEW.TXT,'|',1) = '1HEADER.TXT' THEN
	  RETURN NEW;
	 END IF;
	 IF SPLIT_PART(NEW.TXT,'|',1) = 'CCLI.TXT' THEN
	  INSERT INTO tmp_cliente(
            regiao, cliente, razao_social, fantasia, canal, classificacao, 
            motivo_cla, curva, posicao10, posicao11, ddd, fone, contato, 
            cargo, cnpj_cpf, consumidor, ie, limite_cred, tip_pagamento, 
            cond_pagamento, posicao22, posicao23, posicao24, data_criacao, 
            data_alteracao, posicao27, transportadora, posicao29, posicao30, 
            posicao31, posicao32, posicao33, posicao34, posicao35, posicao36, 
            end_principal, latitude, longetude, posicao40, seq, pasta, posicao44, 
            posicao45, grupo_canal, posicao47, posicao48, posicao49, posicao50, 
            reg, posicao52, posicao53, posicao54, posicao55, posicao56,posicao57) VALUES  (SPLIT_PART(NEW.TXT,'|',2),SPLIT_PART(NEW.TXT,'|',3),SPLIT_PART(NEW.TXT,'|',4),SPLIT_PART(NEW.TXT,'|',5),
            SPLIT_PART(NEW.TXT,'|',6),SPLIT_PART(NEW.TXT,'|',7),SPLIT_PART(NEW.TXT,'|',8),SPLIT_PART(NEW.TXT,'|',9),SPLIT_PART(NEW.TXT,'|',10),
            SPLIT_PART(NEW.TXT,'|',11),SPLIT_PART(NEW.TXT,'|',12),SPLIT_PART(NEW.TXT,'|',13),SPLIT_PART(NEW.TXT,'|',14),SPLIT_PART(NEW.TXT,'|',15),
            SPLIT_PART(NEW.TXT,'|',16),SPLIT_PART(NEW.TXT,'|',17),SPLIT_PART(NEW.TXT,'|',18),SPLIT_PART(NEW.TXT,'|',19),
            SPLIT_PART(NEW.TXT,'|',20),SPLIT_PART(NEW.TXT,'|',21),SPLIT_PART(NEW.TXT,'|',22),SPLIT_PART(NEW.TXT,'|',23),SPLIT_PART(NEW.TXT,'|',24),
            SPLIT_PART(NEW.TXT,'|',25),SPLIT_PART(NEW.TXT,'|',26),SPLIT_PART(NEW.TXT,'|',27),SPLIT_PART(NEW.TXT,'|',28),SPLIT_PART(NEW.TXT,'|',29),
            SPLIT_PART(NEW.TXT,'|',30),SPLIT_PART(NEW.TXT,'|',31),SPLIT_PART(NEW.TXT,'|',32),SPLIT_PART(NEW.TXT,'|',33),SPLIT_PART(NEW.TXT,'|',34),
            SPLIT_PART(NEW.TXT,'|',34),SPLIT_PART(NEW.TXT,'|',35),SPLIT_PART(NEW.TXT,'|',36),SPLIT_PART(NEW.TXT,'|',37),SPLIT_PART(NEW.TXT,'|',38),
            SPLIT_PART(NEW.TXT,'|',39),SPLIT_PART(NEW.TXT,'|',40),SPLIT_PART(NEW.TXT,'|',41),SPLIT_PART(NEW.TXT,'|',42),SPLIT_PART(NEW.TXT,'|',43),
            SPLIT_PART(NEW.TXT,'|',44),SPLIT_PART(NEW.TXT,'|',45),SPLIT_PART(NEW.TXT,'|',46),SPLIT_PART(NEW.TXT,'|',47),SPLIT_PART(NEW.TXT,'|',48),
            SPLIT_PART(NEW.TXT,'|',49),SPLIT_PART(NEW.TXT,'|',50),SPLIT_PART(NEW.TXT,'|',51),SPLIT_PART(NEW.TXT,'|',52),SPLIT_PART(NEW.TXT,'|',53),
            SPLIT_PART(NEW.TXT,'|',54),SPLIT_PART(NEW.TXT,'|',55));
            RETURN NEW;
	 END IF;
	 IF SPLIT_PART(NEW.TXT,'|',1) = 'VENCLI.TXT' THEN
	  RETURN NEW;
	 END IF;
	 IF SPLIT_PART(NEW.TXT,'|',1) = 'CLICRM.TXT' THEN
	  RETURN NEW;
	 END IF;
	 IF SPLIT_PART(NEW.TXT,'|',1) = 'CLIEND.TXT' THEN
	    
	    INSERT INTO tb_end(
            regiao, cliente, cod_end, tipo, nome_rua, num, bairro, cidade, 
            estado, cep)values (SPLIT_PART(NEW.TXT,'|',2),SPLIT_PART(NEW.TXT,'|',3),SPLIT_PART(NEW.TXT,'|',4),SPLIT_PART(NEW.TXT,'|',5),
            SPLIT_PART(NEW.TXT,'|',6),SPLIT_PART(NEW.TXT,'|',7),SPLIT_PART(NEW.TXT,'|',8),SPLIT_PART(NEW.TXT,'|',9),SPLIT_PART(NEW.TXT,'|',10),
            SPLIT_PART(NEW.TXT,'|',11));

	  RETURN NEW;
            
	 END IF;
	 IF SPLIT_PART(NEW.TXT,'|',1) = 'CAPAPEDIDO.TXT' THEN 

	     if SPLIT_PART(NEW.TXT,'|',14) = '' then
	      tot := 0.0;
             else            
              tot := cast(SPLIT_PART(NEW.TXT,'|',14) as double precision);
             end if;
            INSERT INTO TB_CAPAPEDIDO(carga, vendedor, regiao, cliente, carga_pedido, posicao7, 
            data_ped, data_1, data_2, posicao11, quant, descon, total, posicao15, 
            posicao16, posicao17, posicao18, posicao19, posicao20, posicao21, 
            posicao22, posicao23, posicao24, posicao25, posicao26, posicao27, 
            posicao28, posicao29, posicao30, posicao31, posicao32, posicao33, 
            posicao34, posicao35) VALUES (SPLIT_PART(NEW.TXT,'|',2),SPLIT_PART(NEW.TXT,'|',3),SPLIT_PART(NEW.TXT,'|',4),SPLIT_PART(NEW.TXT,'|',5),
            SPLIT_PART(NEW.TXT,'|',6),SPLIT_PART(NEW.TXT,'|',7),SPLIT_PART(NEW.TXT,'|',8),SPLIT_PART(NEW.TXT,'|',9),SPLIT_PART(NEW.TXT,'|',10),
            SPLIT_PART(NEW.TXT,'|',11),cast(SPLIT_PART(NEW.TXT,'|',12) as integer),SPLIT_PART(NEW.TXT,'|',13),tot,SPLIT_PART(NEW.TXT,'|',15),
            SPLIT_PART(NEW.TXT,'|',16),SPLIT_PART(NEW.TXT,'|',17),SPLIT_PART(NEW.TXT,'|',18),SPLIT_PART(NEW.TXT,'|',19),
            SPLIT_PART(NEW.TXT,'|',20),SPLIT_PART(NEW.TXT,'|',21),SPLIT_PART(NEW.TXT,'|',22),SPLIT_PART(NEW.TXT,'|',23),SPLIT_PART(NEW.TXT,'|',24),
            SPLIT_PART(NEW.TXT,'|',25),SPLIT_PART(NEW.TXT,'|',26),SPLIT_PART(NEW.TXT,'|',27),SPLIT_PART(NEW.TXT,'|',28),SPLIT_PART(NEW.TXT,'|',29),
            SPLIT_PART(NEW.TXT,'|',30),SPLIT_PART(NEW.TXT,'|',31),SPLIT_PART(NEW.TXT,'|',32),SPLIT_PART(NEW.TXT,'|',33),SPLIT_PART(NEW.TXT,'|',34),
            SPLIT_PART(NEW.TXT,'|',35));
	  RETURN NEW;		
	 END IF;
	 IF SPLIT_PART(NEW.TXT,'|',1) = 'ITEMPEDIDO.TXT' THEN 
            INSERT INTO tb_pedido(
            carga, vendedor, regiao, cliente, carga_pedido, item, 
            ocorencia, quant, desconto, tabela, total, posicao13, posicao14, 
            posicao15, posicao16, unitario, posicao18, posicao19, posicao20, 
            posicao21, posicao22, posicao23, posicao24, posicao25, posicao26, 
            posicao27, posicao28, posicao29, posicao30, posicao31, posicao32, 
            posicao33, posicao34, posicao35, posicao36, posicao37, posicao38,posicao39) VALUES (SPLIT_PART(NEW.TXT,'|',2),SPLIT_PART(NEW.TXT,'|',3),SPLIT_PART(NEW.TXT,'|',4),
            SPLIT_PART(NEW.TXT,'|',5),
            SPLIT_PART(NEW.TXT,'|',6),SPLIT_PART(NEW.TXT,'|',7),SPLIT_PART(NEW.TXT,'|',8),cast(SPLIT_PART(NEW.TXT,'|',9) as integer),SPLIT_PART(NEW.TXT,'|',10),
            SPLIT_PART(NEW.TXT,'|',11),cast(SPLIT_PART(NEW.TXT,'|',12) as double precision),SPLIT_PART(NEW.TXT,'|',13),SPLIT_PART(NEW.TXT,'|',14),sPLIT_PART(NEW.TXT,'|',15),
            SPLIT_PART(NEW.TXT,'|',16),cast(SPLIT_PART(NEW.TXT,'|',17) as double precision),SPLIT_PART(NEW.TXT,'|',18),SPLIT_PART(NEW.TXT,'|',19),
            SPLIT_PART(NEW.TXT,'|',20),SPLIT_PART(NEW.TXT,'|',21),SPLIT_PART(NEW.TXT,'|',22),SPLIT_PART(NEW.TXT,'|',23),SPLIT_PART(NEW.TXT,'|',24),
            SPLIT_PART(NEW.TXT,'|',25),SPLIT_PART(NEW.TXT,'|',26),SPLIT_PART(NEW.TXT,'|',27),SPLIT_PART(NEW.TXT,'|',28),SPLIT_PART(NEW.TXT,'|',29),
            SPLIT_PART(NEW.TXT,'|',30),SPLIT_PART(NEW.TXT,'|',31),SPLIT_PART(NEW.TXT,'|',32),SPLIT_PART(NEW.TXT,'|',33),SPLIT_PART(NEW.TXT,'|',34),
            SPLIT_PART(NEW.TXT,'|',34),SPLIT_PART(NEW.TXT,'|',35),SPLIT_PART(NEW.TXT,'|',36),SPLIT_PART(NEW.TXT,'|',38),SPLIT_PART(NEW.TXT,'|',39));
	  RETURN NEW;		
	 END IF;
	 
         IF SPLIT_PART(NEW.TXT,'|',1) = 'CEVS.TXT' THEN
	  RETURN NEW;
	 END IF;
return new;
	END;

$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION separa_tx()
  OWNER TO postgres;
