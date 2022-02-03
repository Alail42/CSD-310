
DROP USER IF EXISTS 'pysports_user'@'localhost';



CREATE USER 'Batmin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Admin123';


GRANT ALL PRIVILEGES ON pysports.* TO'Batmin'@'localhost';


DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;



CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);



INSERT INTO team(team_name, mascot)
    VALUES('Team Bat Inc', 'Bat');

INSERT INTO team(team_name, mascot)
    VALUES('Team Villans', 'Chaos');


INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Bruce', 'Wayne', (SELECT team_id FROM team WHERE team_name = 'Team Bat Inc'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Richard', 'Grayson', (SELECT team_id FROM team WHERE team_name = 'Team Bat Inc'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Jason', 'Todd', (SELECT team_id FROM team WHERE team_name = 'Team Bat Inc'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('The', 'Joker', (SELECT team_id FROM team WHERE team_name = 'Team Villans'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Edward', 'Nygma', (SELECT team_id FROM team WHERE team_name = 'Team Villans'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Vitor', 'Frost', (SELECT team_id FROM team WHERE team_name = 'Team Villans'));
