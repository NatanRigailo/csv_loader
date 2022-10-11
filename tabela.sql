CREATE TABLE `CAP_competencias_respostas` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`data` DATETIME,
	`nome` VARCHAR(200),
	`cat_atribuido` VARCHAR(200),
	`cat_desejado` VARCHAR(200),
	`Backups` INT,
	`Banco_de_dados` INT,
	`Hospedagem` INT,
	`e-mail` INT,
	`Cloud` INT,
	`DNS` INT,
	`Infraestrutura` INT,
	`Wifi` INT,
	`Estação` INT,
	`Servidor` INT,
	`Firewall` INT,
	`Devops` INT,
	`Monitoramento` INT,
	`tec_id` INT,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;


-- #Timestamp,nome,atribuido,desejado,Backups,Hospedagem,e-mail,Cloud,DNS,Infraestrutura,Wifi,Estação,Servidor,Firewall,Devops,Monitoramento,ID
-- 2022/09/08 1:00:25 PM GMT-3
-- ,William Fernandes
-- ,DNS;Estação;Suporte;Clientes
-- ,Banco de dados;Hospedagem;Cloud;Servidor;Firewall;Devops;Clientes
-- ,2
-- ,2
-- ,2
-- ,3
-- ,2
-- ,2
-- ,2
-- ,2
-- ,3
-- ,3
-- ,2
-- ,1
-- ,2
-- ,123
