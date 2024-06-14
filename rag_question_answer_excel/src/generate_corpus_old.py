import pandas as pd

# Define the corpus data for flowers with thematic, question, and answer
data = {
    "Thematics": [
        "National Flowers", "Night Bloomers", "Love Symbols", "Fragrant Flowers",
        "Wedding Flowers", "Sun Lovers", "Remembrance Flowers", "Thousand Leaves",
        "Luxury Symbols", "Winter Bloomers", "Apology Flowers", "Greek Names",
        "Tea Flowers", "Cheerful Flowers", "Sacred Flowers", "Easter Flowers",
        "New Beginnings", "Sun Followers", "Greek Mythology", "Purple Flowers",
        "Valentine's Day", "South African Flowers", "Trumpet Flowers", "Rainbow Flowers",
        "Peaceful Flowers", "Dutch Named", "Heart-shaped Leaves", "Medicinal Flowers",
        "Teacher Appreciation", "Star Named", "Desert Flowers", "Hawaiian Leis",
        "Southern Symbols", "Delicate Petals", "Saffron Production", "Kyoto Symbol",
        "Friendship Symbols", "Round Blooms", "Eternal Life", "Christmas Flowers",
        "Blue Dyes", "Buddhist Symbols", "Latin Sword", "Mother's Day Bouquets",
        "Trumpet Shape", "Fall Season", "Resilient Flowers", "Culinary Flowers",
        "Humility Symbols", "Lily Named"
    ],
    "Questions": [
        "What is the national flower of Japan?",
        "Which flower is known as the 'Queen of the Night'?",
        "Which flower symbolizes love and passion?",
        "Which flower is famous for its beautiful fragrance and is often used in perfumes?",
        "What flower represents purity and is often used in weddings?",
        "Which flower is known as the 'Sun's Favorite'?",
        "Which flower is associated with the remembrance of the dead, particularly in Mexico?",
        "Which flower's name means 'a thousand leaves'?",
        "Which flower is considered a symbol of luxury and wealth in Chinese culture?",
        "Which flower is known for blooming in the harsh conditions of winter?",
        "Which flower is often given as a sign of apology?",
        "Which flower has a name that means 'beautiful' in Greek?",
        "Which flower is used to make a popular type of tea, especially in China?",
        "Which flower is known for its bright yellow color and is a symbol of cheerfulness?",
        "Which flower was sacred to the ancient Egyptians?",
        "Which flower is often associated with the Easter holiday?",
        "Which flower symbolizes new beginnings and rebirth?",
        "Which flower is known for its ability to open and close with the sun?",
        "Which flower is known as the 'Flower of the Gods' in Greek mythology?",
        "Which flower is famous for its various shades of purple and its pleasant scent?",
        "Which flower is often associated with the month of February and Valentine's Day?",
        "Which flower is native to South Africa and is known for its unique shape?",
        "Which flower is known for its large, trumpet-shaped blooms and vibrant colors?",
        "Which flower has a name derived from the Greek word for 'rainbow'?",
        "Which flower is a symbol of peace and calmness, often seen in blue and white?",
        "Which flower is named after a famous Dutch painter?",
        "Which flower is known for its heart-shaped leaves and blooms?",
        "Which flower is known for its medicinal properties and is often used in herbal teas?",
        "Which flower is often given to teachers to show appreciation?",
        "Which flower's name means 'star' in Greek?",
        "Which flower is known for its ability to thrive in dry, desert conditions?",
        "Which flower is often used in leis in Hawaii?",
        "Which flower is a traditional symbol of the American South?",
        "Which flower is known for its delicate petals and sweet fragrance?",
        "Which flower is often used in the production of saffron?",
        "Which flower is associated with the city of Kyoto, Japan?",
        "Which flower symbolizes friendship and happiness?",
        "Which flower is known for its large, round blooms and is often used in floral arrangements?",
        "Which flower is a symbol of eternal life and is often seen in ancient art?",
        "Which flower is known for its vibrant red color and is often associated with Christmas?",
        "Which flower is known for its striking blue color and is often used in dyes?",
        "Which flower is often associated with the Buddhist religion?",
        "Which flower's name means 'sword' in Latin?",
        "Which flower is often used in bouquets for Mother's Day?",
        "Which flower is known for its trumpet-like shape and vibrant yellow color?",
        "Which flower is often associated with the fall season?",
        "Which flower is known for its resilience and ability to survive harsh conditions?",
        "Which flower is famous for its use in culinary dishes, particularly in France?",
        "Which flower is often associated with the concept of humility?",
        "Which flower's name means 'flower of the lily' in Latin?"
    ],
    "Answers": [
        "Cherry Blossom", "Cereus", "Rose", "Jasmine", "Lily", "Sunflower", "Marigold", "Yarrow",
        "Peony", "Camellia", "Orchid", "Calla Lily", "Chrysanthemum", "Daffodil", "Lotus", "Lily",
        "Daffodil", "Sunflower", "Carnation", "Lavender", "Rose", "Protea", "Hibiscus", "Iris",
        "White Poppy", "Tulip", "Bleeding Heart", "Chamomile", "Apple Blossom", "Aster",
        "Cactus Flower", "Plumeria", "Magnolia", "Gardenia", "Saffron Crocus", "Cherry Blossom",
        "Yellow Rose", "Hydrangea", "Ivy", "Poinsettia", "Bluebell", "Lotus", "Gladiolus", "Carnation",
        "Daffodil", "Chrysanthemum", "Dandelion", "Lavender", "Violet", "Lilium"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_path = "../corpus/data.csv"
df.to_csv(csv_path, index=False)
