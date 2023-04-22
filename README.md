# ML-Micro-service. 

This microservice application provides a machine learning prediction algorithm for the classic Iris dataset. The application is built using Python, Flask, HTML, and Tailwind CSS. The algorithm is trained using the classic Iris dataset and predicts the species of an iris flower based on its sepal length, sepal width, petal length, and petal width.

## Installation
To install the dependencies, run the following command:

```bash
pip3 install -r requirments.txt
```
You also need to install Tailwind CSS. Follow the instructions on Tailwind CSS website to install it.

## Instructions
To run the code, execute the following command:

```bash
python3 app.py
```

You also need to execute the following command to compile the CSS file:
```bash
npm run css
```

## File Tree
```tree
├── package.json
├── package-lock.json
├── __pycache__
│   ├── algorithm.cpython-310.pyc
│   └── webFunction.cpython-310.pyc
├── README.md
├── requirments.txt
├── modeling.ipynb
├── static
│   └── css
│       ├── dist
│       │   └── output.css
│       └── src
│           └── input.css
├── tailwind.config.js
├── templates
│   └── index.html
└── webFunction.py

```
## Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and create a new branch. Then, submit a pull request with your changes.