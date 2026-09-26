import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer_churn.csv")

print("\n--- CUSTOMER DATA ---")
print(df)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

churn_rate = (df["Churn"] == "Yes").mean() * 100
print("\nOverall Churn Rate:", round(churn_rate, 2), "%")

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print("\n--- CHURN BY CONTRACT ---")
print(contract_churn)

df["Tenure_Group"] = pd.cut(
    df["Tenure"],
    bins=[0, 6, 12, 24, 100],
    labels=["0-6 months", "7-12 months", "13-24 months", "24+ months"]
)

tenure_churn = pd.crosstab(
    df["Tenure_Group"],
    df["Churn"],
    normalize="index"
) * 100

print("\n--- CHURN BY TENURE ---")
print(tenure_churn)

charge_analysis = df.groupby("Churn")["Monthly_Charges"].mean()
print("\n--- AVERAGE MONTHLY CHARGES ---")
print(charge_analysis)

support_analysis = df.groupby("Churn")["Support_Calls"].mean()
print("\n--- AVERAGE SUPPORT CALLS ---")
print(support_analysis)

df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("churn_distribution.png")
plt.show()

print("\n--- KEY INSIGHTS ---")
print("1. Customers on month-to-month contracts show higher churn in this sample.")
print("2. Customers with shorter tenure show greater churn.")
print("3. Higher support-call frequency is associated with churn in this sample.")
print("4. Churn patterns can help businesses identify customers requiring retention efforts.")
