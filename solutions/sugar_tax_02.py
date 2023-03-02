pt_products = df.pivot_table(
    index=["type"], columns="time", values="price", aggfunc="count", margins=True
)
pt_products
