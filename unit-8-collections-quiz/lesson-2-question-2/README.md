# Question 2

Return the number of customers per state.
This function receives a dictionary containing states (as keys) and
customers for those states (as a list of dictionaries) and should
return a final dictionary containing the count of customers per state.

```python
customers = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',  # Eldest
        'age': 31
    }],
    'NY': [{
        'name': 'Linda',  # Eldest
        'age': 71
    }]
}
number_of_customers_per_state(customers)
>>>
{
    'UT': 2,
    'NY': 1
}
```
