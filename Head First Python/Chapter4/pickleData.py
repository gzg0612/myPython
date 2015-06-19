import pickle
try:
    with open("man.out", "wb") as man_data, open("other.out", "wb") as other_data:
        pickle.dump(man, man_data)
        pickle.dump(other, other_data)
except IOError as err:
    print("open file error:" + str(err))
except pickle.pickleError as err:
    print("pickle err:" + str(err))
