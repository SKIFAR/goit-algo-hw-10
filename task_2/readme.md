# Monte Carlo Integration

## Objective
The goal of this task is to calculate the definite integral of a given function using the **Monte Carlo method** and verify the accuracy of the result by comparing it with the analytical solution obtained using the **`quad`** function from the `scipy.integrate` module.

---

## Methodology

### 1. Monte Carlo Integration
The Monte Carlo method estimates the integral by:
1. Randomly generating points (x, y) within a rectangular area that fully contains the function’s graph.
2. Counting how many of these points fall below the curve y = f(x).
3. Calculating the ratio of points under the curve to the total number of points and multiplying it by the area of the rectangle.

Multiple experiments are performed, and the average result is taken to improve accuracy.

### 2. Verification with SciPy `quad`
To verify the accuracy of the Monte Carlo estimate, the same integral is computed using the built-in numerical integration method:

```python
result, error = scipy.integrate.quad(f, a, b)
```

This function provides a highly accurate numerical result and an estimation of the integration error.

---

## Visualization

A plot is generated to visualize:

- The function **f(x)** in red.  
- The integration interval **[a, b]** shaded in gray.  
- The bounding rectangle used in the Monte Carlo simulation (dashed blue lines).  

---

## Results Example

Example output (values may vary slightly due to randomness):

- Monte Carlo integral ≈ 7.083752
- SciPy quad integral = 7.083718 (±7.86e-14)

---

## Conclusion

The result obtained using the **Monte Carlo method** is very close to the value calculated using the **SciPy `quad`** function, confirming the correctness of the algorithm.  
The small difference between the two results is due to the stochastic nature of the Monte Carlo approach.  
Increasing the number of random points and experiments reduces the error and improves accuracy.
