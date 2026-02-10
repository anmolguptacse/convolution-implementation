# verify.py
from problem_a import problem_a
from problem_b import problem_b

print("---------Part (c): Equality Checking--------")

# Get outputs from both methods
O_naive = problem_a()
O_flat = problem_b()

# Parameters
N, M = 8, 16
E_pool, F_pool = 6, 6

# Calculate max difference
max_diff = 0.0
for n in range(N):
    for m in range(M):
        for x in range(E_pool):
            for y in range(F_pool):
                diff = abs(O_naive[n][m][x][y] - O_flat[n][m][x][y])
                if diff > max_diff:
                    max_diff = diff

print(f"Max absolute difference: {max_diff:.10f}")
print(f"Outputs {'MATCH' if max_diff < 1e-7 else 'DO NOT MATCH'}")

# Calculate checksums
def compute_checksum(O):
    total = 0.0
    for n in range(N):
        for m in range(M):
            for x in range(E_pool):
                for y in range(F_pool):
                    total += O[n][m][x][y]
    return total

print(f"\nChecksums:")
print(f"Naive:    {compute_checksum(O_naive):.6f}")
print(f"Flattened: {compute_checksum(O_flat):.6f}")