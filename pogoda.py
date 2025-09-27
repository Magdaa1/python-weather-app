import matplotlib.pyplot as plt
import requests
import pandas as pd
import sys

# Zastąp 'TWÓJ_KLUCZ_API' kluczem wygenerowanym na OpenWeatherMap
API_KEY = "Twoj_klucz"
miasto = input("Dla jakiego miasta chcesz sprawdzic pogode? ")

# Wyczyść miasto, by usunąć potencjalne spacje i upewnić się, że jest poprawne w URL
miasto = miasto.strip()

if not miasto:
    print("Brak nazwy miasta. Program kończy działanie.")
    sys.exit()

# NOWY Adres URL do pobrania PROGNOZY
url = f"https://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={API_KEY}&units=metric"

# Wysyłanie zapytania i pobieranie odpowiedzi
odpowiedz = requests.get(url)

# Sprawdzenie, czy zapytanie się powiodło
if odpowiedz.status_code == 200:
    dane_json = odpowiedz.json()

    # Wydobycie interesujących nas danych
    pogoda = dane_json['weather'][0]['description']
    temperatura = dane_json['main']['temp']
    wilgotnosc = dane_json['main']['humidity']
    wiatr = dane_json['wind']['speed']

    # Stworzenie DataFrame z Pandas
    dane_ramka = pd.DataFrame({
        'Miasto': [miasto],
        'Temperatura': [temperatura],
        'Wilgotność (%)': [wilgotnosc],
        'Wiatr (m/s)': [wiatr],
        'Warunki': [pogoda]
    })

    print("\nPrezentacja danych w formie tabeli:")
    print(dane_ramka)

    # --- WIZUALIZACJA DANYCH(MATPLOTLIB) - --

    # Przygotowanie danych do wykresu
    etykiety = ['Temperatura (°C)', 'Wilgotność (%)']
    wartosci = [temperatura, wilgotnosc]

    # Tworzenie wykresu słupkowego
    plt.figure(figsize=(8, 6))  # Ustawienie rozmiaru okna wykresu

    # Stworzenie słupków
    wykres = plt.bar(etykiety, wartosci, color=['skyblue', 'lightcoral'])

    # Dodanie etykiet (wartości) na szczycie słupków
    for bar in wykres:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval,
                 round(yval, 1), ha='center', va='bottom', fontsize=12)

    # Dodanie tytułów i etykiet
    plt.title(f'Kluczowe Parametry Pogody dla {miasto}', fontsize=16)
    plt.ylabel('Wartość', fontsize=12)
    plt.ylim(0, max(wartosci) * 1.2)  # Ustawienie limitu osi Y

    # Wyświetlenie wykresu
    plt.show()

    # ----------------------------------------
    # Użyjemy nazwy miasta, aby nazwa pliku była unikalna
    nazwa_pliku = f"pogoda_{miasto.lower()}.csv"

    # 5. Zapis DataFrame do pliku CSV
    dane_ramka.to_csv(nazwa_pliku, index=False)

    print(f"\n✅ Dane dla {miasto} zapisano do pliku: {nazwa_pliku}")
   # -- print("Dane JSON pobrane poprawnie:")
# print(dane_json)
else:
    if odpowiedz.status_code == 404:
        print(f"Błąd: Miasto '{miasto}' nie zostało znalezione w bazie danych.")
        print("Sprawdź pisownię i spróbuj ponownie.")
    else:
        print("Wystąpił błąd podczas pobierania danych.")
        print(f"Kod błędu: {odpowiedz.status_code}")
