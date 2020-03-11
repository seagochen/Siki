# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Created: May 31, 2018
# LastChg: Mar 11, 2020

from siki.basics.Exceptions import InvalidParamException

def binary_to_string(binary):
    """
    this function will convert a binary data to string
    """
    return binary.decode("UTF8")




def string_to_binary(strdata):
    """
    this function will convert a string data to binary
    """
    return strdata.encode("UTF8")




def dict_to_string(dictionary):
    """
    this function will convert a dict type to string
    """
    import json

    if type(dictionary) is dict:
        return json.dumps(dictionary)
    else:
        raise InvalidParamException("input type is not a correct dictionary type")




def string_to_dict(strdata):
    """
    this function will convert a string data to dict type
    """
    import json

    if type(strdata) is str:
        return json.loads(strdata)
    else:
        raise InvalidParamException("input type is not a correct string type")




def dict_to_binary(dictionary):
    """
    this function will convert a dictionary to binary type
    """
    strdata = dict_to_string(dictionary)
    return string_to_binary(strdata)




def binary_to_dict(binary):
    """
    this function wil convert a binary to dictionary
    """
    strdata = binary_to_string(binary)
    return string_to_dict(strdata)




def list_to_string(listdata, sep=","):
    """
    this function will convert a list to string
    """
    if type(listdata) is list:
        # using list comprehension 
        return "[" + sep.join([str(elem) for elem in listdata]) + "]"
    else:
        raise InvalidParamException("input type is not a correct list type")




def string_to_list(strdata, sep=","):
    """
    this function will convert a string to list
    """
    if type(strdata) is str:
        return strdata.strip('][').split(sep)
    else:
        raise InvalidParamException("input type is not a correct string type")




def list_to_binary(listdata, sep=","):
    """
    this function will convert a list to binary
    """
    strdata = list_to_string(listdata, sep)
    return string_to_binary(strdata)




def binary_to_list(binary, sep=","):
    """
    this function will convert binary to list
    """
    strdata = binary_to_string(binary)
    return string_to_list(strdata, sep)




def datetime_to_str(date = None, format = "%Y-%m-%d %H:%M:%S"):
    """
    this method will convert the datetime into string with the format YYYY-mm-dd HH:MM:SS

    @Args:
    * [date] datetime.datetime, without any input the returning will be the current timestamp
    * [format] str, the format of output string
    
    @Returns:
    * [str] formatted string of timestamp
    """
    from datetime import datetime

    if date is None:
        date = datetime.now()

    if type(date) is not datetime:
        return "1970-01-01 00:00:00" # 错误的数据格式，用1970作为默认的时间返回，方便后台进行错误检查

    return date.strftime(format)


def str_to_datetime(date: str, format = "%Y-%m-%d %H:%M:%S"):
    """
    Convert string back to datetime

    @Args:
    * [date] str, the input string in some date format
    * [format] str, default is YYYY-mm-dd HH:MM:SS

    @Returns:
    * [datetime] returning is a datetime type
    """
    from datetime import datetime

    if date is not None:
        return datetime.strptime(date, format)
    else:
        return datetime.strptime("1970-01-01 00:00:00", format)




if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    test_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

    str1 = list_to_string(test_list)
    print("list_to_string", str1)

    raw1 = list_to_binary(test_list)
    print("list_to_binary", raw1)

    rest_list1 = string_to_list(str1)
    print("string_to_list", rest_list1)

    rest_list2 = binary_to_list(raw1)
    print("binary_to_list", rest_list2)

    str2 = dict_to_string(test_dict)
    print("dict_to_string", str2)

    raw2 = dict_to_binary(test_dict)
    print("dict_to_binary", raw2)

    rest_dict1 = string_to_dict(str2)
    print("string_to_dict", rest_dict1)

    rest_dict2 = binary_to_dict(raw2)
    print("binary_to_dict", rest_dict2)
