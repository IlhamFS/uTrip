# made
# assume this is a main class
# ini file cuma buat coba2 fungsi aja

import settings
import sorting
import feedback
import query

settings.init_build()

# testing umum
print len(settings.places)
# print settings.places[1269]

# testing niken
print settings.name_ids["Ayam Goreng President"]

# testing query
result = query.get_query_result("Jakarta", ["Shopping"], 10, 12)
print "YOLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
print(result)

# # testing sorting
coba = {"Art Museums": [421], "Caverns & Caves": [421], "Other Fun & Games": [830, 908]}
hasil = sorting.sort_all(coba)
print (hasil)

# testing feedback
downloads = [10,20,10]
feedback.update_downloads(downloads)
print settings.places[10]

# print settings.places[20]
print settings.cities_dict["Jakarta"]
print settings.places[380]
