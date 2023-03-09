import re

pattern = r"[A-Z]yclone"
text = 'In meteorology, a Cyclone is a large air mass that rotates around a strong center of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The Cyclone low-pressure systems are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones and Dyclone cyclones also lie within the synoptic scale.[5] '


matches = re.search(pattern, text)    #give first occurence

matches= re.finditer(pattern, text)    #gives all matches
for match in matches:
    print(match)
