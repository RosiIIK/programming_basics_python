bitcoins = int(input())
chinese_iuana = float(input())
comision = float(input()) # % tax

bitcoin_price = 1168
dollar_price = 1.76
chinese_iuana_price = dollar_price * 0.15
euro_price = 1.95

total_lv = (bitcoin_price * bitcoins) + (chinese_iuana_price * chinese_iuana)
total_euro = total_lv / 1.95
total_comision = (total_euro * comision) / 100

final_price = total_euro - total_comision
print(f"{final_price:.2f}")
