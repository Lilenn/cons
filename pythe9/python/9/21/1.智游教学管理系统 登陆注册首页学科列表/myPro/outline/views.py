from django.shortcuts import render,redirect,render_to_response
from django.views import View
from .models import OutlineModel
from stage.models import StageModel
# Create your views here.

class OutlineView(View):
    def get(self,request):
        stage_id = request.GET['stage_id']
        outline = OutlineModel.objects.filter(stage_id=stage_id)
        return render_to_response('outline/outline_list.html',{'outlines':outline})

class DetailView(View):
    def get(self,request):
        outline_id = request.GET['outline_id']
        outline = OutlineModel.objects.get(id=outline_id)
        stage = StageModel.objects.get(id=outline.stage_id)
        return render_to_response('outline/detail.html',{'outline':outline,'stage':stage})

class EditView(View):
    def get(self,request):
        outline_id = request.GET['outline_id']
        outline = OutlineModel.objects.get(id=outline_id)
        return render_to_response('outline/edit.html',{'outlines':outline})
    def post(self,request):
        outline_id = request.POST['outline_id']
        title = request.POST['title']
        number = request.POST['number']
        days = request.POST['days']
        advancing = request.POST['advancing']
        remark = request.POST['remark']
        outline = OutlineModel.objects.get(id=outline_id)
        if outline:
            outline.title = title
            outline.number = number
            outline.days = days
            outline.advancing = advancing
            outline.remark = remark
            outline.save()
        return redirect('/outline/detail/?outline_id={outline_id}&stage_id={stage_id}'.format(outline_id=outline_id,stage_id=outline.stage_id))

class DeleteView(View):
    def get(self,request):
        outline_id = request.GET['outline_id']
        outline = OutlineModel.objects.get(id=outline_id)
        stage_id = outline.stage_id
        if outline:
            outline.delete()
        return redirect('/outline/list/?stage_id=' + str(stage_id))

class AddView(View):
    def get(self,request):
        stage = StageModel.objects.all()
        return render_to_response('outline/add.html',{'stages':stage})
    def post(self,request):

        stage_id = request.POST['stage_id']
        title = request.POST['title']
        number = request.POST['number']
        days = request.POST['days']
        advancing = request.POST['advancing']
        remark = request.POST['remark']

        outline = OutlineModel()
        outline.stage_id = stage_id
        outline.title = title
        outline.number = number
        outline.days = days
        outline.advancing = advancing
        outline.remark =remark
        outline.save()

        return redirect('/outline/list/?stage_id=' +str(stage_id))

