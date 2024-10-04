Testar a API: Você pode usar o Postman ou o navegador para acessar os endpoints:

http://127.0.0.1:8000/api/patos/
http://127.0.0.1:8000/api/clientes/
http://127.0.0.1:8000/api/vendas/


Cadastro de Patos: Endpoint para cadastrar patos com detalhes como
nome e mãe.
POST


Cadastro de Clientes: Endpoint para cadastrar clientes, incluindo nome e
elegibilidade para desconto.
POST
http://127.0.0.1:8000/api/clientes/

Registro de Vendas: Endpoint para registrar vendas, aplicando descontos
conforme necessário e registrando a data da venda.
POST
http://127.0.0.1:8000/api/vendas/

Listagem de Patos Vendidos: Endpoint para obter uma lista de todos os
patos vendidos com detalhes da transação
POST
http://127.0.0.1:8000/api/vendas/

Geração de Relatórios: Endpoints para gerar e baixar relatórios em Excel
e PDF.
http://localhost:8000/api/reports/excel/
http://localhost:8000/api/reports/pdf/





-----------------------
subir o sistema
python manage.py runserver
http://127.0.0.1:8000/
