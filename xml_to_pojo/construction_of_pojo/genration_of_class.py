

method = {}


def re_aranage_dict(parsing_dict: dict):
    # print(parsing_dict)
    '''
        we will generate base method using the base flag in dict
    '''
    for key in parsing_dict:
        if 'base' in parsing_dict[key]:
            if 'have_text' in parsing_dict[key]:
                defining_the_base_method(key, parsing_dict[key][0])
            if 'dont_have_text' in parsing_dict[key]:
                defining_the_base_method_for_text(key, parsing_dict[key][0])
    print(method)

    '''
        TODO: we will generate not_base method using the not_base flag in dict
    '''
    for key in parsing_dict:
        if 'not_base' in parsing_dict[key]:
                defining_the_parent_methods(key, parsing_dict[key])


def defining_the_base_method_for_text(key, list_of_parms: list):
    function_str = "public static class " + key + " { \n\n"
    string_varible = "private String "+ key.lower() +";\n"
    getter_function_str = "@XmlValue\n"+"public String get"+key+"() {\n"+"return "+key.lower()+";\n}\n\n"
    setter_function_str = "public void set"+key+"(String "+key.lower()+") {\n"+"this."+key.lower()+" = "+key.lower()+";\n}\n\n"

    if len(list_of_parms) > 0:
        string_varible = ""
        for params in list_of_parms:
            string_varible += "private String "+ params.lower() +";\n"
        function_str += string_varible + "\n" + getter_function_str + setter_function_str + getter_for_a_string(list_of_parms) + "}"
    else:
        function_str += string_varible + "\n" + getter_function_str + setter_function_str + "}"
    print(function_str)
    print("\n")
    method[key] = function_str


def defining_the_base_method(key, list_of_parms: list):
    function_str = "public static class " + key + " { \n\n"
    if len(list_of_parms) > 0:
        string_varible = ""
        for params in list_of_parms:
            string_varible += "private String "+ params.lower() +";\n"
        function_str += string_varible + "\n" + getter_for_a_string(list_of_parms) + "}"
        method[key] = function_str


def defining_the_parent_methods(key, param):
    pass


def getter_for_a_string(list_of_parms):
    ans = ""
    for key in list_of_parms:
        getter_function_str = '@XmlAttribute(name="'+key+'")\n'+"public String get"+key+"() {\n"+"return "+key.lower()+";\n}\n\n"
        setter_function_str = "public void set"+key+"(String "+key.lower()+") {\n"+"this."+key.lower()+" = "+key.lower()+";\n}\n\n"
        ans += getter_function_str+setter_function_str
    return ans


def generate_getter_and_setter(key: str, list_of_parms: list):
    for val in list_of_parms:
        method[val] =[generate_getter(val),
                      generate_setter(val),
                      genrate_function_name(list_of_parms),
                      genrate_varible_name(val)]


def genrate_function_name(val):
    pass


def genrate_varible_name(val):
    return "private String" + val + ";"


def generate_getter(list_of_parms: list):
    # @XmlAttribute(name="Timestamp")
    # public String getTimestamp() {
    # return timestamp;
    # }
    # attribute_name = val[0].upper() + str[1:]
    # getter_method = "@XmlAttribute(name=\""+attribute_name+"\")\n"
    # getter_method += "public String get"+attribute_name+"() { return "+val.lower()+ "; }"
    # print(getter_method)
    pass


def generate_setter(val):
    pass
