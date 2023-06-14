Sign Language Interpreter Project
==============================
## Data Science Domains: Computer Vision, Classification Machine Learning

Effective communication is one of the most important aspects in society. However, for people who rely on sign language, communication with those unfamiliar with this communication method is a difficult task. A model that is able to take a video stream from a camera as an input, and then output the letters that are being signed can be an invaluable tool. This model could be deployed to places like hospitals, schools, and government offices to help facilitate communication so that it does not represent a significant barrier.

# Important Files 
* [sign_language_interpreter.py](https://github.com/lau-allen/sign-language-interpreter/blob/main/sign_language_interpreter.py) - entry point to launch the sign language interpreter, which utilizes your computer webcam to retrieve hand signs as inputs to a CNN model. The result of this script is the model prediction of the signed hand. 
* [/reports/Sign_Language_Interpreter_FinalNotebook.ipynb](https://github.com/lau-allen/sign-language-interpreter/blob/main/reports/Sign_Language_Interpreter_FinalNotebook.ipynb) - Jupyter Notebook containing the finalized code and explanations of the data science process used to create the sign language interpreter project. 
* [/reports/Sign_Language_Interpreter_Presentation.pdf](https://github.com/lau-allen/sign-language-interpreter/blob/main/reports/Sign_Language_Interpreter_Presentation.pdf) - Slide deck for the presentation of the project. 

# Additional Information
Additional Contributors:
Link to Original Repo: 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
