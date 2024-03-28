### # wptwBrasil

### 		Análise de Sentimento e Visualização de Dados das Piores Empresas para se 									Trabalhar em TI no Brasil

Este é um código Python que realiza análise de sentimento em um conjunto de dados contendo reclamações de trabalhadoras e trabalhadores, e posteriormente gera visualizações como nuvem de palavras e gráficos de barras das empresas mais reclamadas.

#### Pré-requisitos

- Python 3.x
- Bibliotecas Python: pandas, nltk, wordcloud, matplotlib

#### Instalação de Dependências

Antes de executar o código, certifique-se de instalar as dependências necessárias. Você pode fazer isso executando o seguinte comando no terminal:

```
pip install -r requirements.txt
```

#### Executando o Código

1. Clone o repositório ou baixe o arquivo `worst.csv`.
2. Execute o código Python fornecido neste repositório.

#### Descrição do Código

O código realiza as seguintes tarefas:

1. Carrega os dados de reclamações de um arquivo CSV (`worst.csv`).
2. Pré-processa o texto, removendo stopwords e pontuações, e converte todas as palavras para minúsculas.
3. Utiliza o módulo NLTK para realizar a análise de sentimento nas colunas "EMPRESA" e "MOTIVOS".
4. Gera uma nuvem de palavras das reclamações mais frequentes.
5. Conta a frequência das palavras nos motivos das reclamações.
6. Gera gráficos de barras das empresas mais reclamadas em lotes de 10.

### Autor

Este código foi desenvolvido por @AdalbertoBrant https://www.linkedin.com/in/ilha/

### Contribuições

Contribuições são bem-vindas! Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Referências

Esse projeto foi desenvolvido a partir dos dados encontrados no website [worstplacetowork.com.br]() desenvolvido pelo programador Anderson Weber https://www.linkedin.com/in/andersonweber/

### Licença

Este projeto está licenciado sob a MIT.
