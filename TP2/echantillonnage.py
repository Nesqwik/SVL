
class Echantillonnage:

    def sous_echantillonnage(self, array, size, frequency):
        out = []
        i = 0
        while i < len(array):
            lenth = min(size, len(array) - i)
            out.extend(array[i:(i+lenth)])
            i += frequency

        return out
