site_side_length = int(input())
tile_width = float(input())
tile_length = float(input())
bench_width = int(input())
bench_length = int(input())

site_area = site_side_length * site_side_length
tile_area = tile_width * tile_length
bench_area = bench_width * bench_length

tile_placing_time = 0.2

site_area_without_bench = site_area - bench_area
tiles_number = site_area_without_bench / tile_area
work_time = tiles_number * tile_placing_time

print(tiles_number)
print(work_time)
