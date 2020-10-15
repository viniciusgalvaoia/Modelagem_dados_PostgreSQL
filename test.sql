-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- Programa              : test.sql
-- Descricao             : Queries para verificar se as tabelas foram populadas corretamentes
--
-- Data        Tipo             Autor                                                               
-- -- -- --    --  --           -- --- -- -- -- -- -- -- -- -- -- --       
-- 15/10/2020  Criação          Vinícius Augusto Galvão da Silva                                      
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- Verificando se a tabela users foi populada corretamente

SELECT * 
FROM users
LIMIT 5;

-- Verificando se a tabela songs foi populada corretamente

SELECT * 
FROM songs
LIMIT 5;

-- Verificando se a tabela time foi populada corretamente

SELECT * 
FROM time
LIMIT 5;

-- Verificando se a tabela artists foi populada corretamente

SELECT * 
FROM artists
LIMIT 5;

-- Verificando se a tabela songplays foi populada corretamente

SELECT * 
FROM songplays
LIMIT 5;
