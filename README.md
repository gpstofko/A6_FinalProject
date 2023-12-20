# A6_FinalProject
Group Mates: Griffin Stofko, Divinefavour Osuji, Miles Lambert, Bruno Pena-Lepe

**Took out:**
Central African Republic,2017,CAF,347.33,383309,,,,,,,,,,59.02,0.67,40.98,2.16,,,,,,,6.611111,20.939444,POINT (6.611111 20.939444)
B/c nan in third index
Eritrea,2017,ERI,33.97,54005,,,,,,,,,,,,,,,,,,,,15.179384,39.782334,POINT (15.179384 39.782334)
B/c Nan in all index's
(These for NAN Y-Values)
Lesotho,2017,LSO,,,,,,,,,,,,72.27,0.22,27.73,2.29,68.65,59.32,92.96,42.75,42.77,42.72,-29.609988,28.233608,POINT (-29.609988 28.233608)
Mauritius,2017,MUS,,,,,,,,,,,,59.16,0.21,40.84,-0.08,99.87,99.83,99.92,95.5,95.18,95.97,-20.348404,57.552152,POINT (-20.348404 57.552152)
Seychelles,2017,SYC,,,,,,,,,,,,43.74,0.25,56.26,1.99,96.25,,,100,,,-4.679574,55.491977,POINT (-4.679574 55.491977)
Tunisia,2017,TUN,,,,,,92.66,,,78.12,,88.29,31.36,0.2,68.64,1.57,96.25,88.71,99.7,90.92,81.35,95.29,33.886917,9.537499,POINT (33.886917 9.537499)

**Reflection Questions:**
Choose a dataset.
The dataset utilized includes data regarding African countries during the year 2017 and their malaria cases and other factors: https://www.kaggle.com/datasets/lydia70/malaria-in-africa

Determine which algorithm is the best fit. Based on the dataset you choose, you will need to figure out which algorithm to use. This will require you to get to know your data and your goals! Is there a linear correlation between variables? Are you looking for numerical value or a label/category? Do you know the labels or do you need the model to create them for you?

We tried to create and find a correlation between incidence of malaria (per 1000 population at risk) and multiple variables, including People using at least basic sanitation services (% of population), urban population (% of total population) as well as rural population (% of total population). We're looking for a numberical value from multivariable linear regression for the combined variables to correlate rural and urban populations as well as basic sanitation services to incidence of malaria. From the data, our Y value was incidence of malaria (per 1000 population at risk) and our three X-values were People using at least basic sanitation services (% of population), urban population (% of total population),and rural population (% of total population).

Do some tests with matplotlib and visualize your data. Does it provide a good correlation? Why or why not?
There is almost no correlation between the urban population% and instances of malaria as well as little correlation between access to sanitation services and malaria.

Program your model. Once you have chosen your type of model, it’s time to create it! In this step, you will write a program that fits your chosen model to the data. Your program and output will be specific to the model you choose.

Analyze and present your findings. An important part of creating predictive models is being able to communicate the results. In this final step of the project, you will present your findings using slides or an infographic. Your product should include the following components:
