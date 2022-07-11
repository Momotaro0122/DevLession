# Work - find texture

## Details

1. Line 24 - string format

```python
print("Spend time : {:0.4f} sec".format(spend_time))
                    # ^ "0.4f would be print 4 digits float number
```

2. Recommand function's document

```python
def find_texture(maya_file):
    '''
    [::args::]
        -- List your argument and key-word arguments
    [::return::]
        -- Describe what will your return, or any exceptions.
    '''
```

3. Try to use more "meaningful" variable name
4. Try to add "plural" at list object represenet we have multiple data.

```python
for i in content:
    pass
# More meaningful :
for line in contents:
    pass
```

5. match_list is not good, try let it more "meaningful"

```python
match_list = [] # Matched strings > not good
# Because we want to saving texture path string,
# "textures" is more meaningful here.
textures = [] 
```

6. Using sys.argv to get arugmnet from outside

```python
maya_file = sys.argv[1]
```
