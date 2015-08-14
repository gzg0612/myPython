def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (min, secs) = time_string.split(splitter)
    return (min + '.' + secs)
class AthleteList(list):
    def __init__(self, a_name, a_dob = None, a_time = []):
        list.__init__([])
        self.name = a_name
        self.dob  = a_dob
        self.time = a_time
    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])
def get_coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return (AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as err:
        print("File Error: " + str(err))
        return (None)
