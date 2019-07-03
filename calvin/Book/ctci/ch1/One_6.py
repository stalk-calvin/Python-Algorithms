class One_6(object):
    def compress(self, input):
        result = []
        a=input[0]
        consecutive=1
        for x in input[1:]:
            if a == x:
                consecutive+=1
                continue
            else:
                result.append(a)
                result.append(str(consecutive))
                a=x
                consecutive=1

        if consecutive > 0:
            result.append(a)
            result.append(str(consecutive))

        ret = ''.join(result)
        return ret if len(ret) < len(input) else input