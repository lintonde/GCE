import random
import time

DIMS = 64
STEP = 10.0
EPS = 1e-4

SCALE = 1.37
SHIFTS = [random.uniform(-50, 50) for _ in range(DIMS)]

NOISE_POINTS = 100_000

# ---------- helpers ----------
def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def bits_to_text(bits):
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join(chr(int(c, 2)) for c in chars if len(c) == 8)

def triangle_area(p1, p2, p3):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    return abs(
        x1*(y2-y3) +
        x2*(y3-y1) +
        x3*(y1-y2)
    ) / 2

def make_point(x, y):
    # 2D + padding
    return [x, y] + [random.uniform(-1,1) for _ in range(DIMS-2)]

def is_on_grid(p):
    return abs(p[0]/STEP - round(p[0]/STEP)) < EPS and \
           abs(p[1]/STEP - round(p[1]/STEP)) < EPS

def transform(p):
    return [(p[i]*SCALE + SHIFTS[i]) for i in range(DIMS)]

def inverse(p):
    return [((p[i] - SHIFTS[i]) / SCALE) for i in range(DIMS)]

# ---------- encode ----------
def encode(message):
    bits = text_to_bits(message)
    pts = []

    # open marker
    pts += [
        make_point(-1000, 0),
        make_point(-990, 20),
        make_point(-980, 0)
    ]

    for i, b in enumerate(bits):
        x = i * 40

        p1 = make_point(x, 0)
        p2 = make_point(x, STEP)

        if b == '1':
            p3 = make_point(x + STEP, 0)
        else:
            p3 = make_point(x + 2*STEP, 0)

        pts += [p1, p2, p3]

    # close marker
    pts += [
        make_point(100000, 0),
        make_point(100010, 30),
        make_point(100020, 0)
    ]

    return pts

# ---------- noise ----------
def add_noise(points):
    for _ in range(NOISE_POINTS):
        x = random.uniform(-5000, 5000) + 0.37*STEP
        y = random.uniform(-5000, 5000) + 0.61*STEP
        points.append(make_point(x, y))
    random.shuffle(points)
    return points

# ---------- decode ----------
def decode(points):
    grid = [p for p in points if is_on_grid(p)]
    grid.sort(key=lambda p: (p[0], p[1]))

    payload = grid[3:-3]
    bits = ""

    for i in range(0, len(payload), 3):
        tri = payload[i:i+3]
        if len(tri) < 3:
            break

        tri = sorted(tri, key=lambda p: (p[0], p[1]))
        area = triangle_area(tri[0], tri[1], tri[2])

        if area < 0.75 * STEP * STEP:
            bits += '1'
        else:
            bits += '0'

    return bits_to_text(bits)

# ---------- run ----------
message = "HELLO WORLD"

t0 = time.time()

pts = encode(message)
pts = add_noise(pts)

encrypted = [transform(p) for p in pts]

t1 = time.time()

decrypted = [inverse(p) for p in encrypted]
decoded = decode(decrypted)

t2 = time.time()

print("Decoded:", decoded)
print("Encrypt time:", round(t1 - t0, 3), "sec")
print("Decrypt time:", round(t2 - t1, 3), "sec")
print("Total points:", len(encrypted))
