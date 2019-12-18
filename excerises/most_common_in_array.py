from collections import Counter
import statistics


class MostCommonInArray(object):
    def __init__(self, array):
        self.array = array

    def most_common_collections(self):
        data = Counter(self.array)
        return data.most_common[0][0]

    def most_common_statistics(self):
        return statistics.mode(self.array)

    def most_common_manual(self):
        result = {}
        most_pop_value_key = None
        sec_most_pop_value_key = None
        for element in self.array:
            if not result.has_key(element):
                result.update({element: 1})
                if most_pop_value_key is None:
                    most_pop_value_key = element
                    sec_most_pop_value_key = element
            else:
                result.update({element: result[element] + 1})
                if result[element] > result[most_pop_value_key]:
                    most_pop_value_key = element
                else:
                    if result[element] > result[sec_most_pop_value_key]:
                        sec_most_pop_value_key = element

        return result, most_pop_value_key, sec_most_pop_value_key


if __name__ == "__main__":
    # list = [1, 3, -1, 4, -2, -3, 10, 2, 5, -4, 0]
    array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 0, 0, 1, 1, 1, -2, -2, -2]
    most_common = MostCommonInArray(array)
    result = most_common.most_common_manual()
    print(result)
