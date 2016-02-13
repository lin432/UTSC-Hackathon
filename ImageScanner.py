import urllib2
import subprocess

EAN_ACCESS_CODE = "F2EF335156BEAF07"

def get_upc(fileName):
    '''(str) -> str
    gets the upc from an image.
    '''
    output = subprocess.check_output("zbarimg -D " + fileName)
    output = output.strip()
    output = output[output.index(':')+1:]
    return output
    
def get_data(upc_code):
    '''(string) -> str
    accesses EANdata.com with free data stream for data on product
    '''

    response = urllib2.urlopen("http://eandata.com/feed/?v=3&mode=json&keycode="
                               + EAN_ACCESS_CODE + "&find=" + upc_code)
    data = response.read()
    if data.find('company') != -1:
        
        company = data[data.find('company')-1:len(data)-2]
    
        company_name = company[company.find('name')+7:company.find('logo')-3]
        company_name = company[:company.find(' ')]
        print company_name
    else:
        company_name = 'Could not be found. Please submit'
    product = data[data.find('attributes')+24:data.find('description')-3]
    print product
    product_name = ''
    for i in range(0, len(product)):
        if product[i] != '\\':
            product_name += product[i]

    return (product_name,company_name)
        

# use this for testing
def get_test():
    '''() -> str
    test without getting from barcode
    '''
    return ("Kellog's Rice Krispies Squares/Original"),("Kellogg")

# use this for processing everythings
def process_image(fileName):
    return get_data(get_upc(filename))

