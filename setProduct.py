#dictionary with correct product names as key and metadata value as val.

products = { 
  "PSA (Manage)" : "Manage", "CPQ (Sell)" : "Sell", "BCDR (Recover)" : "Recover", "Help Desk (Assist)" : "Assist", "MDR (Fortify)" : "Fortify", "SIEM (Perch)" : "Perch"}

#function to get metadata by name
def getsafeMetadata(metadataname):
  safeMeta = ''
  metadataValue = document.get_meta_data_value(metadataname)
  if len(metadataValue) > 0:
    safeMeta = metadataValue[-1]
    print(safeMeta)
  return safeMeta

#function to map product based on products dict, data cleaning using split
def getProduct(val):
  #edge case that getsafeMetadata returned ''
  if val == '':
    return 'Knowledge Article'
  #checking for and then splitting multiple product items
  val = val.split(';')
  if len(val) > 1:
    return addMultiProduct(val)
  for key, value in products.items():
    if val[0] == value:
      val[0] = key
  return 'ConnectWise ' + val[0]

#function to add multiple products to indexed item
def addMultiProduct(list):
  newString = ''
  for product in list:
    product = 'ConnectWise ' + getProduct(product);
    newString += product + ';'
  return newString

# try calling getsafemetadata and mapping value to product metadata
try:
  uri = getsafeMetadata('kav_dc_products')
  document.add_meta_data({ 'product': getProduct(uri) })
  document.add_meta_data({ 'commonproduct': getProduct(uri) })
except Exception as e:
  print(e)
