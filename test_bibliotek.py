import pandas as pd
import numpy as np

# Testowanie NumPy
tablica_numpy = np.array([1, 2, 3, 4, 5])
print("NumPy zainstalowany poprawnie.")
print("Utworzona tablica NumPy:", tablica_numpy)
print("-" * 20)

# Testowanie Pandas
dane = {'Kolumna_A': [10, 20, 30], 'Kolumna_B': [1, 2, 3]}
dataframe_pandas = pd.DataFrame(dane)
print("Pandas zainstalowany poprawnie.")
print("Utworzony DataFrame Pandas:")
print(dataframe_pandas)