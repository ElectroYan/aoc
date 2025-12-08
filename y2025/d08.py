import day
from matrix import Vector3d
class Day(day.Day):
    def p1(self):
        vectors = []
        for l in self.lines:
            h,w,d = l.split(",")
            vectors.append(Vector3d(int(h), int(w), int(d)))

        distances = []
        for i, v1 in enumerate(vectors):
            for j, v2 in enumerate(vectors):
                if i > j:
                    distances.append((v1.euclid(v2), v1, v2))

        distances  = sorted(distances, key=lambda x: x[0])

        clusters = {}
        cluster_reverse = {}
        cluster_count = 0
        last1 = None
        last2 = None
        for dis, v1, v2 in distances[:1000]:
            passed = False
            if v1 in clusters and v2 in clusters:
                if clusters[v1] == clusters[v2]:
                    passed = True
                else:
                    cluster1 = clusters[v1]
                    cluster2 = clusters[v2]
                    vecs = cluster_reverse.pop(cluster2)
                    for vec in vecs:
                        cluster_reverse[cluster1].append(vec)
                        clusters[vec] = cluster1
            elif v1 in clusters:
                cluster = clusters[v1]
                cluster_reverse[cluster].append(v2)
                clusters[v2] = cluster
            elif v2 in clusters:
                cluster = clusters[v2]
                cluster_reverse[cluster].append(v1)
                clusters[v1] = cluster
            else:
                clusters[v1] = cluster_count
                clusters[v2] = cluster_count
                cluster_reverse[cluster_count] = [v1, v2]
                cluster_count += 1
            # print("Distance:", dis, v1, v2, "=>", clusters[v1], passed)
        # print(cluster_reverse)
        lens = [len(x) for x in cluster_reverse.values()]
        lens.sort(reverse=True)
        # print(lens)
        if len(lens) >= 3:
            return lens[0] * lens[1] * lens[2]
        else:
            return lens[0]

    def p2(self):
        vectors = []
        for l in self.lines:
            h,w,d = l.split(",")
            vectors.append(Vector3d(int(h), int(w), int(d)))

        distances = []
        for i, v1 in enumerate(vectors):
            for j, v2 in enumerate(vectors):
                if i > j:
                    distances.append((v1.euclid(v2), v1, v2))

        distances  = sorted(distances, key=lambda x: x[0])

        clusters = {}
        cluster_reverse = {}
        cluster_count = 0
        v_in_a_cluster = 0
        last1 = None
        last2 = None
        for dis, v1, v2 in distances:
            passed = False
            if v1 in clusters and v2 in clusters:
                if clusters[v1] == clusters[v2]:
                    passed = True
                else:
                    cluster1 = clusters[v1]
                    cluster2 = clusters[v2]
                    vecs = cluster_reverse.pop(cluster2)
                    for vec in vecs:
                        cluster_reverse[cluster1].append(vec)
                        clusters[vec] = cluster1
            elif v1 in clusters:
                cluster = clusters[v1]
                cluster_reverse[cluster].append(v2)
                clusters[v2] = cluster
                v_in_a_cluster += 1
            elif v2 in clusters:
                cluster = clusters[v2]
                cluster_reverse[cluster].append(v1)
                clusters[v1] = cluster
                v_in_a_cluster += 1
            else:
                clusters[v1] = cluster_count
                clusters[v2] = cluster_count
                cluster_reverse[cluster_count] = [v1, v2]
                cluster_count += 1
                v_in_a_cluster += 2
            if v_in_a_cluster == len(vectors) and len(cluster_reverse.keys()) == 1:
                last1 = v1
                last2 = v2
                break
        # print(cluster_reverse, v_in_a_cluster)
        # print(last1, last2)
        return last1.h * last2.h
