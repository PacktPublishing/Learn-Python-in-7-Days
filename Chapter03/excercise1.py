url = "http://www.thapar.edu/index.php/about-us/mission"

url_list = url.split("/")

domain_name = url_list[2]
print domain_name.replace("www.","")

