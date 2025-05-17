# ADM Carros Python Edition 🐍🚗

![Python Version](https://img.shields.io/badge/python-3.13.3-blue)
![GitHub repo size](https://img.shields.io/github/repo-size/augustojbe/adm-carros)
![License](https://img.shields.io/github/license/augustojbe/adm-carros)

Sistema de gerenciamento de veículos reescrito em Python 3.13.3 com interface moderna e banco de dados relacional.

## 🌟 Recursos Principais

- ✅ Cadastro completo de veículos (marca, modelo, ano, placa, etc.)
- 🔍 Pesquisa avançada com filtros combináveis
- ✏️ Edição e exclusão de registros
- 📊 Dashboard com métricas básicas
- 🖥️ Interface gráfica moderna

## � Stack Tecnológica

- **Linguagem**: Python 3.13.3
- **Banco de Dados**: PostgreSQL
- **ORM**: SQLAlchemy 2.0
- **Dependências**: Gerenciadas por Poetry
- **Testes**: pytest
- **Relatórios**: FPDF ou ReportLab

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/augustojbe/adm-carros-python.git
   cd adm-carros-python
2. Configure o ambiente virtual (recomendado):
  python -m venv venv
  source venv/bin/activate  -> Linux/Mac
  ou venv\Scripts\activate no Windows
3. Instale as dependências:
  pip install -r requirements.txt

## 🗃️ Estrutura do Projeto

adm-carros-python/
├── src/
│   ├── models/          # Classes de domínio
│   ├── views/           # Interface gráfica
│   ├── controllers/     # Lógica de negócio
│   ├── database/        # Configuração do banco
│   ├── utils/           # Helpers e validadores
│   └── main_window.py   # Ponto de entrada
├── tests/               # Testes unitários
├── requirements.txt     # Dependências
├── pyproject.toml       # Configuração Poetry
└── README.md

## 🤝 Como Contribuir
 - Faça um fork do projeto

 - Crie uma branch (git checkout -b feature/nova-funcionalidade)

 - Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')

 - Push para a branch (git push origin feature/nova-funcionalidade)

 - Abra um Pull Request

## ✉️ Contato
 - Desenvolvedor: Augusto Alves
 - Email: augustojbe@gmail.com
 - Repositório: github.com/augustojbe/adm-carros-python


