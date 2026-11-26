import pandas as pd

df = pd.read_excel("dmart_dataset.xlsx")

df["Discount"] = (
    pd.to_numeric(df["Discount"], errors="coerce")
    .fillna(0)
)

df["Quantity"] = (
    df["Quantity"]
    .replace({"two": 2, "Three": 3, "three": 3})
)

df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["Unit_Price"] = pd.to_numeric(
    df["Unit_Price"],
    errors="coerce"
)

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

for col in [
    "Store_Location",
    "Product_Category",
    "Product_Name",
    "Payment_Method"
]:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.title()
    )

df["Gross_Sales"] = (
    df["Quantity"] *
    df["Unit_Price"]
)

df["Discount_Flag"] = (
    df["Discount"] >
    df["Gross_Sales"]
)

df = (
    df
    .drop_duplicates(subset=["Invoice_ID"])
    .sort_values("Date")
    .reset_index(drop=True)
)

df.to_excel(
    "clean_invoice_data.xlsx",
    index=False
)

print(
    " Cleaned Excel file saved as clean_invoice_data.xlsx"
)
