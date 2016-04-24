Since I had all that data on superhero films sitting around after my [last post](http://statsforgeeks.com/2016/04/11/much-ado-about-batman-v-superman/), I decided to take a shot at the ongoing debate over whether there are too many superhero movies. The question pops up so often that once I was finished with my analysis, a new article at *The Guardian* declared "[We've reached peak superhero. So which ones should we cull?](http://www.theguardian.com/film/2016/apr/21/which-big-screen-superheroes-should-be-culled-marvel-warner-bros-film)"

Have we reached peak superhero, though? Even Ben Child, the author of that article at *The Guardian*, admits "no." And I agree. As long as the films continue to tell excellent stories and bring fans in by the droves, the question of "too much?" is irrelevant. But when we start to see diminishing returns, as often happens with sequel after sequel after sequel, then it's time to ask "WHY ARE THEY MAKING MORE?"

When I hear people say "not another superhero movie," I often think back to the 2000s and the onslaught of romantic comedies. What better example than a film genre that saturated the market for quite some time until everyone wondered how Katherine Heigl was getting so much work. Since I had data on superhero films released between 2008 and 2015, I decided to look at romantic comedies released in the same time period. Maybe I could figure out what happened to the romantic comedy bubble and apply that to superhero films. Or maybe it was just another excuse to test out Python and Markdown.

## The Data

I scraped all films in the "Romantic Comedy" genre from BoxOfficeMojo and filtered out titles that were released in less than 500 theaters in order to concentrate on big studio releases (since there is really little comparison when it comes to independent or foreign superhero films). This had a "dumbing down" effect on critics' scores, which I gathered from Rotten Tomatoes. Independent and foreign films in the "Romantic Comedy" generally garner more critical acclaim than big-studio releases, but they also make far less money because they play in fewer theaters.

This is final table, sorted by release year:

<div class="table-responsive">
<table class="table" border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      
      <th>Title</th>
      <th>Release Year</th>
      <th>Critics' Scores</th>
      <th>Final Domestic Gross (M)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      
      <td>Trainwreck</td>
      <td>2015</td>
      <td>0.85</td>
      <td>110.21</td>
    </tr>
    <tr>
      
      <td>What If (2014)</td>
      <td>2014</td>
      <td>0.70</td>
      <td>3.49</td>
    </tr>
    <tr>
      
      <td>Magic in the Moonlight</td>
      <td>2014</td>
      <td>0.52</td>
      <td>10.54</td>
    </tr>
    <tr>
      
      <td>Blended</td>
      <td>2014</td>
      <td>0.14</td>
      <td>46.29</td>
    </tr>
    <tr>
      
      <td>About Last Night (2014)</td>
      <td>2014</td>
      <td>0.69</td>
      <td>48.64</td>
    </tr>
    <tr>
      
      <td>That Awkward Moment</td>
      <td>2014</td>
      <td>0.23</td>
      <td>26.07</td>
    </tr>
    <tr>
      
      <td>About Time</td>
      <td>2013</td>
      <td>0.70</td>
      <td>15.32</td>
    </tr>
    <tr>
      
      <td>Don Jon</td>
      <td>2013</td>
      <td>0.81</td>
      <td>24.48</td>
    </tr>
    <tr>
      
      <td>Baggage Claim</td>
      <td>2013</td>
      <td>0.14</td>
      <td>21.57</td>
    </tr>
    <tr>
      
      <td>The Big Wedding</td>
      <td>2013</td>
      <td>0.07</td>
      <td>21.82</td>
    </tr>
    <tr>
      
      <td>Playing for Keeps</td>
      <td>2012</td>
      <td>0.03</td>
      <td>13.10</td>
    </tr>
    <tr>
      
      <td>Silver Linings Playbook</td>
      <td>2012</td>
      <td>0.92</td>
      <td>132.09</td>
    </tr>
    <tr>
      
      <td>What to Expect When You're Expecting</td>
      <td>2012</td>
      <td>0.22</td>
      <td>41.15</td>
    </tr>
    <tr>
      
      <td>The Five-Year Engagement</td>
      <td>2012</td>
      <td>0.63</td>
      <td>28.84</td>
    </tr>
    <tr>
      
      <td>Think Like a Man</td>
      <td>2012</td>
      <td>0.53</td>
      <td>91.55</td>
    </tr>
    <tr>
      
      <td>New Year's Eve</td>
      <td>2011</td>
      <td>0.07</td>
      <td>54.54</td>
    </tr>
    <tr>
      
      <td>Crazy, Stupid, Love.</td>
      <td>2011</td>
      <td>0.78</td>
      <td>84.35</td>
    </tr>
    <tr>
      
      <td>Friends with Benefits</td>
      <td>2011</td>
      <td>0.70</td>
      <td>55.80</td>
    </tr>
    <tr>
      
      <td>Larry Crowne</td>
      <td>2011</td>
      <td>0.41</td>
      <td>35.61</td>
    </tr>
    <tr>
      
      <td>Monte Carlo</td>
      <td>2011</td>
      <td>0.38</td>
      <td>23.19</td>
    </tr>
    <tr>
      
      <td>Midnight in Paris</td>
      <td>2011</td>
      <td>0.93</td>
      <td>56.82</td>
    </tr>
    <tr>
      
      <td>Something Borrowed</td>
      <td>2011</td>
      <td>0.15</td>
      <td>39.05</td>
    </tr>
    <tr>
      
      <td>Jumping the Broom</td>
      <td>2011</td>
      <td>0.56</td>
      <td>37.30</td>
    </tr>
    <tr>
      
      <td>Arthur (2011)</td>
      <td>2011</td>
      <td>0.26</td>
      <td>33.04</td>
    </tr>
    <tr>
      
      <td>Just Go With It</td>
      <td>2011</td>
      <td>0.19</td>
      <td>103.03</td>
    </tr>
    <tr>
      
      <td>No Strings Attached</td>
      <td>2011</td>
      <td>0.49</td>
      <td>70.66</td>
    </tr>
    <tr>
      
      <td>How Do You Know</td>
      <td>2010</td>
      <td>0.32</td>
      <td>30.21</td>
    </tr>
    <tr>
      
      <td>Life as We Know It</td>
      <td>2010</td>
      <td>0.28</td>
      <td>53.37</td>
    </tr>
    <tr>
      
      <td>Easy A</td>
      <td>2010</td>
      <td>0.85</td>
      <td>58.40</td>
    </tr>
    <tr>
      
      <td>Going the Distance</td>
      <td>2010</td>
      <td>0.53</td>
      <td>17.80</td>
    </tr>
    <tr>
      
      <td>Sex and the City 2</td>
      <td>2010</td>
      <td>0.15</td>
      <td>95.35</td>
    </tr>
    <tr>
      
      <td>Just Wright</td>
      <td>2010</td>
      <td>0.45</td>
      <td>21.54</td>
    </tr>
    <tr>
      
      <td>The Back-Up Plan</td>
      <td>2010</td>
      <td>0.18</td>
      <td>37.49</td>
    </tr>
    <tr>
      
      <td>She's Out of My League</td>
      <td>2010</td>
      <td>0.58</td>
      <td>32.01</td>
    </tr>
    <tr>
      
      <td>Valentine's Day</td>
      <td>2010</td>
      <td>0.18</td>
      <td>110.49</td>
    </tr>
    <tr>
      
      <td>When in Rome</td>
      <td>2010</td>
      <td>0.17</td>
      <td>32.68</td>
    </tr>
    <tr>
      
      <td>Leap Year</td>
      <td>2010</td>
      <td>0.21</td>
      <td>25.92</td>
    </tr>
    <tr>
      
      <td>It's Complicated</td>
      <td>2009</td>
      <td>0.57</td>
      <td>112.74</td>
    </tr>
    <tr>
      
      <td>Did You Hear About the Morgans?</td>
      <td>2009</td>
      <td>0.12</td>
      <td>29.58</td>
    </tr>
    <tr>
      
      <td>All About Steve</td>
      <td>2009</td>
      <td>0.07</td>
      <td>33.86</td>
    </tr>
    <tr>
      
      <td>The Ugly Truth</td>
      <td>2009</td>
      <td>0.13</td>
      <td>88.92</td>
    </tr>
    <tr>
      
      <td>500 Days of Summer</td>
      <td>2009</td>
      <td>0.86</td>
      <td>32.39</td>
    </tr>
    <tr>
      
      <td>The Proposal</td>
      <td>2009</td>
      <td>0.44</td>
      <td>163.96</td>
    </tr>
    <tr>
      
      <td>My Life in Ruins</td>
      <td>2009</td>
      <td>0.09</td>
      <td>8.67</td>
    </tr>
    <tr>
      
      <td>Confessions of a Shopaholic</td>
      <td>2009</td>
      <td>0.25</td>
      <td>44.28</td>
    </tr>
    <tr>
      
      <td>He's Just Not That Into You</td>
      <td>2009</td>
      <td>0.40</td>
      <td>93.95</td>
    </tr>
    <tr>
      
      <td>New in Town</td>
      <td>2009</td>
      <td>0.29</td>
      <td>16.73</td>
    </tr>
    <tr>
      
      <td>My Best Friend's Girl</td>
      <td>2008</td>
      <td>0.14</td>
      <td>19.22</td>
    </tr>
    <tr>
      
      <td>Sex and the City</td>
      <td>2008</td>
      <td>0.49</td>
      <td>152.65</td>
    </tr>
    <tr>
      
      <td>What Happens in Vegas</td>
      <td>2008</td>
      <td>0.27</td>
      <td>80.28</td>
    </tr>
    <tr>
      
      <td>Made of Honor</td>
      <td>2008</td>
      <td>0.14</td>
      <td>46.01</td>
    </tr>
    <tr>
      
      <td>Forgetting Sarah Marshall</td>
      <td>2008</td>
      <td>0.85</td>
      <td>63.17</td>
    </tr>
    <tr>
      
      <td>Definitely, Maybe</td>
      <td>2008</td>
      <td>0.71</td>
      <td>32.24</td>
    </tr>
    <tr>
      
      <td>Fool's Gold</td>
      <td>2008</td>
      <td>0.11</td>
      <td>70.23</td>
    </tr>
    <tr>
      
      <td>27 Dresses</td>
      <td>2008</td>
      <td>0.41</td>
      <td>76.81</td>
    </tr>
  </tbody>
</table>
</div>


Details on where I acquired data on superhero films can be found [here](http://statsforgeeks.com/2016/04/11/much-ado-about-batman-v-superman/). You should probably read that before continuing. Or don't. Whatever.

## When Harry Met Tony

Here is a side-by-side comparison of the number of genre films released between 2008-2015:

<img src="super-explosion-fig-1.png"/>

There's less of a normal distribution for superhero films -- or anything that would suggest a peak. But with romantic comedies, you can see a peak between 2009 and the end of 2011. One thing to take into consideration: Superhero films cost more than romantic comedies, which would mean studios would release far less of the former. But the idea that we have reached peak superhero relies on the very fact that there are too many superhero films being released. The upcoming slates from Warner Bros/DC and Disney/Marvel Studios alone suggest we'll be seeing more down the line. For now, however, we're not seeing anything close to the romantic comedy bubble of the late 00s.

Why were so many romantic comedies being produced during this time? Just look at the ranges of total domestic gross for the films grouped by year.

<img src="super-explosion-fig-3.png"/>

These films, which don't cost as much to make as superhero films, were making back their budget and more during the peak. But something happened post 2012 that soured the public on the genre (with the exception of that lone film in 2015, "Trainwrecked," which made a lot of money because Amy Schumer.)

Now look at the ranges of total domestic gross for superhero films grouped by year.

<img src="super-explosion-fig-4.png"/>

Profits from superhero films appear to be on the upswing. Yes, the films cost more to make, but the successful ones pull in a large domestic gross as well as big earnings from foreign markets.

If 2016 so far is any indication ("Deadpool", "Batman v. Superman", and the upcoming "Captain America: Civil War"), that trend could continue.

## How Did the Romantic Comedy Bubble Burst?

So how did the romantic comedy bubble burst? I can't answer that question definitely.

Based on critics' scores, you could make the argument that the overall quality of the genre slightly improved once the studios started producing less.

The following plot compares the average critics' scores by year for both genres <sup>[1]</sup>.

<img src="super-explosion-fig-2.png"/>

However, just like I pointed out in the Batman v. Superman post, critics' opinions aren't always the best indication of how successful a film will be. With superhero films released between 2008-2015, there's a strong correlation (0.59) between critics' scores and final domestic gross. With romantic comedies there's an incredibly weak correlation (0.17), suggesting the successful films were essentially review-proof. If you doubt this, look at the combined earnings and Rotten Tomatoes scores of both Sex and the City movies.

Maybe audience scores would give us a better insight into why the bubble burst. But here's the thing, if I've learned anything economics it's that all bubbles sooner or later burst. In Hollywood, trends come and go -- just look at westerns, zombie films<sup>[2]</sup> and Shrek. So if there's anything we can learn from the romantic comedy bubble, it's that we will reach peak superhero and audiences will eventually stop caring. But maybe that means we'll get one or two good films a year instead of a brooding Superman and Will Smith playing Will Smith as Deadshot.

<hr/>

[1] I removed 2015 because the only major studio release, "Trainwrecked," received great reviews, so it skews the data.

[2] You could write a whole book, and I'm sure someone has, about how the horror genre survives despite the rise and fall of many of its sub-genres. Vampires, zombies, atomic monsters, alien invaders ... it's always a manifestation of what the public currently fears, such as disease, nuclear bombs, communism, etc. It's one of the reasons I love horror and find it so fascinating.

