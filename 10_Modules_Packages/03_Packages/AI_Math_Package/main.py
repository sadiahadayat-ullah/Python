from ai_math import arithmetic
from ai_math import statistics
from ai_math import geometry
from ai_math import linear_algebra

print("Multiplication:",arithmetic.multiply(20,10))
print("Division:",arithmetic.divide(20,10))

numbers = [10,20,30,40,50]

print("Average:",statistics.average(numbers))
print("Maximum:",statistics.maximum(numbers))

print("Circle Area:",geometry.area_circle(5))

print("Vector Add:",linear_algebra.vector_add([1,2],[3,4]))
print("Dot Product:",linear_algebra.dot_product([1,2],[3,4]))
