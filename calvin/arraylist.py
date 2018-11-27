class ArrayList(object):
    def swapMinMax(self, values):
        min_index=0
        for i in range(1, len(values)):
            if values[i] < values[min_index]:
                min_index = i

        max_index=0
        for i in range(1, len(values)):
            if values[i] > values[max_index]:
                max_index=i

        t=values[min_index]
        values[min_index] = values[max_index]
        values[max_index]=t

    def rotate_matrix(self, image):
        if image is None or len(image) == 0 or len(image) != len(image[0]):
            return None

        n = len(image)
        for layer in range(int(n/2)):
            first=layer
            last=n-1-layer
            for i in range(first,last):
                offset=i-first
                top=image[first][i]

                image[first][i] = image[last-offset][first]
                image[last-offset][first] = image[last][last-offset]
                image[last][last-offset] = image[i][last]
                image[i][last] = top

        return image