class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links

class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        t = tuple(filter(lambda x: (id(x.v1) == id(link.v1) and id(x.v2) == id(link.v2)) or \
                  (id(x.v2) == id(link.v1) and id(x.v1) == id(link.v2)), self._links))
        if len(t) == 0:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)
    def _dist_path(self, links):
        return sum([x.dist for x in links if x is not None])
    def find_path(self, start_v, stop_v):
        self._start_v = start_v
        self._stop_v = stop_v
        return self._next(self._start_v, None, [], [])

    def _next(self, current, link_prev, current_path, current_links):
        current_path += [current]
        if link_prev:
            current_links += [link_prev]

        if current == self._stop_v:
            return current_path, current_links

        len_path = -1
        best_path = []
        best_links = []
        for link in current.links:
            path = []
            links = []
            if link.v1 not in current_links:
                path, links = self._next(link.v1, link, current_path[:], current_links[:])
            elif link.v2 not in current_path:
                path, links = self._next(link.v2, link, current_path[:], current_links[:])
            if self._stop_v in path and (len_path == -1 or len_path > self._dist_path(links)):
                len_path = self._dist_path(links)
                best_path = path[:]
                best_links = links[:]
        return best_path, best_links

class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def __repr__(self):
        return self.name
class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist