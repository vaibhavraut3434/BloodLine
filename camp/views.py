from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from host.models import Hostcamp
from datetime import date
# Create your views here.
from .fusioncharts import FusionCharts

def index(request):
    h = Hostcamp()
    obj = h.getdata()
    #print("Today's date:", today)
   # for x in obj:
     #   if x.dob==today:
     

    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column3d", "ex1" , "400", "350", "chart-1", "json", 
    # The data is passed as a string in the `dataSource` as parameter.
    """{  
    "chart": {
    "caption": "Donors Analysis",
    "baseFont": "Lato",
    "captionfontsize":"18",
    "subcaptionfontbold":"0",
    "subcaptionfontsize":"14",
    "subcaption": "Year - 2019",
    "yaxisname": "Total no. of Donors in Maharashtra",
    "captionpadding": "10",
    "bgalpha": "0",
    "canvasbgalpha": "0",
    "showvalues": "0",
    "showborder": "0",
    "canvasborderalpha": "0",
    "showalternatehgridcolor": "0",
    "plotgradientcolor": "",
    "showplotborder": "0",
    "adjustDiv":"0",
    "yaxisnamefontsize":"14",
    "yAxisNameFontBold":"0",
    "yAxisValuesPadding":"9",
    "divlinealpha": "10",
    "xaxislinealpha":"20",
    "LabelPadding": "5",
    "showlabels": "1",
    "numdivlines":"4",
    "showxaxisline":"1",
    "plotspacepercent":"40",
    "yAxisValueDecimals":"0",
    "formatnumberscale": "1",
    "numberscalevalue": "",
    "numberscaleunit": " ",
    "palettecolors": "#ee5253",
    "plotToolText": "<div>Blood Group : <b>$label</b><br/>Count : <b>$value Donors</b></div>",
    "defaultnumberscale": " Donors",
    "plotFillAlpha": "90"
    },
    "annotations": {
    "autoScale": "0",
    "scaleImages": "0",
    "origW": "400",
    "origH": "300",
    "groups": [{
        "id": "user-images",
        "items": [{
        "id": "Batman-icon",
        "type": "",
        "url": "http://csm.fusioncharts.com/files/assets/img/batman.png",
        "x": "$dataset.0.set.0.CenterX - 18",
        "y": "$dataset.0.set.0.EndY + 10",
        "xScale": "75",
        "yScale": "75"
        }, {
        "id": "Wolverine-icon",
        "type": "",
        "url": "http://csm.fusioncharts.com/files/assets/img/wolverine.png",
        "x": "$dataset.0.set.1.CenterX - 18",
        "y": "$dataset.0.set.1.EndY + 10",
        "xScale": "75",
        "yScale": "75"
        }, {
        "id": "IronMan-icon",
        "type": "",
        "url": "http://csm.fusioncharts.com/files/assets/img/ironman.png",
        "x": "$dataset.0.set.2.CenterX - 18",
        "y": "$dataset.0.set.2.EndY + 10",
        "xScale": "75",
        "yScale": "75"
        }, {
        "id": "Deadpool-icon",
        "type": "",
        "url": "http://csm.fusioncharts.com/files/assets/img/deadpool.png",
        "x": "$dataset.0.set.3.CenterX - 18",
        "y": "$dataset.0.set.3.EndY + 10",
        "xScale": "75",
        "yScale": "75"
        }, {
        "id": "SpiderMan-icon",
        "type": "",
        "url": "http://csm.fusioncharts.com/files/assets/img/spiderman.png",
        "x": "$dataset.0.set.4.CenterX - 18",
        "y": "$dataset.0.set.4.EndY + 10",
        "xScale": "75",
        "yScale": "75"
        }, {
        "id": "Thor-icon",
        "type": "",
        "url": "http://csm.fusioncharts.com/files/assets/img/thor.png",
        "x": "$dataset.0.set.5.CenterX - 18",
        "y": "$dataset.0.set.5.EndY + 10",
        "xScale": "75",
        "yScale": "75"
        }, {
        "id": "SuperMan-icon",
        "type": "",
        "url": "http://csm.fusioncharts.com/files/assets/img/superman.png",
        "x": "$dataset.0.set.6.CenterX - 18",
        "y": "$dataset.0.set.6.EndY + 10",
        "xScale": "75",
        "yScale": "75"
        }, {
        "id": "CaptainAmerica-icon",
        "type": "",
        "url": "http://csm.fusioncharts.com/files/assets/img/captain-america.png",
        "x": "$dataset.0.set.7.CenterX - 18",
        "y": "$dataset.0.set.7.EndY + 10",
        "xScale": "75",
        "yScale": "75"
        }]
    }]
    },
    "data": [{
    "label": "O+",
    "value": "4500"
    }, {
    "label": "O-",
    "value": "2000"
    }, {
    "label": "A+",
    "value": "5800"
    }, {
    "label": "A-",
    "value": "4200"
    }, {
    "label": "B+",
    "value": "3600"
    }, {
    "label": "B-",
    "value": "2100"
    }, {
    "label": "AB+",
    "value": "8800"
    }, {
    "label": "AB-",
    "value": "6000"
    }]
    }""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'index.html', {'obj':obj,'output' : column2d.render()})

#    return render(request, 'index.html',{'obj':obj})

def fashion(request):
    return render(request, 'fashion.html')



def travel(request):
    return render(request, 'travel.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')



