import debug
def sanitize(time_string):
    splitter = '.'
    if ':' in time_string:
        splitter = ':'
    elif '-' in time_string:
        splitter = '-'
    (min, secs) = time_string.split(splitter)
    return min + '.' + secs
    
def get_coach_data(file_name):
    try:
        with open("james.txt") as james_file:
            data = james_file.readline()
            data_list = data.strip().split(',')
        return data_list
    except IOError as err:
        print("File Error: " + str(err))
        return (None)

print(sorted(set([sanitize(each_item) for each_item in get_coach_data("james.txt")]))[0:3])
print(sorted(set([sanitize(each_item) for each_item in get_coach_data("julie.txt")]))[0:3])
print(sorted(set([sanitize(each_item) for each_item in get_coach_data("mikey.txt")]))[0:3])
print(sorted(set([sanitize(each_item) for each_item in get_coach_data("sarah.txt")]))[0:3])
debug.MessageBox('aaa', 'aaa')
debug.OutPutLog("D:\\a.txt", "aaaa")
