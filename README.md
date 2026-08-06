# D'Mart Sales Dashboard | Power BI

## Overview

The D'Mart Sales Dashboard is an interactive Business Intelligence project built using Power BI. It transforms retail sales data into meaningful business insights through KPIs, DAX measures, interactive visualizations, and slicers. The dashboard enables users to monitor sales performance, analyze trends, compare store performance, and make data-driven decisions.

---

## Objectives

- Analyze overall sales performance.
- Track monthly revenue trends.
- Compare revenue across store locations.
- Identify top-performing product categories.
- Analyze payment method distribution.
- Build an interactive dashboard using Power BI.

---

## Dataset

The dataset contains retail sales transactions with the following columns:

| Column |
|--------|
| Invoice_ID |
| Date |
| Store_Location |
| Product_Category |
| Product_Name |
| Quantity |
| Unit_Price |
| Discount |
| Payment_Method |
| Customer_ID |

---

## Dashboard KPIs

- Total Revenue
- Total Orders
- Total Quantity Sold
- Average Order Value

---

## Dashboard Visuals

- Revenue Trend (Line Chart)
- Revenue by Store Location (Bar Chart)
- Revenue by Product Category (Donut Chart)
- Revenue by Payment Method (Donut Chart)
- Top Products by Revenue (Bar Chart)
- Interactive Slicers

---

## Slicers

- Date
- Store Location
- Product Category
- Payment Method

---

## DAX Measures

### Revenue

```DAX
Revenue =
SUMX(
    Sales,
    (Sales[Quantity] * Sales[Unit_Price]) - Sales[Discount]
)
```

### Total Orders

```DAX
Total Orders =
DISTINCTCOUNT(Sales[Invoice_ID])
```

### Total Quantity Sold

```DAX
Total Quantity Sold =
SUM(Sales[Quantity])
```

### Average Order Value

```DAX
Average Order Value =
DIVIDE([Revenue],[Total Orders])
```

---

## Business Insights

- Monitor monthly revenue growth.
- Compare sales across store locations.
- Identify best-selling products.
- Analyze customer payment preferences.
- Evaluate category-wise revenue performance.

---

## Tools & Technologies

- Power BI Desktop
- Power Query
- DAX
- Data Modeling
- Data Visualization

---

## Skills Demonstrated

- Data Cleaning
- Data Transformation
- DAX Calculations
- KPI Design
- Dashboard Development
- Business Intelligence
- Interactive Reporting

---

## Project Structure

```text
Dmart-Sales-Dashboard/
│
├── Dataset/
│   └── Dmart_Sales.xlsx
│
├── Dashboard/
│   └── Dmart_Sales_Dashboard.pbix
│
├── Images/
│   └── Dashboard.png
│
└── README.md
```

---

## Dashboard Preview

> Add your Power BI dashboard screenshot here.


<img width="958" height="542" alt="image" src="https://github.com/user-attachments/assets/38fb036f-cfef-406d-ab37-0db4a3665c66" />


---

## Future Improvements

- Customer Segmentation
- Profit Analysis
- Regional Performance Analysis
- Forecasting using Power BI
- Dynamic Target vs Actual KPIs

---

## Author

**Shrikrushna Dhebe**

Data Analyst | Python | SQL | Power BI

---

## License

This project is created for learning and portfolio purposes.
