class One_9(object):
    def string_rotation(self, s1, s2):
        s3 = s2+s2
        if s1 in s3:
            return True
        else:
            return False