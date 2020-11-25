from flask import Flask
from flask import request
from flask import render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index() :
    return render_template("index.html")
    # when you render template remember to import it with 'from flask import render_template'

@app.route('/economic_two_thousand', methods=['POST'])
def show_economic_two_thousand () :
    if request.method == 'POST':
        url = r"C:\Users\Nicolas\Downloads\new_economic_data.csv"
        df = pd.read_csv(url)
        df.drop(df.columns[[0]], axis=1, inplace=True)
        features = ['Debt', 'Foreign_Investment', 'GDP', 'Inflation']
        x=df.loc[:,features].values
        y=df.loc[:,['New Conflict']].values
        x=StandardScaler().fit_transform(x)
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(x)
        principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
        finalDf = pd.concat([principalDf, df[['New Conflict']]], axis=1)

        fig = plt.figure(figsize = (8,8))
        ax = fig.add_subplot(1,1,1) 
        ax.set_xlabel('Principal Component 1', fontsize = 15)
        ax.set_ylabel('Principal Component 2', fontsize = 15)
        ax.set_title('2 component PCA', fontsize = 20)

        new_conflicts = [0, 1]
        colors = ['r', 'b']
        for new_conflict, color in zip(new_conflicts, colors) :
            indicesToKeep = finalDf['New Conflict'] == new_conflict
            ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], 
                    finalDf.loc[indicesToKeep, 'principal component 2']
                    , c = color, s = 50)
            ax.legend(new_conflicts)
            ax.grid()
        plt.savefig('./static/images/economic_two_thousand_plot.png')
        return render_template("index.html", name='Impact of Economic Factors on the Start of New Conflict in 2000', url='./static/images/economic_two_thousand_plot.png')

@app.route('/economic_twenty_new', methods=['POST'])
def show_economic_twenty_new() :
    if request.method == 'POST':
        url = r"C:\Users\Nicolas\Downloads\africa_economic_data.csv"
        df = pd.read_csv(url)
        df.drop(df.columns[[0]], axis=1, inplace=True)
        features = ['Debt', 'Foreign_Investment', 'GDP', 'Inflation']
        x=df.loc[:,features].values
        y=df.loc[:,['New Conflict']].values
        x=StandardScaler().fit_transform(x)
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(x)
        principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
        finalDf = pd.concat([principalDf, df[['New Conflict']]], axis=1)

        fig = plt.figure(figsize = (8,8))
        ax = fig.add_subplot(1,1,1) 
        ax.set_xlabel('Principal Component 1', fontsize = 15)
        ax.set_ylabel('Principal Component 2', fontsize = 15)
        ax.set_title('2 component PCA', fontsize = 20)

        new_conflicts = [0, 1]
        colors = ['r', 'b']
        for new_conflict, color in zip(new_conflicts, colors) :
            indicesToKeep = finalDf['New Conflict'] == new_conflict
            ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], 
                    finalDf.loc[indicesToKeep, 'principal component 2']
                    , c = color, s = 50)
            ax.legend(new_conflicts)
            ax.grid()
        plt.savefig('./static/images/economic_twenty_new.png')
        return render_template("index.html", name='Impact of Economic Factors on the Start of New Conflicts From 1997 to 2018', url='./static/images/economic_twenty_new.png')

@app.route('/ethnicity_two_thousand', methods=['POST'])
def show_ethnicity_two_thousand () :
    if request.method == 'POST':
        url = r"C:\Users\Nicolas\Downloads\new_economic_data.csv"
        df = pd.read_csv(url)
        df.drop(df.columns[[0]], axis=1, inplace=True)
        features = ['Ethnicity', 'Religion']
        x=df.loc[:,features].values
        y=df.loc[:,['New Conflict']].values
        x=StandardScaler().fit_transform(x)
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(x)
        principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
        finalDf = pd.concat([principalDf, df[['New Conflict']]], axis=1)

        fig = plt.figure(figsize = (8,8))
        ax = fig.add_subplot(1,1,1) 
        ax.set_xlabel('Principal Component 1', fontsize = 15)
        ax.set_ylabel('Principal Component 2', fontsize = 15)
        ax.set_title('2 component PCA', fontsize = 20)

        new_conflicts = [0, 1]
        colors = ['r', 'b']
        for new_conflict, color in zip(new_conflicts, colors) :
            indicesToKeep = finalDf['New Conflict'] == new_conflict
            ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], 
                    finalDf.loc[indicesToKeep, 'principal component 2']
                    , c = color, s = 50)
            ax.legend(new_conflicts)
            ax.grid()
        plt.savefig('./static/images/ethnicity_two_thousand.png')
        return render_template("index.html", name='Impact of Ethnicity and Religion on the Start of New Conflicts in the Year 2000', url='./static/images/ethnicity_two_thousand.png')

@app.route('/ethnicity_twenty', methods=['POST'])
def show_ethnicity_twenty () :
    if request.method == 'POST':
        url = r"C:\Users\Nicolas\Downloads\africa_economic_data.csv"
        df = pd.read_csv(url)
        df.drop(df.columns[[0]], axis=1, inplace=True)
        features = ['Ethnicity', 'Religion']
        x=df.loc[:,features].values
        y=df.loc[:,['New Conflict']].values
        x=StandardScaler().fit_transform(x)
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(x)
        principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
        finalDf = pd.concat([principalDf, df[['New Conflict']]], axis=1)

        fig = plt.figure(figsize = (8,8))
        ax = fig.add_subplot(1,1,1) 
        ax.set_xlabel('Principal Component 1', fontsize = 15)
        ax.set_ylabel('Principal Component 2', fontsize = 15)
        ax.set_title('2 component PCA', fontsize = 20)

        new_conflicts = [0, 1]
        colors = ['r', 'b']
        for new_conflict, color in zip(new_conflicts, colors) :
            indicesToKeep = finalDf['New Conflict'] == new_conflict
            ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], 
                    finalDf.loc[indicesToKeep, 'principal component 2']
                    , c = color, s = 50)
            ax.legend(new_conflicts)
            ax.grid()
        plt.savefig('./static/images/ethnicity_twenty_years.png')
        return render_template("index.html", name='Impact of Ethnicity and Religion on the Start of New Conflicts From 1997 to 2018', url='./static/images/ethnicity_twenty_years.png')
