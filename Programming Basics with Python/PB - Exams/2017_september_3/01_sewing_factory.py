num_tables = int(input())
table_length = float(input())
table_width = float(input())

tablecloth_hanging_out_of_table_m = 0.30
cover_side = table_length / 2

price_tablecloth_m = 7
price_cover_m = 9
exchange_usd_bgn = 1.85

tablecloths_area = num_tables * (table_length + 2 * tablecloth_hanging_out_of_table_m) * \
                   (table_width + 2 * tablecloth_hanging_out_of_table_m)
covers_area = num_tables * cover_side * cover_side

final_price_usd = tablecloths_area * price_tablecloth_m + covers_area * price_cover_m
final_price_bgn = final_price_usd * exchange_usd_bgn

print(f"{final_price_usd:.2f} USD")
print(f"{final_price_bgn:.2f} BGN")
