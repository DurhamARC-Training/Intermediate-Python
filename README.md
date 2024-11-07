# Coding with Python

Welcome to ARC training course "Coding with Python" repository! This repository contains all the materials and resources for the course.

## Organisation

The repository is organized as follows:

- `Intermediate.ipynb`: The course's Jupyter notebook with the corresponding materials.

- `Intermediate_full.ipynb`: The course's Jupyter notebook with all the material filled in. It is meant for reference purposes for teaching the course and as a fallback if something is missing from the notes students made during the course.

- `pull_files_from_repo.py`: download script that can be executed to extract this repository into a folder.

## Getting started as student

There are three possibilities to get the data:

1. If you want only to follow along, just download and open the `Intermediate.ipynb` notebook on your machine or in your environment using your local Jypyter installation.

2. If you have GIT available, you can just clone the repo with:

   `git clone https://github.com/DurhamARC-Training/Intermediate-Python.git`

3. There is also a python script which downloads everything (including the filled notebook) as a ZIP archive and extracts it a folder if GIT isn't available:

      a. Download the `pull_files_from_repo.py` file and put it into your environment

      b. Execute `python pull_files_from_repo.py` in the folder.

## Getting started for teaching

To get started with teaching the course, follow these steps:

1. Install the requirements including JupyterLab Deck by running the following command to create a conda environment:

    ```
    conda env create -f environment.yml
    ```

2. Launch a JupyterLab session by running the following command:

    ```
    conda activate intermediate_python
    jupyter-lab
    ```

3. Use the `Intermediate.ipynb` for the presentations and exercises to use during the course. If needed, use the `Intermediate_full.ipynb` notebook as lecture notes with solutions.

4. Click on the little card styles JupyterLab-Deck icon for running a notebook as a presentation.

5. It is also possible to convert the Jupyter notebook to PDF (be sure first to run all cells you want to run and save):

    * Call `jupyter nbconvert --to slides --post serve `Intermediate.ipynb`
    * Go to http://localhost:8000/Intermediate.slides.html?print-pdf#/
    * Print via Print to PDF function of your browser

## Contributing

If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request. Contributions are welcome!