# filename = "a_example"
filename = "b_lovely_landscapes"
# filename = "c_memorable_moments"
# filename = "d_pet_pictures"
# filename = "e_shiny_selfies"
infile = "%s.txt" % filename
outfile = "%s_output.txt" % filename

# Read file
file = open(infile, 'r')
num_photos = int(file.readline())
photos = []
h_photos = []
v_photos = []
for item in range(num_photos):
    line = file.readline().split()
    p = {}
    p['i'] = item
    p['orient'] = line[0]
    p['tags'] = []
    for tag in line[2:]:
        p['tags'].append(tag)
    photos.append(p)
    if p['orient'] == 'H':
        h_photos.append(p)
    else:
        v_photos.append(p)
file.close()
# print(photos)

slides = []
# slides.extend(h_photos)
for p in h_photos:
    slides.append([p])
for i in range(0, len(v_photos), 2):
    # print(i)
    slides.append([v_photos[i], v_photos[i+1]])

def get_tags(photos):
    tags = set()
    for photo in photos:
        for tag in photo['tags']:
            tags.add(tag)
    # print(tags)
    return tags

def get_score(slideA, slideB):
    tagsSlideA = get_tags(slideA)
    tagsSlideB = get_tags(slideB)
    commonTags = tagsSlideA.intersection(tagsSlideB)
    # print("Tags slide A: ", tagsSlideA)
    # print("Tags slide B: ", tagsSlideB)
    # print("common: ", commonTags)
    # print("score: " + str(min(len(tagsSlideA), len(tagsSlideB), len(commonTags))))
    return min(len(tagsSlideA), len(tagsSlideB), len(commonTags))

# Make slideshow
slideshow = []

# for p in photos:
#     slideshow.append([p])

# for p in h_photos:
#     slideshow.append([p])
#
# for i in range(0, len(v_photos), 2):
#     # print(i)
#     slideshow.append([v_photos[i], v_photos[i+1]])

# Always make the first potential slide the first in slideshow
slideshow.append(slides[0])
del slides[0]

# Add each of the remaining slides (in some order)
total_potential_slides = len(slides)
for i in range(total_potential_slides):
    firstSlide = slideshow[i]
    lowest_score = 100000000000000
    lowest_item = -1
    for j in range(len(slides)):
        score = get_score(firstSlide, slides[j])
        if score != 0:
            if score < lowest_score:
                # print("found lower", j, score, slides[j])
                lowest_score = score
                lowest_item = j
            # else:
            #     print("not lower:", j)
    # print('lowest: ', lowest_item)
    print(str(i) + ",", end="")

    slideshow.append(slides[lowest_item])
    del slides[lowest_item]




# Calc score
print("scores")
print("length slideshow", len(slideshow))
score = 0
for i in range(len(slideshow) - 1):
    score += get_score(slideshow[i], slideshow[i + 1])
print("score: ", score)





# Output slideshow
file = open(outfile, 'w')
file.write(str(len(slideshow)) + "\n")
for photo in slideshow:
    for item in photo:
        file.write(str(item['i']) + " ")
    file.write("\n")
file.close()
