# Automação de Cadastro de Produtos com PyAutoGUI e Pandas

Este projeto é uma automação para realizar o cadastro de produtos em um sistema web utilizando a biblioteca **PyAutoGUI** para interação com a interface do usuário e **Pandas** para manipulação de dados. A automação segue um fluxo pré-definido para importar os dados de um arquivo CSV e cadastrar cada produto no sistema.

---

## 🛠️ Funcionalidades

1. **Abertura do navegador e acesso ao sistema**: A automação abre o navegador Microsoft Edge e acessa o sistema através do link fornecido.
2. **Login automatizado**: Realiza login utilizando as credenciais configuradas no código.
3. **Importação da base de dados**: Lê um arquivo CSV contendo informações dos produtos a serem cadastrados.
4. **Cadastro de produtos**: Itera pelos produtos na base de dados, preenchendo os campos no sistema e enviando os dados.
5. **Execução em lote**: Repete o processo até cadastrar todos os produtos da base.

---

## 📋 Pré-requisitos

- **Python 3.8+**
- Bibliotecas Python necessárias:
  - `pyautogui`
  - `pandas`
- Arquivo CSV contendo os produtos no seguinte formato:
  ```
  codigo,marca,tipo,categoria,preco_unitario,custo,obs
  001,MarcaX,Eletrônico,CategoriaA,100.00,80.00,Promoção
  002,MarcaY,Doméstico,CategoriaB,50.00,40.00,Nan
  ```
- O navegador Microsoft Edge deve estar instalado e configurado no sistema.

---

## 🚀 Como Executar

1. **Clonar o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <PASTA_DO_PROJETO>
   ```

2. **Instalar as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar a base de dados**:
   - Salve o arquivo `produtos.csv` na localização especificada no código: `C:/Users/Tiago/Documents/PROJETOS/Automação Python/produtos.csv`.

4. **Executar o script**:
   ```bash
   python automacao_cadastro.py
   ```

---

## 📝 Fluxo de Operação

1. O script abre o navegador e acessa o sistema no link:  
   `https://dlp.hashtagtreinamentos.com/python/intensivao/login`.
2. Realiza login com as credenciais configuradas no código.
3. Lê o arquivo `produtos.csv` e exibe o conteúdo no console para verificação.
4. Itera sobre as linhas da tabela e preenche os campos do formulário no sistema.
5. Envia os dados de cada produto e passa para o próximo até finalizar.

---

## ⚠️ Observações

- **Segurança**: Certifique-se de substituir as credenciais de login por variáveis de ambiente ou métodos seguros antes de uso em produção.
- **Coordenadas no PyAutoGUI**: As coordenadas para cliques (`x`, `y`) podem variar dependendo da resolução e do layout do sistema. Ajuste conforme necessário.
- **Erro de campos vazios**: Certifique-se de que a base de dados não contém informações inválidas para evitar falhas no preenchimento dos campos.

---

## 📄 Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---
