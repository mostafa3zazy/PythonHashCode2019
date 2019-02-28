# filename = "a_example"
# filename = "b_lovely_landscapes"
# filename = "c_memorable_moments"
# filename = "d_pet_pictures"
filename = "e_shiny_selfies"
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

# Make slideshow
slideshow = []

# for p in photos:
#     slideshow.append([p])

for p in h_photos:
    slideshow.append([p])

for i in range(0, len(v_photos), 2):
    # print(i)
    slideshow.append([v_photos[i], v_photos[i+1]])



# Calc score
def get_tags(photos):
    tags = set()
    for photo in photos:
        for tag in photo['tags']:
            tags.add(tag)
    # print(tags)
    return tags

print("scores")
score = 0
for i in range(len(slideshow) - 1):
    tagsSlideA = get_tags(slideshow[i])
    tagsSlideB = get_tags(slideshow[i + 1])
    commonTags = tagsSlideA.intersection(tagsSlideB)
    # print("Tags slide A: ", tagsSlideA)
    # print("Tags slide B: ", tagsSlideB)
    # print("common: ", commonTags)
    # print("score: " + str(min(len(tagsSlideA), len(tagsSlideB), len(commonTags))))
    score += min(len(tagsSlideA), len(tagsSlideB), len(commonTags))
print("score: ", score)





# Output slideshow
file = open(outfile, 'w')
file.write(str(len(slideshow)) + "\n")
for photo in slideshow:
    for item in photo:
        file.write(str(item['i']) + " ")
    file.write("\n")
file.close()
