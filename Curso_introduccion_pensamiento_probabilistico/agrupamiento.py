import random
import math
from bokeh.plotting import figure, show


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

    def __str__(self):
        return f'{self.x}#{self.y}'


def generate_random_vectors():
    vectors = []
    for _ in range(10):
        vector = Vector(random.randint(0, 10), random.randint(0, 10))
        vectors.append(vector)
    return vectors


# We can use euclidian distance because we are dealing with a cartesian plane
def get_euclidian_distance(vector_a, vector_b):
    return math.sqrt((vector_a.x - vector_b.x)**2 + (vector_a.y - vector_b.y)**2)


def run():

    vectors = generate_random_vectors()

    # Generating a graph of the vectors with bokeh
    x_points = [vector.x for vector in vectors]
    y_points = [vector.y for vector in vectors]

    p = figure(plot_width=400, plot_height=400)

    # add a circle renderer with a size, color, and alpha
    p.circle(x_points, y_points, size=20, color="navy", alpha=0.5)

    # show the results
    show(p)

    clusters = []

    # First, I define a first cluster formed by a first random vector
    initial_vector = random.choice(vectors)
    clusters.append([initial_vector])
    vectors.remove(initial_vector)

    # I'll implement memoization with a dict of distances
    distances = {}

    # I'll work with the first cluster of my clusters list
    cluster = clusters[-1][::]

    while vectors:
        closest_relationship = ''
        for vector_tracked in cluster:
            for vector in vectors:
                if f'{vector_tracked}*{vector}' not in distances.keys():
                    distance = get_euclidian_distance(
                        vector_tracked, vector)
                    distances[f'{vector_tracked}*{vector}'] = distance
                if closest_relationship:
                    if distances[closest_relationship] > distances[f'{vector_tracked}*{vector}']:
                        closest_relationship = f'{vector_tracked}*{vector}'
                else:
                    closest_relationship = f'{vector_tracked}*{vector}'

        next_vector_x = int(closest_relationship.split('*')[1].split('#')[0])
        next_vector_y = int(closest_relationship.split('*')[1].split('#')[1])

        for vector in vectors:
            if vector.x == next_vector_x and vector.y == next_vector_y:
                cluster.append(vector)
                vectors.remove(vector)
                clusters.append(cluster[::])
                break

    for cluster in clusters:
        for vector in cluster:
            print(vector)
        print('\n')
        print('*' * 20)
        print('\n')


if __name__ == "__main__":
    run()