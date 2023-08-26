import os


# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the working directory to the script's directory
os.chdir(script_dir)

for i in os.listdir("../../../Practice - Python/"):
    print(i)




"""
chatGPT | aug/23

prompt : why the same code is working in .ipynb notebook but not in .py file ?

.ipynb : 
for i in os.listdir("../../../Practice - Python/"):
    print(i)

output : anagram.ipynb
decorators
DSA-Python
factorial.py
fibonacci
file-handling
find_nums_list.py
for-while-else-loop.ipynb
generatiors.ipynb
list_comprehension.ipynb
move_zeros.ipynb
OOPs
pattern


.py :
for i in os.listdir("../../../Practice - Python/"):
    print(i)




The code you've provided appears to be the same in both the Jupyter Notebook (.ipynb) and Python script (.py) files. However, the difference in behavior could be due to the working directory and file paths being handled differently in these two environments.

In a Jupyter Notebook, the working directory is typically set to the location of the notebook file itself. This means that when you use relative paths like `"../../../Practice - Python/"`, the notebook is looking for the directory relative to its own location.

However, when you run a standalone Python script (`.py` file), the working directory is usually the directory from which the script is executed. This might be different from the location of the script file itself, especially if you're executing it from a different directory.

To ensure consistent behavior, you should consider the following:

1. **Explicitly Set the Working Directory:** At the beginning of your script, you can explicitly set the working directory to the location of the script using the `os.chdir()` function. This way, your relative paths will work consistently.

   ```python
   import os

   # Get the directory of the script
   script_dir = os.path.dirname(os.path.abspath(__file__))

   # Set the working directory to the script's directory
   os.chdir(script_dir)

   for i in os.listdir("../../../Practice - Python/"):
       print(i)
   ```

2. **Use Absolute Paths:** Instead of relying on relative paths, you can use absolute paths to ensure that your script always accesses the correct directory, regardless of the working directory.

   ```python
   import os

   target_dir = os.path.abspath("../../../Practice - Python/")

   for i in os.listdir(target_dir):
       print(i)
   ```

By applying one of these approaches, you should be able to achieve consistent behavior between your Jupyter Notebook and standalone Python script.


"""