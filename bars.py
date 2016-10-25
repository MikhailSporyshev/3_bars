import json

def load_data(filepath):

	return json.load(open(filepath))


def get_biggest_bar(data):
	idx = 0;
	max_sits = int(data[0]["Cells"]["SeatsCount"])
	for i in range(1,len(data)):
		cur_sits = int(data[i]["Cells"]["SeatsCount"])
		if cur_sits > max_sits:
			max_sits = cur_sits
			idx = i
	return idx

def get_smallest_bar(data):
	idx = 0;
	min_sits = int(data[0]["Cells"]["SeatsCount"])
	for i in range(1,len(data)):
		cur_sits = int(data[i]["Cells"]["SeatsCount"])
		if cur_sits < min_sits:
			min_sits = cur_sits
			idx = i
	return idx

def get_closest_bar(data, longitude, latitude):
    idx = 0
    min_lon = float(data[0]["Cells"]["geoData"]["coordinates"][0])
    min_lat = float(data[0]["Cells"]["geoData"]["coordinates"][1])
    min_sq_dist = (min_lon- longitude)** 2 + (min_lat- latitude)** 2  
    for i in range(1,len(data)) :
    	cur_lon = float(data[i]["Cells"]["geoData"]["coordinates"][0])
    	cur_lat = float(data[i]["Cells"]["geoData"]["coordinates"][1])
    	cur_sq_dist = (cur_lon- longitude)** 2 + (cur_lat- latitude)** 2
    	if cur_sq_dist < min_sq_dist:
    		min_sq_dist = cur_sq_dist
    		idx = i
    return idx

if __name__ == '__main__':
    print("input filepath:")
    data = load_data(input())
    print("input longitude:")
    longitude = float(input())
    print("input latitude:")
    latitude = float(input())

    max_idx = get_biggest_bar(data)
    min_idx = get_smallest_bar(data)
    proxi_idx = get_closest_bar(data,longitude,latitude)
    print(max_idx, min_idx, proxi_idx)