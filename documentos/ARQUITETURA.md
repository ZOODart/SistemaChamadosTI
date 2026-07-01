# Arquitetura do Sistema de Chamados TI

## Objetivo

Criar um sistema para Windows destinado ao gerenciamento de chamados tecnicos em instituiçao
de ensino
O sistema devera registrar historicos, controlar pendencias, gerar relatorios gerenciais 
e permitir a personalizaçao de cada colegio.

-----

# Fluxo Geral

Administrador criara usuarios e colegios

usuario faz login

seleciona o colegio que deseja atender

dashboard

a partir desse momento todas as operaçoes pertencem ao colegio selecionado

criar chamado
editar chamado
finalizar chamado
consultar historico
pesquisar soluçoes
gerar relatorios
configuraçoes

---

# Tipos de Usuarios

## Administrador

pode: 

- Criar usuarios
- Desativar usuarios
- Criar colegios
- Desativar colegios
- Alterar categorias
- Alterar tipos
- Restaurar backups
- Alterar configuraçoes globais

Existe apenas um administradir principal.

Nunca podera ser excluido

---

## Tecnico

Pode:
- Abrir chamados
- Finalizar chamados
- Editar chamados proprios
- Consultar historico
- Pesquisar soluçoes
- Visualizar calendario
- Gerar relatorios

---

# Estrutura do Sistema

main.py

Responsável por iniciar o sistema e coordenar os módulos.

---

banco/

Responsável pela comunicação com o SQLite.

database.py

---

interface/

login.py

dashboard.py

chamados.py

relatorios.py

configuracoes.py

---

modelos/

usuario.py

colegio.py

categoria.py

tipo.py

chamado.py

anexo.py

---

utilitarios/

backup.py

pesquisa.py

exportar.py

calendario.py

---

anexos/

Armazena imagens e PDFs.

---

relatorios/

Arquivos exportados.

---

# Banco de Dados

usuarios

colegios

usuario_colegio

categorias

tipos

chamados

anexos

---

# Funcionamento

Após o login, o usuário escolhe um colégio.

O sistema passa a trabalhar utilizando esse colégio como contexto.

Todas as categorias, tipos, chamados, calendário e tema visual pertencem ao colégio
 atualmente selecionado, fora os relatorios, que voce pode selecionar qual colegio voce 
 quer visualizar e exportar.

---

# Registro

Possui:

Categoria

Tipo

Descrição do problema

Descrição da solução

Prioridade

Data

Anexos

Técnico

Colégio

---

# Lembrete

Possui:

Categoria

Tipo

Descrição do problema

Prioridade

Data de abertura

Prazo

Status

Quando finalizado:

Descrição da solução

Anexos

Data de finalização

---

# Pesquisa

Pesquisar por:

Categoria

Tipo

Descrição do problema

Descrição da solução

Prioridade

Técnico

Colégio

Período

---

# Dashboard

Mostrar:

Pendentes do dia

Pendentes da semana

Atividades recorrentes

Avisos

Calendário

Acesso rápido para Novo Chamado

---

# Relatórios

Indicadores por:

Técnico

Colégio

Categoria

Tipo

Prioridade

Período

Tempo médio de resolução

Quantidade de chamados

Exportação:

PDF

Excel

CSV

---

# Objetivo Final

Ser um sistema intuitivo, rápido, organizado e escalável para gestão de chamados técnicos 
em escolas.


# Princípios do Projeto

- Interface simples e intuitiva.
- O técnico deve preencher o mínimo possível.
- Nenhuma informação deve ser duplicada.
- Todas as ações importantes devem ser registradas.
- Dados nunca são apagados; apenas desativados quando necessário.
- O sistema deve ser rápido mesmo com muitos chamados.
- Cada módulo deve ter apenas uma responsabilidade.
- O banco de dados deve ser normalizado e preparado para expansão.