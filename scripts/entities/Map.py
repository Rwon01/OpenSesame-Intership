import pandas as pd

map = pd.read_excel("map/tiles.xlsx")
map_data = map.to_numpy().tolist()

