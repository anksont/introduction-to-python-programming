# Question 3

Eldest customer per state.
This function receives a dictionary containing states (as keys) and
customers for those states (as a list of dictionaries) and should
return a final dictionary containing the eldest customer per each state.

```python
Example:
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
    }, {
        'name': 'Lisa',
        'age': 25
    }]
}
eldest_customer_per_state(customers)
>>>
{
    'UT': {
        'name': 'John',
        'age': 31
    },
    'NY': {
        'name': 'Linda',
        'age': 71
    }
}
```
