import pandas as pd
import os

pos_dir = "D:/AI dataset/aclImdb_v1/aclImdb/test/pos"
neg_dir = "D:/AI dataset/aclImdb_v1/aclImdb/test/neg"

def load_reviews(folder, label):
    reviews = []
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), "r", encoding="utf-8", errors="ignore") as f:
            reviews.append((f.read(), label))
    return reviews

data = load_reviews(pos_dir, "positive") + load_reviews(neg_dir, "negative")

test_df = pd.DataFrame(data, columns=["review", "sentiment"])

test_df.to_csv("reviews_test.csv", index=False)