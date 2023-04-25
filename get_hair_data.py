from simple_image_download import simple_image_download as simpd

response = simpd.simple_image_download

keywords = ["bald men with beard", "bald men without beard"]
# ["scruffy beard", "Goatee Beard", "Royale Beard", "Goatee without moustache", "Petite Goatee", 
#             "Van Dyke Beard", "Short Boxed Beard", "Balbo Beard", "stubble beard", "Mutton Chops Beard",
#             "Gunslinger Beard and Moustache", "Hipster Beard"  ]
#["men with beards", "men with facial hair"]

for kw in keywords:
    response().download(kw, 40)