import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Baixe os recursos necessários
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')

# Carregar o arquivo CSV
df = pd.read_csv('worst.csv')

# Pré-processamento de texto
stop_words = set(stopwords.words('portuguese'))

# Incluindo a lista de stop words fornecida
stop_words.update([
    "pra",
    "nada",
    "falta",
    "todo",
    "todos",
    "fazer",
    "dia",
    "nao",
    "lá",
    "mal",
    "vai",
    "vc",
    "além",
    "ter",
    "onde",
    "nunca",
    "sobre",
    "pois",
    "toda",
    "pro",
    "só",
    "horas",
    "assim",
    "qualquer",
    "porque",
    "sendo",
    "ainda",
    "sempre",
    "antes",
    "muitas",
    "menos",
    "fica",
    "semana",
    "vez",
    "enquanto",
    "outras",
    "anos",
    "sabem",
    "podia",
    "tipo",
    "deixa",
    "tempo",
    "mesmo",
    "sem",
    "talvez",
    "tudo",
    "tal",
    "cada",
    "então",
    "vez"
])

def preprocess_text(text):
    if pd.isnull(text):
        return ''
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(tokens)


# Aplicar a análise de sentimento
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    return score['compound']

# Aplicar pré-processamento e análise de sentimento nas colunas EMPRESA e MOTIVOS
df['EMPRESA_processed'] = df['EMPRESA'].apply(preprocess_text)
df['MOTIVOS_processed'] = df['MOTIVOS'].apply(preprocess_text)

df['EMPRESA_sentiment'] = df['EMPRESA_processed'].apply(analyze_sentiment)
df['MOTIVOS_sentiment'] = df['MOTIVOS_processed'].apply(analyze_sentiment)

# Contar a frequência das empresas e motivos
top_100_empresas = df['EMPRESA'].value_counts().head(100)
top_motivos = df['MOTIVOS'].value_counts().head(100)

# Gerar a nuvem de palavras para os motivos
motivos_text = ' '.join(df['MOTIVOS_processed'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(motivos_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Palavras Mais Frequentes')
plt.savefig('grafico/palavras_frequentes.png', dpi=300, bbox_inches='tight')
plt.show()

# Contar a frequência das palavras
word_freq = Counter(motivos_text.split())

# Ordenar as palavras por frequência (da mais frequente para a menos frequente)
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Escrever as palavras e suas frequências no arquivo de texto
with open('nuvempalavras.txt', 'w', encoding='utf-8') as f:
    for word, freq in sorted_word_freq:
        f.write(f'{word}: {freq}\n')

# Gerar o ranking das empresas com mais reclamações em lotes de 10
num_empresas = len(top_100_empresas)
num_batches = num_empresas // 10 + 1  # Número total de lotes

for batch_num in range(num_batches):
    start_idx = batch_num * 10
    end_idx = min((batch_num + 1) * 10, num_empresas)
    
    batch_empresas = top_100_empresas.iloc[start_idx:end_idx]
    
    if len(batch_empresas) == 0:
        continue  # Ignorar lotes vazios
    
    plt.figure(figsize=(10, 5))
    batch_empresas.plot(kind='bar')
    plt.title(f'Top 100 das Empresas mais Reclamadas (Rank {batch_num + 1} de {num_batches})')
    plt.xlabel('Empresa')
    plt.ylabel('Número de Reclamações')
    
    # Garantir que o diretório 'grafico' exista
    if not os.path.exists('grafico'):
        os.makedirs('grafico')
    
    # Salvar o gráfico como PNG no diretório 'grafico'
    plt.savefig(f'grafico/top_empresas_rank_{batch_num + 1}_of_{num_batches}.png', dpi=300, bbox_inches='tight')
    plt.close()
