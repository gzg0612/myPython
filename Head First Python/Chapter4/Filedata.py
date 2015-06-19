import pickle
man = []
other = []
try:
    with open('sketch.txt') as data:
        data.seek(0)
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = line_spoken.strip()
                if 'Man' == role:
                    man.append(line_spoken)
                elif 'Other Man' == role:
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError:
    print("The data file is missing")

try:
    with open("man.out", "wb") as man_data, open("other.out", "wb") as other_data:
        pickle.dump(man, man_data)
        pickle.dump(other, other_data)
except IOError as err:
    print("open file error:" + str(err))
except pickle.pickleError as err:
    print("pickle err:" + str(err))
