import numpy as np
import matplotlib.pyplot as plt

np.warnings.filterwarnings("ignore")

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

# def z(n, c):
#     if n == 0:
#         return 0

#     else:
#         return z(n - 1, c) ** 2 + c


# for n in range(10):
#     print(f"z({n}) = {z(n, c=1)}")

########################################

# def sequence(c):
#     z = 0
#     while True:
#         yield z
#         z = z ** 2 + c

# for n, z in enumerate(sequence(c=1)):
#     print(f"z({n}) = {z}")
#     if n >= 9:
#         break

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
plt.imshow(is_stable(c, num_iterations=20), cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()