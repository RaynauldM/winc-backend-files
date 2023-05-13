__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile


# step 1


def clean_cache():
    path = "./cache"
    if os.path.exists(path):
        if os.listdir(path):
            for kid in os.listdir(path):
                os.remove(os.path.join(path, kid))
    else:
        os.mkdir(path)


# step 2


def cache_zip(zip_path, cache_path):
    clean_cache()
    with zipfile.ZipFile(zip_path) as zip:
        zip.extractall(cache_path)


# step 3


def cached_files():
    return_list = []
    abs_path = os.path.abspath("./cache")
    for item in os.listdir("./cache"):
        return_list.append(os.path.join(abs_path, item))
    return return_list


# step 4


def find_password(cached_files):
    return_string = "nothing found"
    for item in cached_files:
        f = open(item)

        for item in f:
            if "password" in item:
                return_list = item.split("password: ")
                for char in return_list:
                    if char == "\\":
                        return_list.remove(char)

                new_string = "".join(return_list)
                return_string = new_string
        return_string = return_string.replace("\n", "")
    return return_string.strip()
