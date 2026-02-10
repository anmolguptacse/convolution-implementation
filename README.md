# convolution-implementation


# Convolution Implementation Study

This repository contains implementations of convolution operations with performance analysis, as per the problem statement.

## Problem Statement
Implement convolution with parameters:
- N=8, C=4, H=28, W=28, R=5, S=5, M=16
- Random signed values between 0 and 1
- Average pooling (2x2), stride=2, no zero padding

## Implementation Details

### a) 7-loop Naive Implementation (`problem_a.py`)
- 7 nested loops: N → M → E → F → R → S → C
- Direct computation without optimization

### b) Flattened Implementation (`problem_b.py`)
- Flatten weights and patches
- Matrix multiplication approach
- Two versions: original and optimized

### c) Equality Verification (`verify.py`)
- Compares outputs from both implementations
- Verifies results match within tolerance

### d) Performance Measurement
- Uses `perf` command to measure instructions and execution time

### e) Analysis 
- Performance comparison
- Memory analysis
- Speedup calculations

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/anmolguptacse/convolution-implementation.git
cd convolution-implementation
```
### 2. Run individual implementations
``` bash
# Naive implementation
python3 problem_a.py

# Flattened implementation
python3 problem_b.py
```
### 3.Verify equality (Part c)
``` bash
python3 verify.p
```
### 4.Measure Perforrmance
```
perf stat -e instructions,cycles,cpu-clock python3 problem_a.py
perf stat -e instructions,cycles,cpu-clock python3 problem_b.py
