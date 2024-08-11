import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def exchange():
    code = entry.get()

    if code:
        try:
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ripple,solana,tether,tron,cardano,dai,kaspa,pepe,litecoin&vs_currencies=usd')
            response.raise_for_status()
            data = response.json()
            if code in data:
                exchange_rate = data[code]
                mb.showinfo("Курс обмена криптовалюты", f"Курс: {exchange_rate} {code} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"криптовалюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка",f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!","Введите криптовалюту")


window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("360x300")

Label(text="Введите код криптовалюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
