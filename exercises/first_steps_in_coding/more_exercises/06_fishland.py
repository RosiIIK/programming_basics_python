skumria_price_per_kilo = float(input())
caca_price_per_kilo = float(input())
palamud_kilo = float(input())
safrid_kilo = float(input())
total_quantity_midi = int(input())
midi_price_per_kilo = 7.50
palamud_price_per_kilo = skumria_price_per_kilo + skumria_price_per_kilo * 0.6
total_price_palamud = palamud_kilo * palamud_price_per_kilo
safrid_price_per_kilo = caca_price_per_kilo + caca_price_per_kilo * 0.8
total_price_safrid = safrid_price_per_kilo * safrid_kilo
total_price_midi = total_quantity_midi * midi_price_per_kilo
total_sum = total_price_palamud + total_price_safrid + total_price_midi
print(f"{total_sum:.2f}")
