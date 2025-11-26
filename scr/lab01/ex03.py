price = input("")
discount = input("")
vat = input("")
base = int(price) * (1 - int(discount) / 100)
vat_amount = base * (int(vat) / 100)
total = base + vat_amount
print(
    f"База после скидки: {base:.2f}.",
    f"НДС: {vat_amount:.2f}.",
    f"Итого к оплате: {total:.2f}.",
    sep="\n",
)
