# import yaml  # ggf. pip install pyyaml

# # Data Dictionary 
# config = {
# 'photo_dir': 'photos',
# 'data_dir': 'photo_info',
# 'extensions': ['jpg', 'jpeg'],
# }

# config_filename = 'config.yaml'
# writer = open(config_filename, 'w')
# yaml.dump(config, writer)
# writer.close()

# # readback = open(config_filename).read()
# # print(readback)

import yaml

with open("config.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

getyaml = data["data_dir"]  # liefert String
print("Ausgabe:", getyaml)

getyaml = data["extensions"]  # liefert Liste
print("Ausgabe:", getyaml)
print("Ausgabe:", getyaml[0])
print("Ausgabe:", getyaml[1])

getyaml = data["photo_dir"]  # liefert string
print("Ausgabe:", getyaml)

getyaml = data["value"]  # liefert float
print("Ausgabe:", getyaml)
