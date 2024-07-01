# README: Neural Network Challenge - Student Loan Repayment Prediction

## Background
At our company, which specializes in student loan refinancing, predicting borrower repayment capabilities is vital for setting accurate interest rates. This project focuses on developing a neural network model capable of predicting the likelihood of student loan repayments based on borrower data.

## Project Files
- **Module 18 Challenge files**: [Download here](https://www.example.com/download)
- **student_loans_with_deep_learning.ipynb**: Starter file to be used in Google Colab

## Initial Setup
1. **Repository Setup**: Create a new GitHub repository named `neural-network-challenge-1`.
2. **Clone Repository**: Clone the repository to your local machine.
3. **Add Starter File**: Add the downloaded `student_loans_with_deep_learning.ipynb` to your repository.
4. **Push Changes**: Ensure all changes are pushed to your GitHub repository.
5. **Google Colab**: Upload the notebook to Google Colab for development.

## Instructions

### Part 1: Data Preparation
- **Data Reading**: Load the dataset from [student-loans.csv](https://static.bc-edx.com/ai/ail-v-1-0/m18/lms/datasets/student-loans.csv) into a Pandas DataFrame. Identify potential features and target variables.
- **Dataset Creation**: Separate the data into features (X) and target (y) datasets. Use the `credit_ranking` column as the target.
- **Data Splitting**: Divide the datasets into training and testing sets.
- **Data Scaling**: Utilize scikit-learn’s StandardScaler to scale the feature data.

### Part 2: Model Development and Evaluation
- **Neural Network Design**: Construct a deep neural network using TensorFlow's Keras. Tailor the model architecture based on the number of input features.
- **Model Compilation and Training**: Compile the model with binary_crossentropy loss function, adam optimizer, and accuracy metric. Fit the model on training data.
- **Model Evaluation**: Assess the model with testing data to determine its loss and accuracy.
- **Model Saving**: Save and export the model as `student_loans.keras`.

### Part 3: Predicting Loan Repayment
- **Model Loading**: Reload the saved model.
- **Make Predictions**: Apply the model to the testing data, generate predictions, convert them to binary values, and save the results in a DataFrame.
- **Classification Report**: Generate and analyze a classification report based on the predictions and the testing data.

### Part 4: Recommendation System Discussion
- **Data Requirements**: Discuss the types of data required for a student loan recommendation system and its relevance.
- **Filtering Method**: Define whether the system will use collaborative, content-based, or context-based filtering and justify the choice.
- **Real-world Challenges**: Identify and explain two real-world challenges in building a student loan recommendation system.

## Hints and Considerations
- Review data preprocessing methods from previous modules if needed.
- Ensure consistency in preprocessing for both training and testing datasets.

## Requirements
Ensure that your Jupyter Notebook includes detailed sections for each part of the project, demonstrating all steps from data preparation to predictions and discussions on the recommendation system.

**Push all changes and updates regularly to your GitHub repository to track version history and collaborate effectively.**

## Acknowledgments

I would like to express my gratitude to OpenAI's ChatGPT for its invaluable assistance during the course of this project. The conversational AI provided essential insights and support in data analysis, problem-solving, and the generation of content, which significantly contributed to the success of this endeavor.
