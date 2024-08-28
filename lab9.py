import pandas as pd
import numpy as np

sku = pd.read_csv('lesson9data/SKU.csv')
supplier = pd.read_csv('lesson9data/supplier.csv')
inventory = pd.read_csv('lesson9data/inventory.csv')

# 1
inventory = pd.merge(pd.merge(sku, inventory, on="SKU", how="right"), supplier, on="Supplier_code", how='left')
print(inventory)

# 2
inventory.to_csv('final.csv', index=False)

# 3
no_suplier = inventory[inventory['Supplier_name'].isnull()]
print(no_suplier)

supplier_from_inventory = inventory["Supplier_code"].unique()
print(supplier_from_inventory)

supplier_from_supplier_df = np.array(supplier["Supplier_code"])
print(supplier_from_supplier_df)

not_in_inventory = np.setdiff1d(supplier_from_supplier_df, supplier_from_inventory)
print(not_in_inventory)

