# Create ASCII Box

Write a program that takes three inputs: height `h` (rows), width `w` (columns), and a character `c` and creates a `h` × `w` box using the character `c`.

For this exercise, it's recommended to use a nested for-loop. There are other ways of solving it (which might be a good starting point), but try reaching the nested for-loop solution.

```python
>>> create_box(3, 4, '*')
'****
 ****
 ****'
>>> create_box(2, 2, '@')
'@@
 @@'
```

**IMPORTANT**: You need to `return` your box, not just print it.
