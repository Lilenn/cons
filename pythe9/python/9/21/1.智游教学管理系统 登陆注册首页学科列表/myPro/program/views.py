from django.shortcuts import render,render_to_response,redirect
from django.views import View
from .models import ProgramModel
from stage.models import StageModel
from outline.models import OutlineModel

# Create your views here.
class ProgramView(View):
    def get(self,request):
        outline_id = request.GET['outline_id']

        program = ProgramModel.objects.filter(outline_id=outline_id)
        outline = OutlineModel.objects.filter(id=outline_id)
        return render_to_response('program/program_list.html',{'programs':program,'outlines':outline})

class DetailView(View):
    def get(self,request):
        program_id = request.GET['program_id']
        program = ProgramModel.objects.get(id=program_id)
        outline = OutlineModel.objects.get(id=program.outline_id)
        return render_to_response('program/detail.html', {'program': program, 'outline': outline})

class AddView(View):
    def get(self,request):
        stage = StageModel.objects.all()
        outline = OutlineModel.objects.all()
        return render_to_response('program/add.html', {'stages': stage,'outlines':outline})
    def post(self,request):
        stage_id = request.POST['stage_id']
        ouline_id = request.POST['outline_id']
        number = request.POST['number']
        sign = request.POST['sign']
        digest = request.POST['digest']
        prepare = request.POST['prepare']
        process = request.POST['process']
        attention = request.POST['attention']
        exercise = request.POST['exercise']
        share = request.POST['share']
        management = request.POST['management']
        remark = request.POST['remark']

        program = ProgramModel()
        program.stage_id = stage_id
        program.outline_id = ouline_id
        program.number = number
        program.sign = sign
        program.digest = digest
        program.propare = prepare
        program.process = process
        program.attention = attention
        program.exercise = exercise
        program.share = share
        program.management = management
        program.remark = remark
        program.save()

        return redirect('/program/list/?outline_id=' + str(ouline_id))

class EditView(View):
    def get(self,request):
        program_id = request.GET['program_id']
        program = ProgramModel.objects.get(id=program_id)
        stage = StageModel.objects.all()
        outline = OutlineModel.objects.all()

        return render_to_response('program/edit.html',{'program':program,'stage':stage,'outline':outline})
    def post(self,request):
        program_id = request.POST['program_id']
        stage_id = request.POST['stage_id']
        outline_id = request.POST['outline_id']
        number = request.POST['number']
        sign = request.POST['sign']
        digest = request.POST['digest']
        prepare = request.POST['prepare']
        process = request.POST['process']
        attention = request.POST['attention']
        exercise = request.POST['exercise']
        share = request.POST['share']
        management = request.POST['management']
        remark = request.POST['remark']

        program = ProgramModel.objects.get(id=program_id)
        if program:
            program.stage_id = stage_id
            program.outline_id = outline_id
            program.number = number
            program.sign = sign
            program.digest = digest
            program.propare = prepare
            program.process = process
            program.attention = attention
            program.exercise = exercise
            program.share = share
            program.management = management
            program.remark = remark
            program.save()

        return redirect('/program/detail/?program_id={program_id}&outline_id={outline_id}'.format(program_id=program_id,outline_id=program.outline_id))

class DeleteView(View):
    def get(self,request):
        program_id = request.GET['program_id']
        program = ProgramModel.objects.get(id=program_id)
        outline_id = program.outline_id
        if program:
            program.delete()
        return redirect('/program/list/?outline_id=' + str(outline_id))