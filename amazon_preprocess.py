import csv
import os

file_path = "/Users/maxwoolf/Downloads/amazon_ratings/"
files = os.listdir(file_path)
files.remove('.DS_Store')
files.remove('amazon_ratings.csv')

with open(file_path + 'amazon_ratings.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['user_id', 'item_id', 'rating', 'timestamp', 'category'])

    for ratings_file in files:
        extracted_name = ratings_file[8:(len(ratings_file)-4)] \
                            .replace("_", " ")
        with open(file_path + ratings_file, 'rb') as f2:
            for entry in f2:
                data = entry.strip().split(",")
                writer.writerow([data[0], data[1],
                                data[2], data[3], extracted_name])

