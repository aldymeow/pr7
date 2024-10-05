def perevod(dec):

  if dec == 0:
    return "0"

  def septt(n):
    if n == 0:
      return []
    else:
      return septt(n // 7) + [str(n % 7)]

  # Получаем список цифр семиричного числа
  sept_d = septt(dec)

  # Соединяем цифры в строку
  sept_n = "".join(sept_d)

  return sept_n

print ('Введите число в 10ой СС больше нуля, которое нужно перевести в 7ую:')
dec = int(input())
sept_n = perevod(dec)
print(f"Число в 7ой СС: {sept_n}")