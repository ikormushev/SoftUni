wanted_compote_jars = int(input())
wanted_jam_jars = int(input())

cherries_needed_compote = (wanted_compote_jars + 1) * 0.300
cherries_needed_jam = (wanted_jam_jars + 1) * 0.650

cherries_needed_compote *= 1.05  # including losses
cherries_needed_jam *= 1.10  # including losses

cherries_kg = cherries_needed_compote + cherries_needed_jam
cherries_kg *= 3.20

print(f"{cherries_kg:.2f}")
