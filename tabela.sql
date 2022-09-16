CREATE TABLE `CAP_competencias_respostas` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`data` DATETIME,
	`nome` VARCHAR(200),
	`cat_atribuido` VARCHAR(200),
	`cat_desejado` VARCHAR(200),
	`Backups` INT,
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


#Timestamp,nome,atribuido,desejado,Backups,Hospedagem,e-mail,Cloud,DNS,Infraestrutura,Wifi,Estação,Servidor,Firewall,Devops,Monitoramento,ID