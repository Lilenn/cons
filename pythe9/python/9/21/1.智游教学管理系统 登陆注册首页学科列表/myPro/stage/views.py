from django.shortcuts import render,render_to_response,redirect
from django.views import View
from .models import StageModel
from subject.models import SubjectModel
# Create your views here.

class StageView(View):
    def get(self,request):
        subject_id = request.GET['subject_id']
        stage_list = StageModel.objects.filter(subject_id=subject_id)
        return render_to_response('stage/stage_list.html',{'stage_list':stage_list})

class DetailView(View):
    def get(self,request):
        stage_id = request.GET['stage_id']
        subject_id  =request.GET['subject_id']
        stage = StageModel.objects.get(id=stage_id)
        subject = SubjectModel.objects.get(id=stage.subject_id)
        return render_to_response('stage/detail.html',{'stage':stage,'subject':subject})


class DeleteView(View):
    def get(self,request):
        stage_id = request.GET['stage_id']
        stage = StageModel.objects.get(id=stage_id)
        subject_id = stage.subject_id
        if stage:
            stage.delete()
        return redirect('/stage/list/?subject_id=' + str(subject_id))

class EditView(View):
    def get(self,request):
        stage_id = request.GET['stage_id']
        stage = StageModel.objects.get(id=stage_id)
        return render_to_response('stage/edit.html',{'stage':stage})
    def post(self,request):
        stage_id = request.POST['stage_id']
        title = request.POST['title']
        number = request.POST['number']
        days = request.POST['days']
        project = request.POST['project']
        teaching = request.POST['teaching']
        learning = request.POST['learning']
        sharing = request.POST['sharing']
        remark = request.POST['remark']
        stage = StageModel.objects.get(id=stage_id)
        if stage:
            stage.title = title
            stage.number = number
            stage.days = days
            stage.teaching = teaching
            stage.learning = learning
            stage.sharing = sharing
            stage.project = project
            stage.remark = remark
            stage.save()

        return redirect('/stage/detail/?stage_id={stage_id}&subject_id={subject_id}'.format(stage_id=stage_id,subject_id=stage.subject_id))

class AddView(View):
    def get(self,request):
        subjects = SubjectModel.objects.all()
        return render_to_response('stage/add.html',{'subjects':subjects})
    def post(self,request):
        subject_id = request.POST['subject_id']
        title = request.POST['title']
        number = request.POST['number']
        days = request.POST['days']
        project = request.POST['project']
        teaching = request.POST['teaching']
        learning = request.POST['learning']
        sharing = request.POST['sharing']
        remark = request.POST['remark']

        stage = StageModel()
        stage.subject_id = subject_id
        stage.title = title
        stage.project = project
        stage.days = days
        stage.number = number
        stage.teaching = teaching
        stage.learning = learning
        stage.sharing = sharing
        stage.remark = remark
        stage.save()

        return redirect('/stage/list/?subject_id=' + str(subject_id))