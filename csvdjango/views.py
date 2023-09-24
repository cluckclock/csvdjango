from django.shortcuts import HttpResponse
import pandas as pd
  
def Table(request):
    df = pd.read_csv("field_data.csv")
    #'tableview/static/csv/20_Startups.csv' is the django 
    # directory where csv file exist.
    # Manipulate DataFrame using to_html() function
    geeks_object = df.to_html()
  
    return HttpResponse(geeks_object)