import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Influencer Dataset
def generate_influencers(n=1000):
    categories = ['Fitness', 'Wellness', 'Bodybuilding', 'Nutrition']
    platforms = ['Instagram', 'YouTube', 'Twitter', 'Facebook']
    genders = ['Male', 'Female']

    data = []
    for i in range(n):
        data.append([
            i + 1,
            fake.name(),
            random.choice(categories),
            random.choice(genders),
            random.randint(10000, 1000000),  # follower count
            random.choice(platforms)
        ])
    return pd.DataFrame(data, columns=['ID', 'Name', 'Category', 'Gender', 'Follower Count', 'Platform'])

# Posts Dataset
def generate_posts(influencers_df, n=1000):
    data = []
    for _ in range(n):
        influencer = influencers_df.sample(1).iloc[0]
        data.append([
            influencer['ID'],
            influencer['Platform'],
            fake.date_between(start_date='-90d', end_date='today'),
            fake.url(),
            fake.sentence(nb_words=6),
            random.randint(1000, influencer['Follower Count']),
            random.randint(100, 50000),
            random.randint(10, 5000)
        ])
    return pd.DataFrame(data, columns=['influencer_id', 'Platform', 'Date', 'URL', 'Caption', 'Reach', 'Likes', 'Comments'])

# Tracking Data Dataset
def generate_tracking_data(influencers_df, n=1000):
    products = ['Whey Protein', 'Creatine', 'Vitamin C', 'Multivitamin']
    campaigns = ['FitJuly', 'PowerBoost', 'SummerShred', 'WellnessWave']
    data = []
    for _ in range(n):
        influencer = influencers_df.sample(1).iloc[0]
        data.append([
            influencer['Platform'],
            random.choice(campaigns),
            influencer['ID'],
            fake.uuid4(),
            random.choice(products),
            fake.date_between(start_date='-90d', end_date='today'),
            random.randint(1, 20),
            random.randint(500, 10000)
        ])
    return pd.DataFrame(data, columns=['source', 'campaign', 'influencer_id', 'user_id', 'product', 'date', 'orders', 'revenue'])

# Payouts Dataset
def generate_payouts(influencers_df, n=1000):
    basis_options = ['post', 'order']
    data = []
    for _ in range(n):
        influencer = influencers_df.sample(1).iloc[0]
        basis = random.choice(basis_options)
        rate = random.randint(200, 2000)
        orders = random.randint(1, 20)
        total_payout = rate if basis == 'post' else rate * orders
        data.append([
            influencer['ID'],
            basis,
            rate,
            orders,
            total_payout
        ])
    return pd.DataFrame(data, columns=['influencer_id', 'basis', 'rate', 'orders', 'total_payout'])

# Generate all datasets
influencers_df = generate_influencers()
posts_df = generate_posts(influencers_df)
tracking_df = generate_tracking_data(influencers_df)
payouts_df = generate_payouts(influencers_df)

# Save to CSV
influencers_df.to_csv('influencers.csv', index=False)
posts_df.to_csv('posts.csv', index=False)
tracking_df.to_csv('tracking_data.csv', index=False)
payouts_df.to_csv('payouts.csv', index=False)

print("✅ All datasets generated and saved as CSV!")
