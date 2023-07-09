price_skumriq_kg = float(input())
price_caca_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

price_palamud_kg = price_skumriq_kg + (price_skumriq_kg * 0.6)
price_safrid_kg = price_caca_kg + (price_caca_kg * 0.8)
price_midi_kg = 7.50

palamud = palamud_kg * price_palamud_kg
safrid = safrid_kg * price_safrid_kg
midi = midi_kg * price_midi_kg

final_price = palamud + safrid + midi

print('{:0.2f}'.format(final_price))
