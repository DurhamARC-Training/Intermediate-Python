![Course logo](img/ARC448p.png)

# Course: "Coding with Python"

Welcome to the "Coding with Python" repository! This repository contains all the materials and resources for the course.

## Course description

This practical course develops essential Python skills for researchers who have completed "[Learning to programme with Python](https://github.com/DurhamARC-Training/BasicProgrammingPython)" and want to write more effective code. We'll explore Python's core data structures (dictionaries, sets, tuples), learn list comprehensions and conditional expressions, and cover advanced string manipulation techniques for efficient data processing.
Beyond these fundamentals, we'll focus on writing robust, maintainable code through proper exception handling and modular programming. The course concludes with an introduction to object-oriented programming and classes. Throughout, we'll work through examples together, emphasising clear, readable Python that follows established conventions and prepares you for more complex computational work in your research.

## Organisation

The repository is organised as follows:

- `Intermediate.ipynb`: This file/folder contains the course material we will be using during the course

- `Intermediate_full.ipynb`: This file/folder contains the completed course material, the solutions to the exercises and the speaker notes. It is meant for reference purposes for teaching the course and as a fallback if something is missing from the notes students made during teaching.

## Accessing the Materials

For this course we are using [JupyterLite](https://jupyterlite.readthedocs.io/en/stable/), which is a tool that allows us to launch [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/) and run our Python code in the web browser through the notebook (.ipynb) files contained in this repository.

To access and run the course materials, start by:

* Navigating to the course materials on our GitHub page: [https://durhamarc-training.github.io/Intermediate-Python/](https://durhamarc-training.github.io/Intermediate-Python/)

* Start by accessing `Intermediate.ipynb`

You are now ready to start the course!

NOTE: The first time you run your code/load new modules, there may be a small wait while the module(s) are loaded.

## Contributing

If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request. Contributions are welcome!

You can add the files of the `common-tools` github submodule by typing in `git submodule update --init`. Consult the README in the then filled `common-tools` directory for further instructions.
In general you should never edit the content in the `Intermediate.ipynb` but work on `Intermediate_full.ipynb` and have the tool generate the student notebook versions automatically as described in the `common-tools` README.
