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

def sendSubjectGrade(request,userEmail):
	dataList=[]
	user = User.objects.get(USEREMAIL=userEmail)
	major = user.MAJOR
	track = user.TRACK
	trackCategory = user.TRACK_CATEGORY
	studentId=user.STUDENT_ID
	if int(studentId[:4])<=2009:
		studentId="2009"
	elif int(studentId[:4])>=2012:
		studentId="2012"
	else:
		studentId="2010"
	queryset = Subject.objects.filter(USEREMAIL=userEmail,CATEGORY=trackCategory)
	dataClass={}

	
	if major == "심화컴퓨터":
		studentIdRequirement=CSEIntenCoStudentId.objects.get(STUDENT_ID=studentId[:4])
		dataClass["TOTAL"]=0
		dataClass["MAJOR"]=0
		dataClass["BASEMAJOR"]=0
		dataClass["ENGINEER_CUL"]=0
		for row in queryset:
			dataClass["TOTAL"]+=row.GRADE
			if row.CLASS=="전공기반":
				dataClass["BASEMAJOR"]+=row.GRADE
			elif row.CLASS=="전공":
				dataClass["MAJOR"]+=row.GRADE
			elif row.CLASS=="기본소양":
				dataClass["ENGINEER_CUL"]+=row.GRADE
			
		for key,value in dataClass.items():
			dataDict={}
			dataDict["CATEGORY"]=key
			dataDict["GRADE"]=str(value)
			if key == "BASEMAJOR":
				dataDict["GRADE"]+=":"+str(studentIdRequirement.BASEMAJOR_GRADE)
			elif key == "MAJOR":
				dataDict["GRADE"]+=":"+str(studentIdRequirement.MAJOR_GRADE)
			elif key == "DESIGN":
				dataDict["GRADE"]+=":"+str(studentIdRequirement.DESIGN_GRADE)
			elif key == "ENGINEER_CUL":
				dataDict["GRADE"]+=":"+str(studentIdRequirement.ENGINEER_CUL_GRADE)
			elif key == "TOTAL":
				dataDict["GRADE"]+=":"+str(studentIdRequirement.TOTAL_GRADE)
			dataList.append(dataDict)
	elif major == "글로벌SW융합":
		dataClass["SW_MAJOR"]=0
		dataClass["SW_CUL"]=0
		for row in queryset:
			if row.CLASS=="전공":
				dataClass["SW_MAJOR"]+=row.GRADE
			elif row.CLASS=="교양" or row.CLASS == "기본소양":
				dataClass["SW_CUL"]+=row.GRADE
		for key,value in dataClass.items():
			dataDict={}
			dataDict["CATEGORY"]=key
			dataDict["GRADE"]=str(value)
			if key == "SW_MAJOR":
				dataDict["GRADE"]+=":"+"51"
			elif key == "SW_CUL":
				dataDict["GRADE"]+=":"+"24~42"	
			dataList.append(dataDict)
	
	elif major == "SW연계융합":
		subject=Subject.objects.filter(USEREMAIL=userEmail,CATEGORY=trackCategory)
			
		if track == "연계전공":
			
			dataClass["SW_CONN_COMMON"]=0
			dataClass["SW_CONN_MAJOR"]=0
			dataClass["SW_CONN_CUL"]=0
			dataClass["TOTAL"]=0		
			for row in subject:
				dataClass["TOTAL"]+=row.GRADE
				if row.CLASS=="공통":
					dataClass["SW_CONN_COMMON"]+=row.GRADE
				elif row.CLASS=="전공":
					dataClass["SW_CONN_MAJOR"]+=row.GRADE
				elif row.CLASS=="교양":
					dataClass["SW_CONN_CUL"]+=row.GRADE
			
			for key,value in dataClass.items():
				dataDict={}
				dataDict["CATEGORY"] = key
				dataDict["GRADE"]=str(value)
				if key == "SW_CONN_MAJOR":
					dataDict["GRADE"]+=":"+"45"
				elif key == "SW_CONN_COMMON":
					dataDict["GRADE"]+=":"+"15"
				elif key == "SW_CONN_CUL":
					dataDict["GRADE"]+=":"+"6"
		elif track == "융합전공":
			
			dataClass["SW_CONN_TOTAL"]=0
			for row in subject:
				print(row.TITLE)
				dataClass["SW_CONN_TOTAL"]+=row.GRADE
			for key,value in dataClass.items():
				dataDict={}
				dataDict["CATEGORY"]=key
				dataDict["GRADE"]=str(value)+":"+"36"
				dataList.append(dataDict)
	
		elif track == "복수전공":

			subject=Subject.objects.filter(USEREMAIL=userEmail,CATEGORY=trackCategory)
			dataClass["SW_CONN_MAJOR"]=0
			for row in subject:
				if row.CLASS=="전공":
					dataClass["SW_CONN_MAJOR"]+=row.GRADE
			
			for key,value in dataClass.items():
				dataDict={}
				dataDict["CATEGORY"]=key
				if trackCategory == "플랫폼소프트웨어" or trackCategory == "데이터과학" or trackCategory == "인간중심소프트웨어":
					dataDict["GRADE"]=str(value)+":"+"65"
				else:
					dataDict["GRADE"]=str(value)+":"+"51"

		elif track == "부전공":

			subject=Subject.objects.filter(USEREMAIL=userEmail)
			dataClass["SW_CONN_MAJOR"]=0
			for row in subject:
				if row.CLASS=="전공":
					dataClass["SW_CONN_MAJOR"]+=row.GRADE

			for key,value in dataClass.items():
				dataDict={}
				dataDict["CATEGORY"]=key
				dataDict["GRADE"]=str(value)+":"+"21"

		
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")

def SendNonSubject(request, userEmail):
	dataList=[]
	user = User.objects.get(USEREMAIL=userEmail)
	major = user.MAJOR
	track = user.TRACK
	#유저의 비 교과목 가져오기
	queryset = Gr.objects.filter(USEREMAIL=userEmail)
	trackNonSubject=CSEIntenCoNonSubject.objects.all()
	if major == "심화컴퓨터":
		trackNonSubject=CSEIntenCoNonSubject.objects.all()
	elif major == "글로벌SW융합":
		trackNonSubject=GlobalSWCoNonSubject.objects.filter(TRACK=track)
	
	userNonSub={}
	for row in queryset:
		userNonSub[row.CATEGORY]=row.CONTENT
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
			dataDict["CATEGORY"]=row.TITLE
			dataDict["CONTENT"]=MyENGGrade+","+str(ENGGrade)
		else:
			if row.TITLE  in userNonSub.keys():
				dataDict["CATEGORY"]=row.TITLE
				dataDict["CONTENT"]=userNonSub[row.TITLE]+","+row.CONTENT
			else:
				dataDict["CATEGORY"]=row.TITLE
				dataDict["CONTENT"]="N"+","+row.CONTENT
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




def UpdateUserInfo(request, userEmail, major, track, trackCategory):
	dataList=[]
	user = User.objects.get(USEREMAIL=userEmail)
	user.MAJOR=major
	user.TRACK=track
	user.TRACK_CATEGORY=trackCategory
	user.save()

	
	dataDict={}
	dataDict["major"]=major
	dataDict["track"]=track
	dataList.append(dataDict)
	print(dataList)
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")


def SendQuestion(request,userEmail):
	dataList=[]
	answer=Answer.objects.filter(USEREMAIL=userEmail)
	for row in answer:
		if row.ISANSWERED == False:
			continue
		dataDict={}
		dataDict["title"]=row.TITLE
		dataDict["desc"]=row.DESC
		dataDict["answer"]=row.ANSWER
		dataList.append(dataDict)
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")


def getQuestion(request,userEmail,title,desc):
	dataList=[]
	question = Question.objects.create(USEREMAIL=userEmail,TITLE=title,DESC=desc)
	answer=Answer.objects.create(USEREMAIL=userEmail,TITLE=title,DESC=desc,QUESTION_ID=question.id)
	dataDict={}
	dataDict["resultValue"]=True
	dataList.append(dataDict)
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")



def SendFaq(request):
	dataList=[]
	answer=Answer.objects.filter(ISFAQ=True)

	for row in answer:
		dataDict={}
		dataDict["title"]=row.TITLE
		dataDict["desc"]=row.DESC
		dataDict["answer"]=row.ANSWER
		dataList.append(dataDict)
	
	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")

def UpdateUserNonSubject(request, userEmail, category, content):
	dataList=[]
	gr = Gr.objects.filter(USEREMAIL=userEmail,CATEGORY=category)
	if len(gr) == 0 :
		Gr.objects.create(USEREMAIL=userEmail,CATEGORY=category,CONTENT=content)
	else:
		uGr=Gr.objects.get(USEREMAIL=userEmail,CATEGORY=category)
		uGr.CONTENT=content
		uGr.save()
	
			
	dataDict={}
	dataDict["resultValue"]=1
	dataList.append(dataDict)

	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")	

def sendSubjects(request,userEmail):
	userSubject = Subject.objects.filter(USEREMAIL=userEmail)
	user=User.objects.get(USEREMAIL=userEmail)
	major=user.MAJOR
	userSubjectDict={}
	for row in userSubject:
		userSubjectDict[row.TITLE]=1
	dataList=[]
	if major == "심화컴퓨터":
		subject=CSEIntenCoSubject.objects.all()
	elif major == "글로벌SW융합":
		subject=GlobalSWCoSubject.objects.all()
	for row in subject:
		if row.TITLE in userSubjectDict.keys():
			dataDict={}
			dataDict["CATEGORY"]=row.CLASS
			dataDict["CONTENT"]=row.TITLE+",Y"
			dataList.append(dataDict)
		else:
			dataDict={}
			dataDict["CATEGORY"]=row.CLASS
			dataDict["CONTENT"]=row.TITLE+",N"
			dataList.append(dataDict)

	result=(json.dumps(dataList, ensure_ascii=False).encode('utf8') )
	return HttpResponse(result, content_type=u"application/json; charset=utf-8")

				
			
		

