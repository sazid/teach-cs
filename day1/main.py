# modulo
a = 5
print(a % 2)

# array
arr = [1, 2, 3, 4, 5]
print(arr[6 % 5])

p = 3

result = 0
result += ord('c') * 1
result += ord('a') * 3
result += ord("t") * 9

result = 0
result += ord("t") * 1
result += ord("a") * 3
result += ord("c") * 9

# hashing <-> unique identity of anything in the universe
def hash_(key: str) -> int:
    result = 0
    p = 257
    p_pow = 1
    mod = 10

    for c in key:
        result = (result + (ord(c) * p_pow) % mod ) % mod
        p_pow = (p_pow * p) % mod

    return result


# "name" -> 2, value = "Mini furr"
# "age" -> 2, value = 5
bucket = [
    [],
    [],
    [
        ("name", "Mini furr"),
        ("age", 5),
        ("hairstyle", "red"),
    ],
]

# Dictionary/Unordered map
class MyDict:
    def __init__(self):
        self.buckets = [[]] * 8

    def __setitem__(self, key, value):
        index = hash(key) % 8
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def __getitem__(self, key):
        index = hash(key) % 8
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def __str__(self):
        res = "{ "
        for bucket in self.buckets:
            for k, v in bucket:
                res += f"{k}: {v}"
                res += ", "
            res += ", "
        res += " }"
        return res

    def __repr__(self):
        return str(self)

d = MyDict()
d["name"] = "Mini furr"
d["age"] = 5
d["name"] = "Black fur"
print(d["name"])
print(d["age"])
print(d)
