## Coffee-Shop-Recommenders
Designed a recommendation engine that analyzed coffee shop ratings, amenities, price and user preferences using popularity-based, content-based, and collaborative filtering algorithms.

## Project objective
Develop a Python-based coffee shop recommendation system that analyzes an Excel dataset and generate personalized recommendations using popularity-based, content-based, and collaborative filtering. The project utilizes Pandas for data preprocessing and Scikit-learn for vectorization and similarity computations to recommend coffee shops based on user preferences and historical interactions.

## Dataset used
- <a href="https://github.com/aa6413-tech/Coffee-Shop-Recommenders/blob/main/CoffeeShopRatingInfo.xlsx">Dataset<a/>

## Questions (KPIs)
- What amenities appear most often among recommended shops?
- How diverse are the recommendations made?
- Are users more likely to prefer specialty coffee shops or chain locations?

- Dashboard interaction <a href="https://github.com/aa6413-tech/Coffee-Shop-Recommenders/blob/main/Recommender_image.png">View Dashboard</a>

## Process
- Load coffee shop data from a centralized Excel dataset using Pandas.
- Validate and preprocess the dataset by removing duplicate records and handling missing values.
- Extract and organize relevant coffee shop attributes, ratings, and user interaction data.
- Transform the processed data into a format suitable for recommendation analysis (feature vectors or user-item matrices).
- Apply a recommendation algorithm to measure relationships between coffee shops based on popularity, content similarity, or user preferences.
- Rank candidate coffee shops according to their recommendation scores.
- Return the highest-ranked coffee shops as personalized recommendations.
- Present the recommendation results in a clear, tabular format for easy interpretation.

## Dashboard

<img width="437" height="326" alt="Recommender_image" src="https://github.com/user-attachments/assets/88f8a6ac-4f0d-4307-b611-02aa90c334f0" />

## Project insight
- Coffee shops with widley desired amenities, such as wheelchair-accessibility, Wifi, and dog-friendly enviroments, appeared more frequently across recommendation scenarios.
- Coffee shops with a broad selection of coffee types were recommended more consistently than coffee shops that offered a specialized, limited menu. 
- Coffee shops combining a diverse and broad selections of amenities, menu options, and consistently high cutomer ratings achieved the strongest overall recommendation rankings, while niche or highly specialized shops appeared less frequently in top recommendations.

## Final Conclusion
The analysis indicates that recommendation outcomes are primarily influenced by the breadth of a coffee shop's offerings and customer-focused features. Coffee shops that provide widely desired amenities, diverse coffee selections, and consistently high customer ratings appeared most frequently across recommendation scenarios, while niche or highly specialized shops ranked less often. These findings suggest that well-rounded coffee shops with broad appeal are more likely to be recommended across popularity-based, content-based, and collaborative filtering approaches to users.


