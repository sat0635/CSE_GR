from django.shortcuts import render
import openpyxl
from django.http import HttpResponse
import json
from .models import *
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

def SendSubject(request,userEmail):
	dataList=[]
	queryset = Subject.objects.filter(USEREMAIL=userEmail)
	dataClass={}
	dataClass["MAJOR"]=0
	dataClass["BASEMAJOR"]=0
	dataClass["ENGINEER_CUL"]=0
	ENGINEER_CUL=0
	for row in queryset:
		if row.CLASS=="전공기반":
			dataClass["BASEMAJOR"]+=row.GRADE
		elif row.CLASS=="전공":
			dataClass["MAJOR"]+=row.GRADE
		elif row.CLASS=="기본소양":
			dataClass["ENGINEER_CUL"]+=row.GRADE	
	for key,value in dataClass.items():
		dataDict={}
		dataDict["CONTENT"]=key+":"+str(value)
		dataList.append(dataDict)

	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")

def SendNonSubject(request, userEmail):
	dataList=[]
	queryset = Gr.objects.filter(USEREMAIL=userEmail)
	trackNonSubject=CSEIntenCoNonSubject.objects.all()
	userNonSub={}
	for row in queryset:
		data=row.CONTENT.split(":")
		userNonSub[data[0]]=data[1]
	for row in trackNonSubject:
		dataDict={}
		if row.TITLE == "영어":
			#유저의 영어 종류  가져오기
			ENGs=[]
			ENGGrade=""
			MyENGGrade=""
			if row.TITLE in userNonSub.keys():
				ENGClass=userNonSub[row.TITLE].split(",")[0]
				MyENGGrade=userNonSub[row.TITLE].split(",")[1]
			else:
				ENGClass="토익"
				MyENGGrade="N"
			ENGs=row.CONTENT.split(",")
			
				
			#졸업요건의 영어종류 찾기
			for ENG in ENGs:
				if ENG.split(":")[0] == ENGClass:
					ENGGrade=ENG.split(":")[1]
					break
			dataDict["CONTENT"]=row.TITLE+":"+MyENGGrade+","+str(ENGGrade)
		else:
			if row.TITLE  in userNonSub.keys():
				dataDict["CONTENT"]=row.TITLE+":"+userNonSub[row.TITLE]+","+row.CONTENT
			else:
				dataDict["CONTENT"]=row.TITLE+":"+"N"+","+row.CONTENT
		dataList.append(dataDict)
		

	for row in dataList:
		print(row)
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")


def InsertUser(request, userEmail):
	dataList=[]
	queryset = User.objects.filter(USEREMAIL=userEmail)
	if len(queryset) == 0 :
		User.objects.create(USEREMAIL=userEmail)
	dataDict={}
	dataDict["resultValue"]=True
	dataList.append(dataDict)
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")


def SendUserInfo(request, userEmail):
	dataList=[]
	queryset = User.objects.filter(USEREMAIL=userEmail)
	
	for row in queryset:
		dataDict={}
		dataDict["major"]=row.MAJOR
		dataDict["track"]=row.TRACK
		dataList.append(dataDict)

	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )	
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")




def UpdateUserInfo(request, userEmail, major, track):
	dataList=[]
	user = User.objects.get(USEREMAIL=userEmail)
	user.MAJOR=major
	user.TRACK=track
	user.save()


	dataDict={}
	dataDict["major"]=major
	dataDict["track"]=track
	dataList.append(dataDict)
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")


def SendQuestion(request):
	dataList=[]
	question=Question.objects.all()
	
	for row in question:
		dataDict={}
		dataDict["title"]=row.TITLE
		dataDict["desc"]=row.DESC
		dataList.append(dataDict)
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")


def getQuestion(request,userEmail,title,desc):
	dataList=[]
	question = Question.objects.create(USEREMAIL=userEmail,TITLE=title,DESC=desc)
	
	dataDict={}
	dataDict["resultValue"]=True
	dataList.append(dataDict)
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")



def SendFaq(request):
	dataList=[]
	question=Question.objects.all()

	for row in question:
		dataDict={}
		dataDict["title"]=row.TITLE
		dataDict["desc"]=row.DESC
		dataList.append(dataDict)
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")
