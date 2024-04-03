from library_item import LibraryItem

def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None

def get_key_from_name(input_name):
    """
    The function returns ... according to ...

    Sample:
        input: "Tom and Jerry"
        output: "01"
    """
    for key in library:
        item = library[key]
        if item.name == input_name:
            return key

video1 = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
video2 = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)

library = {}
library["01"] = video1
library["02"] = video2

input_name = "Tom and Jerry"
output_key = get_key_from_name(input_name)
# print(output_key)

output_director = get_director(key=output_key) # "Tom and Jerry"
print(output_director)