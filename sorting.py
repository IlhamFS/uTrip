# made
# HOW TO SORT? Berdasarkan bobot (W)
# W = Rating + Norm_Review + Norm_Feedback_Download

import operator
import settings

# input : selected categories (categories_dict format)
# output: sorted array (id_places) for all categories
def sort_all(categories):
    # sort each categories
    tmp_categories = []
    for key in categories:
        tmp_categories.append(sort_places(categories[key]))
    # print("=== CHECK HASIL PER KATEGORI ===")
    # print(tmp_categories)

    # take top 3 & sisa from each categories then sort
    top3_list = []
    sisa_list = []
    for i in range(len(tmp_categories)):
        top3_list.extend(tmp_categories[i][:3])
        sisa_list.extend(tmp_categories[i][3:])
    top3_list = sort_places(top3_list)
    sisa_list = sort_places(sisa_list)

    # merge all, must unique
    sorted_all = []
    for k in range(len(top3_list)):
        if top3_list[k] not in sorted_all:
            sorted_all.append(top3_list[k])
    for l in range(len(sisa_list)):
        if sisa_list[l] not in sorted_all:
            sorted_all.append(sisa_list[l]) 
    
    return sorted_all

# input : array of id_places
# output: sorted array (id_places) based on weight 
def sort_places(arr):
    weight_dict = {}
    for i in range(len(arr)):
        # create a map of id_place -> weight
        w = get_weight(settings.places[arr[i]]) # get a place 
        weight_dict[arr[i]] = w
    # sort by weight value
    sorted_dict = sorted(weight_dict.items(), key=operator.itemgetter(1), reverse=True)
    # check hasil sorting dan nilainya
    # print(sorted_dict)
    return [int(i[0]) for i in sorted_dict]

# input : a place
# output: weight of that place
def get_weight(place):
    rate = float(place["rate"])
    count_review = int(place["review"])
    download = 0.0
    if place.get("feedback"):
        download = place["feedback"]["download"]

    w = rate + (float(count_review) / settings.max_review) + (download / settings.max_download)
    return w
