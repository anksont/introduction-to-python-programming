# Question 4

Create a simple class `Car` that is initialized by providing two arguments mandatory arguments, `model` and `color` and one optional one, `convertible` which should be `False` by default.

The class must set those three values as attributes of each instance in order to access the values later. Check the examples below:

```python
c1 = Car(model='BMW E46', color='Red')
print(c1.model)       # 'BMW E46'
print(c1.color)       # 'Red'
print(c1.convertible) # False

c2 = Car(model='Toyota MR2', color='Blue', convertible=True)
print(c2.model)       # 'Toyota MR2'
print(c2.color)       # 'Blue'
print(c2.convertible) # True
```
