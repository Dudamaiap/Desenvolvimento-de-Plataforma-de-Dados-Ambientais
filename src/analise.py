import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('data/dados_pantanal.csv')

df['data'] = pd.to_datetime(df['data'])

# Tratamento dos valores ausentes 
df['nivel_rio_m'] = df['nivel_rio_m'].interpolate()
df['ndvi'] = df['ndvi'].interpolate()

df.to_csv('data/dados_pantanal_limpo.csv', index=False)

# Cálculo de média 
media_temp = df['temperatura_c'].mean()
media_nivel = df['nivel_rio_m'].mean()
media_ndvi = df['ndvi'].mean()

print("Médias:")
print(f"Temperatura: {media_temp:.2f}")
print(f"Nível do rio: {media_nivel:.2f}")
print(f"NDVI: {media_ndvi:.2f}")

#Gráfico de temperatura 
plt.figure()
plt.plot(df['data'], df['temperatura_c'])
plt.title('Temperatura ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig('outputs/grafico_temperatura.png')
plt.close()

# Gráfico de nível do rio
plt.figure()
plt.plot(df['data'], df['ndvi'])
plt.title('NDVI ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('NDVI')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig('outputs/grafico_ndvi.png')
plt.close()

# nível do rio 
plt.figure()
plt.plot(df['data'], df['nivel_rio_m'])
plt.title('Nível do Rio ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('Nível do Rio (m)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig('outputs/grafico_nivel_rio.png')
plt.close()

#Relação temperatura e NDVI
plt.figure()
plt.scatter(df['temperatura_c'], df['ndvi'])
plt.title('Relação entre Temperatura e NDVI')
plt.xlabel('Temperatura (°C)')
plt.ylabel('NDVI')
plt.grid()
plt.tight_layout()
plt.savefig('outputs/grafico_temp_vs_ndvi.png')
plt.close()

# Relação nível do rio e NDVI
plt.figure()
plt.scatter(df['nivel_rio_m'], df['ndvi'])
plt.title('Relação entre Nível do Rio e NDVI')
plt.xlabel('Nível do Rio (m)')
plt.ylabel('NDVI')
plt.grid()
plt.tight_layout()
plt.savefig('outputs/grafico_rio_vs_ndvi.png')
plt.close()