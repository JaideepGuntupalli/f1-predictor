# 🏎️  Predicting Formula 1 Race Results

## Links
- [Website](https://f1-predictor.gjd.one/)

## Project Overview:
The primary objective of this project is to propose a machine-learning approach to predict the winner of Formula 1 Grand Prix races. By considering various present and past factors, our aim is to provide accurate predictions that can assist fans, team managers, and bettors in making informed decisions. Through robust data analysis, we aim to identify the factors contributing to race winners and predict the range of potential winners.

## Data Collection & Exploratory Data Analysis:
To conduct our analysis, we gathered data from multiple sources, including the Ergast Data repository, which contains comprehensive historical data on Formula One. We combined several datasets, including race information, race results, driver standings, constructor standings, qualifying standings, and weather information. Exploratory data analysis allowed us to gain insights into circuit analysis, driver nationality, championship wins, and other key factors influencing driver and constructor performance. This analysis was crucial in understanding the sport and informing our modeling approach.

## Machine Learning Models:
We trained multiple machine learning models to predict driver performance in Formula One races. The models we employed include logistic regression, decision tree, random forest, support vector machine, Gaussian Naive Bayes, and K-Nearest Neighbors. These models were selected based on their suitability for classification problems and their popularity in the machine learning community.

## Application of Machine Learning Models:
Using our trained models, we predicted the likelihood of drivers finishing in podium or points positions and the probability of a driver having a DNF (Did Not Finish). We compared the performance of different models and selected the best one for our final predictions. To evaluate the models' performance, we employed cross-validation, which assesses how well a model can generalize to new data. We used k-fold cross-validation to obtain reliable estimates of the models' performance and avoid overfitting.

## Tech Stack:
Our project utilized various technologies and techniques, including data preprocessing, cleaning, transformation, feature selection, and model evaluation. 

For training the model, we leveraged Python programming language and popular libraries such as Pandas, NumPy, scikit-learn, and Matplotlib for data manipulation, analysis, and visualization. Additionally, we applied feature engineering techniques to transform categorical and numerical data into a format suitable for our machine learning models.

For the frontend we used nextJS with tailwindcss

## Developed by:
- [Jaideep Guntupalli](https://jaideepguntupalli.com/)
- [Ritvik Pendyala](https://pendi.works/)
- [Tejdeep Chippa](https://github.com/phoenix1881)

## License
- [MIT](LICENSE)

## Keywords: 
motorsport, Formula One, data analysis, machine learning, classification, driver performance, constructor performance, podium prediction, points prediction, DNF index, home team effect, circuit analysis, race history, driver nationality, neural networks, statistical modeling, predictive modeling, feature engineering, exploratory data analysis, data visualization, data preprocessing, data cleaning, data transformation, feature selection, model evaluation.
