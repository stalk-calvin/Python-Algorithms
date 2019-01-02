class HistoricalDict(object):
    def __init__(self):
        self._d={}

    def set(self, key, val, time):
        if key not in self._d:
            self._d[key] = [[val], [time]]
        else:
            self._d[key][0].append(val)
            self._d[key][1].append(time)

    def get(self, key, time):
        if key in self._d:
            vallist=self._d[key][0][::-1]
            timelist = self._d[key][1][::-1]
            if time < timelist[-1]:
                return None
            else:
                for i,tt in enumerate(timelist):
                    if time>=tt:
                        return vallist[i]
                return None

    def print(self):
        print(self._d)