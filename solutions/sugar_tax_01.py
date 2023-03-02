df["supp"] = df["supp"].map({0: "Standard", 1: "Supplemental"})
df["store_type_str"] = df["store_type"].map(
    {1: "Large Supermarket", 2: "Small Supermarket", 3: "Pharmacy", 4: "Gas Station"}
)
df["time"] = df["time"].replace({"MAR2015": "MAR2016"})
df
