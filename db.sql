CREATE TABLE Calcul(
	guid VARCHAR ( 50 )  NOT NULL PRIMARY KEY,
	status VARCHAR ( 50 )  NULL,
	date_debut VARCHAR ( 50 )  NOT NULL,
	date_fin VARCHAR ( 50 )   NULL,
	montant REAL,
	resultat REAL
	
);


INSERT into Calcul('12345','en_cours','11/10/2022,17:17:15','11/10/2022,17:17:30',214,524);


update calcul set status='termine' where guid=123456;