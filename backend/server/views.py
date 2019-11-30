from django.shortcuts import render
import openpyxl
from django.http import HttpResponse
import json
from .models import Gr
# Create your views here.
def GetExcel(req):
    if req.method == 'POST':
        if 'file' in req.FILES:
            file = req.FILES['file']
            filename = file._name

            fp = open('%s/%s' % (UPLOAD_DIR, filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            return HttpResponse('File Uploaded')
    return HttpResponse('Failed to Upload File')

def SendGr(request,userId):
	dataList=[]
	queryset = Gr.objects.filter(USERID=userId)
	for row in queryset:
		dataDict={}
		dataDict["CONTENT"]=row.CONTENT
		dataList.append(dataDict)

	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")

