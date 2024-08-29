import pandas as pd

# DataFrame fornecido
df = pd.DataFrame({
    'Categoria': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Valor': [100, 150, 200, 50, 300, 400]
})

# Agrupar os dados pela coluna "Categoria" e calcular a média dos valores
media_por_categoria = df.groupby('Categoria')['Valor'].mean()

print("Média dos valores por categoria:")
print(media_por_categoria)
