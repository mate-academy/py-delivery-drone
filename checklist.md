# Check Your Code Against the Following Points

1. If the function definition line is too long, place each parameter on a new line.
```
def long_function_name(
        var_one,
        var_two,
        var_three,
        var_four
) -> None:
```
2. If a variable can be `None`, you need to specify it in the annotation.
3. Make sure you're not repeating yourself. If something can be done in the parent class, delegate it there.
4. Remember, if you want to check if a variable is set to `None` and assign a default value to it,
you can use the ternary operator: `variable = other if other else 0`.
Or even simpler: `variable = other or 0`. Simple is better than complex.
