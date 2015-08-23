__author__ = 'cupen'


def _(s):
    """
    >>> _("1+2")
    3
    >>> _("1+2+3")
    6
    >>> _("1+2+3-5")
    1
    >>> _("1+2+3-5-10")
    -9

    :param s:
    :return:
    """
    status = 0 # 0-start 1-digit1 2-digit1_end 3-digit2 4-digit2_end
    sum = ""
    num = ""
    flag = ''
    for c in s:
        if c.isdigit():
            if status == 0 or status == 1:
                sum += c
                status = 1
            elif status == 2 or status == 3:
                num += c
                status = 3
        else:
            if status == 1:
                sum = int(sum)
                status = 2
                flag = c

            elif status == 3:
                num = int(num)
                # print(sum,flag,num)
                if flag == '-':
                    sum -= num
                elif flag == '+':
                    sum += num
                flag = c
                num = ''
                status = 2
    if status == 3:
        if flag == '-':
            sum -= int(num)
        elif flag == '+':
            sum += int(num)

    return sum


from excel2sth import Excel, write_file

excelFile = 'test.xls'
excel = Excel(excelFile)

# 直接导出为json
excel.toJson(Excel.XX_TYPE_DICT, excelFile+".json")

# 导出为list json结构,并拼凑出代码
jsonText = "const test = {test}\n".format(test=excel.toJson(Excel.XX_TYPE_LIST))
write_file(excelFile + '.list.js', jsonText)

# 导出为dict json结构,并拼凑出代码
jsonText = "const test = {test}\n".format(test=excel.toJson(Excel.XX_TYPE_DICT))
write_file(excelFile + '.dict.js', jsonText)

# 预处理一遍再导出为json,并拼凑出代码
def _callback(data):
    data['a'] = 1
    data['b'] = 2
    data['c'] = 3
    data['d'] = 4
    return data

excel.beforeToJson(_callback)
jsonText = "const test = {test}\n".format(test=excel.toJson(Excel.XX_TYPE_DICT))
write_file(excelFile + '.dict.pre.js', jsonText)
