import json


# json转换为包含元祖的列表
def get_json_data(file_path):
    """
    将json格式转为字典-元组格式对象
    @param file_path:
    @return:
    """
    data = []
    try:
        with(open(file_path, "r")) as f:
            dict_data = json.loads(f.read())
            for i in dict_data:
                data.append(tuple(i.values()))
        return data
    except BaseException as be:
        print(be)
