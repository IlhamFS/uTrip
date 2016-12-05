# made
# assume this is a main class
# ini file cuma buat coba2 fungsi aja

import settings
import sorting
import query

settings.init_build()

# testing query
result = query.get_query_result("Manado", ["Bridges"], 10, 12)
print(result)

# testing sorting
coba = {"Art Museums": [1319, 1348, 1377, 1406, 421, 1435, 1464, 1493], "Caverns & Caves": [421, 1309, 1338, 1367, 1396, 1425, 1454, 1483], "Other Fun & Games": [830, 908]}
hasil = sorting.sort_all(coba)
print (hasil)
