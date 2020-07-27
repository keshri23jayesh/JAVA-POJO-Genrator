import os
from xmlconverter import list_directory
from construction_of_pojo import genration_of_class

xml_file_path = '/home/jayesh/Dev/Pojo/sample/some_xml_file.xml'
pojo_in_a_dict_form = list_directory(xml_file_path)
# print(pojo_in_a_dict_form)

genration_of_class.re_aranage_dict(pojo_in_a_dict_form)