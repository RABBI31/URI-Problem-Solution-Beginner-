days_number = int(input())
years = int(days_number/365)
reminDays = int(days_number%365)

months = int(reminDays/30)
reminday = int(reminDays%30)
print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{reminday} dia(s)')
