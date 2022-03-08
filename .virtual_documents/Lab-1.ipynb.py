import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
plt.rcParams["figure.figsize"] = [10, 5]


data = pd.read_excel("Pulse.xlsx",converters={'Gender':str})


data


print(f'Average Height = {np.mean(data[["Height"]])[0]:.2f}')
print(f'Average Weight = {np.mean(data[["Weight"]])[0]:.2f}')


male_data = data[data["Gender"] == "Male"]
female_data = data[data["Gender"] == "Female"]


print('===================================')
print(f'Average Height of Male = {np.mean(male_data[["Height"]])[0]:.2f}')
print(f'Average Weight of Male = {np.mean(male_data[["Weight"]])[0]:.2f}')
print('===================================')
print(f'Average Height of Female = {np.mean(female_data[["Height"]])[0]:.2f}')
print(f'Average Weight of female = {np.mean(female_data[["Weight"]])[0]:.2f}')

print('===================================')


print("Most frequent Height and number of students with that Height respectively:")
data[["Height"]].value_counts()[:5]


print("Most frequent Weight and number of students with that Weight respectively:")
data[["Weight"]].value_counts()[:5]


height_weight = data[["Height", "Weight"]]
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Blaine Mason', fontsize=16)
height_weight[["Height"]].hist('Height', ax=ax1, bins=15, color="b", alpha=.7)
height_weight[["Weight"]].hist('Weight', ax=ax2, bins=15, color="r", alpha=.7)
ax1.grid(b=False)
ax2.grid(b=False)
plt.show()


display(Image.open('plots/Dotplot of Height.png'))
display(Image.open('plots/Dotplot of Weight.png'))
display(Image.open('plots/Dotplot of HeightG.png'))
display(Image.open('plots/Dotplot of WeightG.png'))


genders = data[["Gender"]].value_counts()
labels=["Male", "Female"]
plt.pie(genders,labels=labels, autopct='get_ipython().run_line_magic("1.1f%%');", "")


smokes = data[["Smokes"]].value_counts()
labels=["Doesn't Smoke Regularly", "Smokes Regularly"]
plt.pie(genders,labels=labels, autopct='get_ipython().run_line_magic("1.1f%%');", "")


fig, ax = plt.subplots()
plt.title('Blaine Mason', fontsize=16)
ax.bar(x=labels, height=[data["Smokes"].value_counts().iloc[0],data["Smokes"].value_counts().iloc[1]]);


X_axis = np.arange(len(labels))
plt.bar(X_axis, height=[male_data["Smokes"].value_counts().iloc[0],male_data["Smokes"].value_counts().iloc[1]], width=0.3, label="Male")
plt.bar(X_axis + .3, height=[female_data["Smokes"].value_counts().iloc[0],female_data["Smokes"].value_counts().iloc[1]], width=0.3, label="Female")
plt.xticks(X_axis + .2/2, labels)
plt.legend()
plt.title("Blaine Mason", fontsize=16)
plt.show()
