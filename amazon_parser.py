import csv, json

category_string = "Video Game,Wireless Phone Accessory,Wireless Phone Accessory,,,Electronics,,Electronics,Office Product,Paperback,Hardcover,Hardcover,Hardcover,Paperback,Hardcover,Hardcover,Personal Computers,,Personal Computers,Automotive,Personal Computers,Personal Computers,Toy,Misc.,Tools & Home Improvement,Electronics,Jewelry,,,Jewelry,Wireless Phone Accessory,,Electronics,Electronics,Electronics,,Electronics,Electronics,Ecard Gift Certificate,Ecard Gift Certificate,Camera,Electronics,Electronics,Electronics,Sports,Paperback,Paperback,Electronics,Lawn & Patio,Paperback,Paperback,Personal Computers,Paperback,Sports,Kitchen,,Vinyl,Paperback,Electronics,Electronics,,Personal Computers,Accessory,Electronics,Electronics,,Grocery,Health and Beauty,Video Game,Office Product,Personal Computers,,Toy,Paperback,Spiral-bound,,Grocery,Grocery,,Paperback,Sports,Paperback,Toy,Paperback,Camera,,Electronics,Personal Computers,Toy,Paperback,Camera,Electronics,Toy,Electronics,Misc.,Office Product,,Wireless Phone Accessory,Paperback,Paperback,Hardcover,,Wireless Phone Accessory,,,,,Sports,Camera,Electronics,Toy,Toy,,Tools & Home Improvement,Tools & Home Improvement,Personal Computers,,,Misc.,,Health and Beauty,,Paperback,Paperback,Paperback,Perfect Paperback,Electronics,Personal Computers,Tools & Home Improvement,Watch,Paperback,Paperback,Tools & Home Improvement,,Wireless Phone Accessory,Misc.,,Tools & Home Improvement,Toy,Electronics,Paperback,Personal Computers,Personal Computers,Personal Computers,,Electronics,Personal Computers,Personal Computers,Personal Computers,Paperback,Camera,Electronics,Electronics,Camera,Electronics,Electronics,Camera,Video Game,Paperback,Paperback,Paperback,Paperback,Paperback,Paperback,Paperback,Electronics,Personal Computers,Personal Computers,,Personal Computers,Personal Computers,Personal Computers,Personal Computers,Personal Computers,Personal Computers,,Hardcover,Hardcover,Paperback,Paperback,Sports,,Paperback,Tools & Home Improvement,Tools & Home Improvement,Grocery,Toy,Health and Beauty,Paperback,Paperback,Paperback,Lawn & Patio,Health and Beauty,Apparel,Health and Beauty,Automotive,Misc.,,Ecard Gift Certificate,Ecard Gift Certificate,Apparel,,Apparel,,Electronics,,,Office Product,,Toy,Toy,Misc.,Electronics,Electronics,Personal Computers,Tools & Home Improvement,Personal Computers,Personal Computers,,Electronics,Paperback,Paperback,Toy,Paperback,Paperback,Office Product,Paperback,Paperback,Paperback,Paperback,Paperback,Paperback,Paperback,Health and Beauty,Paperback,Paperback,Hardcover,Electronics,Electronics,Misc.,Paperback,Misc.,Misc.,Electronics,,Kitchen,Toy,Kitchen,Misc.,Personal Computers,Paperback,Grocery,Ecard Gift Certificate,Ecard Gift Certificate,Personal Computers,Personal Computers,Personal Computers,Personal Computers,,Electronics,Personal Computers,Misc.,Personal Computers,Personal Computers,Tools & Home Improvement,Tools & Home Improvement,Paperback,Office Product,Office Product,Misc.,Misc.,Office Product,,Hardcover,,Ecard Gift Certificate,,Electronics,Automotive,Sports,Toy,Electronics,Office Product,Health and Beauty,Misc.,Video Game,Hardcover,Electronics,Electronics,Ecard Gift Certificate,Camera,Personal Computers,Personal Computers,,Personal Computers,Electronics,,,Electronics,Health and Beauty,Electronics,Misc.,Health and Beauty,Health and Beauty,Misc.,Kitchen,Sports,Sports,Personal Computers,,Personal Computers,Personal Computers,Personal Computers,Personal Computers,Paperback,Paperback,Paperback,Health and Beauty,Personal Computers,Mass Market Paperback,Health and Beauty,Hardcover,Sports,Misc.,,Toy,,,Electronics,Misc.,Misc.,Kitchen,Misc.,Personal Computers,Misc.,Wireless Phone Accessory,Misc.,Electronics,Personal Computers,Paperback,Health and Beauty,Health and Beauty,,Health and Beauty,Toy,Hardcover,Paperback,Paperback,Paperback,Paperback,Mass Market Paperback,Paperback,Mass Market Paperback,Paperback,Office Product,Wireless Phone Accessory,Wireless Phone Accessory,Mass Market Paperback,Paperback,Sports,Electronics,Paperback,Paperback,Electronics,Electronics,Paperback,Paperback,Paperback,Paperback,Office Product,Office Product,Office Product,Paperback,Personal Computers,Office Product,Kitchen,Paperback,Toy,Toy,Kitchen,Office Product,Office Product,Baby Product,Paperback,Paperback,Electronics,Apparel,Kitchen,Kitchen,,,,,,Office Product,,,,,Health and Beauty,,Tools & Home Improvement,Health and Beauty,Health and Beauty,Health and Beauty,Health and Beauty,,Jewelry,Jewelry,,,,,Health and Beauty,Paperback,Electronics,Electronics,Electronics"


def write_categories_to_file(file_name):
    categories = category_string.split(",")
    category_counts = dict((c, 0) for c in categories)
    with open("./data/amazon_data.csv", "r") as f:
        reader = csv.reader(f)
        for line in reader:
            if line[0] == "Order Date":
                continue
            tokens = line
            for token in tokens:
                if token in categories:
                    category_counts[categories[categories.index(token)]] += 1

    with open(file_name, "w") as f:
        f.write(json.dumps(category_counts))

write_categories_to_file("./data/amazon.json")