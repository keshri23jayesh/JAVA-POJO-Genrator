import os
import xml.etree.ElementTree as ET
from collections import Counter

final_dict = {}


def list_directory(path):
    my_tree = ET.parse(path)
    file_root = my_tree.getroot()
    root_key = file_root.tag
    # print(type(file_root))
    # print(file_root.getchildren())
    # parsing_dict = {file_root.tag: [get_list(file_root.attrib), [child.tag for child in file_root]]}
    parsing_dict = {file_root.tag: [get_list(file_root.attrib), child_with_counts(file_root), False]}
    dict_res = recursive_parsing(parsing_dict, root_key, file_root)
    for key in dict_res:
        if len(dict_res[key][1]) == 0:
            dict_res[key].append('base')
        else:
            dict_res[key].append('not_base')
    return dict_res


def recursive_parsing(parsing_dict: dict, key: str, file_root):
    child_dict = parsing_dict[key][1].copy()
    for item in child_dict:
        for element in file_root.iter(item):
            if item in parsing_dict:
                parsing_dict[item][0].extend(get_list(element.attrib))
                to_set = list(set(parsing_dict[item][0]))
                parsing_dict[item][0] = to_set
                new_child_dict = merge_two_dict(element, parsing_dict[item][1])
                second_time_processed = diff_of_two_list(get_list(new_child_dict), get_list(parsing_dict[item][1]))
                parsing_dict[item][1] = new_child_dict
                if len(second_time_processed) > 0:
                    recursive_parsing(parsing_dict, item, file_root)
                    # for new_tag in second_time_processed:
                        # parsing_dict[new_tag] = [[], {}]
                        # parsing_dict[new_tag].append('have_text' if "\n" in str(element.text) else 'dont_have_text')
                        # recursive_parsing(parsing_dict, item, file_root)
            else:
                parsing_dict[item] = [get_list(element.attrib), child_with_counts(element)]
                # true or false flag for xml has text or not
                parsing_dict[item].append('have_text' if "\n" in str(element.text) else 'dont_have_text')
                recursive_parsing(parsing_dict, item, file_root)
    return parsing_dict

# old version
# def recursive_parsing(parsing_dict: dict, key: str, file_root):
#     child_dict = parsing_dict[key][1].copy()
#     for item in child_dict:
#         for element in file_root.iter(item):
#             if item in parsing_dict:
#                 parsing_dict[item][0].extend(get_list(element.attrib))
#                 to_set = list(set(parsing_dict[item][0]))
#                 parsing_dict[item][0] = to_set
#                 new_child_dict = merge_two_dict(element, parsing_dict[item][1])
#                 parsing_dict[item][1] = new_child_dict
#             else:
#                 parsing_dict[item] = [get_list(element.attrib), child_with_counts(element)]
#                 # true or false flag for xml has text or not
#                 parsing_dict[item].append('have_text' if "\n" in str(element.text) else 'dont_have_text')
#                 recursive_parsing(parsing_dict, item, file_root)
#     return parsing_dict

def diff_of_two_list(li1, li2):
    if len(li1) == 0:
        return li1
    else:
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif


def get_the_list(element: dict):
    dict1 = dict(Counter([child.tag for child in element]))
    list_of_keys = get_list(dict1)
    return list_of_keys


def child_with_counts(file_root):
    # print(file_root)
    # for child in file_root:
    #     print(child)
    return dict(Counter([child.tag for child in file_root]))


def merge_two_dict(file_root, dict2):
    dict1 = dict(Counter([child.tag for child in file_root]))
    for key in dict2:
        if key in dict1:
            dict1[key] = max(dict1[key], dict2[key])
        else:
            dict1[key] = dict2[key]
    return dict1


def get_list(dict_for_list):
    list2 = list(set(dict_for_list.keys()))
    return list2


def union_of_list(lst1: [], lst2: []):
    final_list = lst1 + lst2
    return final_list
