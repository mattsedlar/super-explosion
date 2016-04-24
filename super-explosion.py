import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

movies = ["Fantastic Four","The Dark Knight Rises","Kick-Ass 2", "Avengers: Age of Ultron", "Iron Man 3", "Captain America: Winter Soldier", "X-Men: First Class", "The Amazing Spider-Man 2", "Thor", "Ant-Man","Guardians of the Galaxy","Captain America: First Avenger","Thor: The Dark World","The Wolverine","TMNT (2014)", "Green Lantern","Marvel's The Avengers","X-Men: Days of Future Past","Green Hornet","Ghost Rider: Spirit of Vengeance","Big Hero 6","Man of Steel","Chronicle","Dredd","Kick-Ass","Jonah Hex","Iron Man 2","X-Men Origins: Wolverine","Watchmen","Push","Jumper","Iron Man","The Incredible Hulk","Hellboy II: The Golden Army","The Dark Knight","Punisher: War Zone","The Spirit"]

release_year = pd.Series(["2015","2012","2013","2015","2013","2014","2011","2014","2011","2015","2014","2011","2013","2013","2014","2011","2012","2014","2011","2012","2014","2013","2012","2012","2010","2010","2010","2009","2009","2009","2008","2008","2008","2008","2008","2008","2008"], index=movies, dtype="category")

final_gross = pd.Series([56.1,448.1,28.8,459,409,259.8,146.4,202.9,181,180.2,333.2,176.7,206.4,132.6,191.2,116.6,623.4,233.9,98.8,51.8,222.5,291,64.5,13.4,48,10.5,312,179.8,107.5,31.8,80.1,318.4,134.8,75.9,534.8,8,19.8], index=movies)


critics = pd.Series([.09,.87,.30,.75,.79,.89,.87,.53,.77,.80,.91,.79,.67,.70,.21,.26,.92,.91,.43,.17,.89,.56,.85,.78,.76,.12,.72,.38,.65,.23,.16,.94,.67,.85,.94,.27,.14], index=movies)


d = { "Release Year" : release_year,
      "Domestic Gross" : final_gross,
      "CriticsScores": critics }

df = pd.DataFrame(d)

# make release_year a factor

df["Release Year"] = df["Release Year"].cat.reorder_categories(['2008','2009','2010','2011','2012','2013','2014','2015'])

df = df.sort_values(by="Release Year")

pivot = df.pivot_table(index=["Release Year"], values=["Release Year","CriticsScores"],aggfunc={"Release Year":len,"CriticsScores":np.mean})
# drop 2015 for critics fig
#pivot = pivot.drop(['2015'])
print(pivot)

# PULL in Romantic Comedy Data

comedies = pd.read_csv('List-of-Romantic-Comedies.csv')
comedies["release_year"] = comedies["release_year"].astype("category")
comedies = comedies.sort_values(by="release_year")

comedies= comedies.reindex(np.arange(0,len(comedies),1))

print(comedies.to_html())

pivot2 = comedies.pivot_table(index=["release_year"], values=["release_year","critics_scores","domestic_gross"],aggfunc={"release_year":len,"critics_scores":np.mean})
# drop 2015 for critics fig
#pivot2 = pivot2.ix[:-1]
print(pivot2)

y = ["2008","2009","2010","2011","2012","2013","2014","2015"]
y_pos = np.arange(len(y))

# PLOTS

fig = plt.figure()
ax = plt.axes([0.025,0.025,0.95,0.95])
plt.barh(y_pos,+pivot['Release Year'].values, facecolor='#26b226', edgecolor="white",align="center")
plt.barh(y_pos,-pivot2['release_year'].values, facecolor='#ff69B4', edgecolor="white",align="center")
plt.xticks([])
plt.xlabel("Source: BoxOfficeMojo.com, Wikipedia",fontsize=10)
plt.yticks(y_pos,y)
plt.xlim(-13,9)
plt.annotate("Superhero Films",xy=(0.25,7.65))
plt.annotate("Romantic Comedies",xy=(-5,7.65))
for x,y in zip(y_pos,pivot['Release Year'].values):
  plt.annotate(y, xy=(y+.5,x-.05))
for x,y in zip(y_pos,pivot2['release_year'].values):
  plt.annotate(y, xy=(-y-1,x-.05))
plt.title("Number of Genre Films Released, 2008-2015", fontsize=16)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.get_yaxis().tick_left()
fig.savefig("super-explosion-fig-1.png",bbox_inches="tight")

# fig = plt.figure()
# ax = plt.axes([0.025,0.025,0.95,0.95])
# plt.barh(y_pos,+pivot['CriticsScores'].values, facecolor='#26b226', edgecolor="white",align="center")
# plt.barh(y_pos,-pivot2['critics_scores'].values, facecolor='#ff69B4', edgecolor="white",align="center")
# plt.xticks([])
# plt.xlabel("Source: Rotten Tomatoes, BoxOfficeMojo.com, Author's Calculations", fontsize=10)
# plt.yticks(y_pos,y)
# plt.xlim(-1,1.15)
# plt.annotate("Superhero Films",xy=(0.01,6.65))
# plt.annotate("Romantic Comedies",xy=(-0.49,6.65))
# for x,y in zip(y_pos,pivot['CriticsScores'].values):
#   plt.annotate(math.ceil(y * 100)/100, xy=(y+.015,x-.05))
# for x,y in zip(y_pos,pivot2['critics_scores'].values):
#   plt.annotate(math.ceil(y * 100)/100, xy=(-y-.135,x-.05))
# plt.title("Average Critics' Scores of Genre Films Released, 2008-2014", fontsize=16)
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
# ax.spines["left"].set_visible(False)
# ax.spines["bottom"].set_visible(False)
# ax.get_yaxis().tick_left()
# fig.savefig("super-explosion-fig-2.png",bbox_inches="tight")

# ROMANTIC COMEDIES GROSS

ax2 = comedies.boxplot(column="domestic_gross",by="release_year")
ax2.set_title("Domestic Gross of Romantic Comedy Films, 2008-2015")
ax2.set_xlabel("Release Year\n\n Source:BoxOfficeMojo.com")
ax2.set_ylabel("Domestic Gross (M)")
ax2.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)
fig = ax2.get_figure()
fig.suptitle('')
fig.savefig("super-explosion-fig-3.png")

# ROMANTIC COMEDIES GROSS

ax3 = df.boxplot(column="Domestic Gross",by="Release Year")
ax3.set_title("Domestic Gross of Superhero Films, 2008-2015")
ax3.set_xlabel("Release Year\n\n Source:BoxOfficeMojo.com")
ax3.set_ylabel("Domestic Gross (M)")
ax3.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)
fig = ax3.get_figure()
fig.suptitle('')
fig.savefig("super-explosion-fig-4.png")

print("correlation between final gross and critics scores")
print(np.corrcoef(comedies["domestic_gross"], comedies["critics_scores"]))
