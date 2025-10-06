# General Python syntax

## Main

Overall layout of a Python script with a main function.

    ```python
    # First in the file.
    def main():
        ...

    # All the code in between.
    ...

    # At the end of the file.
    if __name__ == "__main__":
        main()
    ```


## If

The ternary conditional operator

    ```python
    return "even" if n % 2 == 0 else "odd"
    ```

Easy way to check if a value is falsy : None, 0, empty string, False

    ```python
    if not name:
        print('Falsy')
    ```
