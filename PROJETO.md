# API PBE-VEICULAR

## OBJETIVO DO PROJETO:

Disponibilizar de forma democrática os dados de todos os veículos, de todos os anos que já foram homologados no Brasil. Tendo como informações relevantes de emissões, caracteristicas do veículo e organizados por montadora.

## Requisitos:

- API com Django Rest Framework
- Métodos HTTP permitidos: somente GET. 
- Endpoints:
    * Listar todos os veiculos por ano
    * Listar todos os veiculos por montadora
    * Fazer filtros
    * Exportar para CSV ou XLSX
- Métodos HTTP p/ administradores: GET, POST, UPDATE e DELETE.
- Banco de dados Postgres
- Pytest - testar todos endpoints
- Documento Swagger
- Docker
- Github CI/CD
- Publicar no Heroku
