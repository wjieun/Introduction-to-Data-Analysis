import seaborn as sns

flights = sns.load_dataset("flights")
print(flights)

pvt = flights.pivot("month", "year", "passengers")
print(pvt)