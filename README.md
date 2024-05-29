# Relational Analysis & Visualization

This project is concerned with predicting the future sales of a product to facilitating the manufacturing and advertesing costs of the product. I developed this project in 2024-06-09. The ML-Model is using Linear Regression, which I was familiar with as I was working on this project because of my prior project of [Cyber Physical Systems of Systems](https://github.com/mrjex/Cyber-Physical-Systems-and-Sytems-of-Systems). Furthermore, it was my first time using Plotly to visualize charts. However, I didn't find it difficult since I had experience with a similar library for Javascript, Chartjs, from my [Bookster](https://github.com/mrjex/Bookster) project.


## Dataflow

The initial input derived from the CSV file in `/dataset`, and the final output of the execution is stored in `/output-current` in two categories:

**PNG:** A static artifact that denies interaction with the viewer. The advantage of using this format is the ease it brings for the viewers to quickly gain a brief overview of the visualized data.

**HTML:** A dynamic artifact that allows interaction, such that the viewer can hover of the datapoints to get a closer look on the exact data-values.


I sketched the flow of the different states obtainable in this project, which is demonstrated below. Before dissecting the semantics of the picture below, it's important to understand the general executional flow of this project:

You need to run the project by typing `./run.sh` in your terminal. This script invokes the following sequential steps:
    - 1: Store previous outputs from the latest execution of the project in "/output-previous" directory
    - 2: Remove the content stored in "/output-current" directory
    - 3: Generate new output in "/output-current" directory



![Finite-State-Machine](Finite-State-Machine.PNG)

**Explanation:**
    - Each state or node in the picture represents a unique state in the execution of this repository
    - States:
        - S0: Run repository for the first time by running "./run.sh"
        - S1: First time running the repository. No generated output in "/output-current". This implies that the code can't generate a previous output backup/comparison
        - S2: The repository was successfully executed and the output files in "/output-current" was generated
        - S3: Run repository for the (n + 1)th time, where n >= 1. There is now generated files in "/output-current" such that the code can generate the comparative .txt files in "/output-previous" directory
        - S4: Store the "current" output files as .txt files in the (n + 1)th time, n >= 1
    
    - Given the explanation above, the sequence of the visited states for the users is predictable:
        - First iteration: S0, S1, S2, S3, S4
        - (N + 1)th iteration, N >= 1: S2, S4
        - Final conclusion: S0, S1, S2, S3, S4, S2, S4, S2, S4, S2, S4, ..., (S2, S4) * N
        - Simplified conclusion: S0, S1, S2, S3, S4, ((S2, S4) * N)
        



## Output / Generated Artifacts

![1-advertise-tv-units-sold](output-current/png/1-advertise-tv-units-sold.png)

![2-advertise-newspapers-units-sold](output-current/png/2-advertise-newspapers-units-sold.png)

![3-advertise-radio-units-sold](output-current/png/3-advertise-radio-units-sold.png)



## Potential Installation Problems

1. Make sure you have installed the necessary Python dependencies:
    - Python CLI
    - python pip
    - pandas
    - kaleido
    

On Windows 10, you must install the following version of Kaleido, otherwise the latest version works perfectly fine

```
pip install --upgrade kaleido=="0.1.0.post1"
```