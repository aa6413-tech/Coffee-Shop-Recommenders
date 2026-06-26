
# Libraries to handle data manipulation and analysis
import pandas as pd
# Tools for vectorizations and similarity calculations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def POPULARITY_BASED_RECOMMENDER():
    # Loads coffee shop rating data from excel sheet
    df = pd.read_excel('CoffeeShopRatingInfo.xlsx',
                       sheet_name='Popularity')

    # Ensures accurate decisions based on complete data void of duplicates and empty cells
    df = df.drop_duplicates()    
    df = df.dropna(subset=['Rating', 'RatingQuantity']) 

    # Convert df columns to numerical format for future calculation and ranking
    df['Rating'] = pd.to_numeric(df['Rating'])
    df['RatingQuantity'] = pd.to_numeric(df['RatingQuantity'])

    # Serves as baseline value for weighted rating formula
    c = df['Rating'].mean()

    # Establishes benchmark for identifying coffee shops with substancial data
    m = df['RatingQuantity'].quantile(0.75)
    v = df['RatingQuantity']
    r = df['Rating']

    # Formula ensures high rating with low quantities are not prioritized over coffee shops with consitently high ratings
    df['WeightedScore'] = ((v / (v + m) * r) + (m / (v + m) * c))

    # Sort by weighted scores in decending order, selects the top 10 coffee shops
    recommendations = df.sort_values(
        'WeightedScore',
        ascending = False)
    .head(10).reset_index(drop=True) 

    print('Top 10 coffee shops in Wilmington NC!\n')

    # Displays key factors used in recommendation process
    print(recommendations[
        ['CoffeeShops',
         'Rating',
         'RatingQuantity',
         'WeightedScore']
    ])


def CONTENT_BASED_RECOMMENDER():

    # Loads coffee shops attributes and features
    df = pd.read_excel('CoffeeShopRatingInfo.xlsx', sheet_name='Content')

    # Combine content features into one text column('all_content') or document
    # Format allows for TF-IDF to analyze all table content
    df['all_content'] = (
        df['CoffeeShops'].fillna('') + ' ' +
        df['Location'].fillna('') + ' ' +
        df['CoffeeType'].fillna('') + ' ' +
        df['Amenities'].fillna('') + ' ' +
        df['Atmosphere'].fillna('') + ' ' +
        df['RatingQuantity'].fillna('').astype(str) + ' ' +
        df['Rating'].fillna('').astype(str) + ' ' +
        df['PriceRange'].fillna('').astype(str) 
    )

    # Initializes tool to convert strings to numerical data
    # TF-IDF - gives higher weight to unique words in document
    vectorizer = TfidfVectorizer()

    # Converts to TF-IDF vector
    tfidf_matrix = vectorizer.fit_transform(df['all_content'])

    # Measures how similar two businesses are based on their attributes
    similarity_matrix = cosine_similarity(tfidf_matrix)


    def recommend(shop_name, top_n=3):
        # Determines row index in selected coffee shop and corresponidng similarity scores
        idx = df[df['CoffeeShops'] == shop_name].index[0]

        # Ensures the shop is present in df before proceeding
        if shop_name not in df['CoffeeShops'].values:
            return f"{shop_name} not found"
        
        # pairs each similarity score with its corresponding row and stores within list format
        scores = list(enumerate(similarity_matrix[idx]))

        
        # Sorts from most to least similar
        scores = sorted(
            scores,
            key=lambda x: x[1],
            reverse=True
            )

        # Ignoring first item since it will have a perfect similarity score
        scores = scores[1:top_n+1]

        # Collects candidates of simlarity
        recommendations = []

        # Structures data to be easily viewed by user
        for i, score in scores:
            recommendations.append({
                '--CoffeeShops--': df.iloc[i]['CoffeeShops'],
                # Rounds to SECOND decimal
                '--Similarity--': round(score, 3)
            })

        return pd.DataFrame(recommendations)


    print(recommend('Cafe Mata'))

def COLLABORATIVE_RECOMMENDER():

    # Load coffee shop attributes
    df = pd.read_excel(
        'CoffeeShopRatingInfo.xlsx',
        sheet_name='Collab')

    # Tranforms data into matrix format
    user_item_matrix = df.pivot_table(
        index='CoffeeShops',
        columns='UserID',
        values='Rating',
        fill_value=0 # Fill blank cells with '0'
    )

    
    similarity_matrix = cosine_similarity(user_item_matrix)

    def recommend(shop_name, top_n=3):

        # Ensures the shop is present in df before proceeding
        if shop_name not in user_item_matrix.index:
            return f"{shop_name} not found"

        # Retrieves row index in similarity matrix
        idx = user_item_matrix.index.get_loc(shop_name)
        
        #pair similarity scores with corresponding coffee shop's index
        scores = list(enumerate(similarity_matrix[idx]))

        # Sorts similarity scores from highest to lowest
        scores = sorted(
            scores,
            key=lambda x: x[1],
            reverse=True
        )

        # Ignoring first item since it will have a perfect similarity score
        scores = scores[1:top_n+1]

        # Collects candidates of simlarity
        recommendations = []

        # Structures data to be easily viewed by user
        for i, score in scores:
            recommendations.append({
                '--CoffeeShops--':
                    user_item_matrix.index[i],
                '--Similarity--':
                    round(score, 3)
            })

        return pd.DataFrame(recommendations)

    print(recommend('Three Friends Coffee'))


print('--------------------\nPopularity-based recommendation\n--------------------')
POPULARITY_BASED_RECOMMENDER()
print('--------------------\nContent-based recommendation\n--------------------')
CONTENT_BASED_RECOMMENDER()
print('--------------------\nCollaborative-based recommendation\n--------------------')
COLLABORATIVE_RECOMMENDER()    
