from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from .models import Course
from django.views.generic.list import ListView

# TemplateResponseMixin 这个mixin提供的功能是渲染模板并且返回http的响应，需要一个template_name属性 用于指定模板的位置
# 还提供render_response 方法，给模板传入上下文并且渲染模板

from django.views.generic.base import TemplateResponseMixin,View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# PermissionRequiredMixin 允许具有特定权限的用户访问这个视图，超级用户具有所有权限
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .forms import ModuleFormSet

# Create your views here.
# CBV

class OwnerMixin:
    def get_queryset(self):
        qs = super(OwnerMixin,self).get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin:
    def form_vaild(self,form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin,self).form_vaild(form)

class OwnerCourseMixin(OwnerMixin,LoginRequiredMixin):
    model = Course
    feilds = ['subject','title','slug','ovreview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerEditMixin,OwnerCourseMixin):
    fields = ['subject','title','slug','overview']
    success_url = reverse_lazy('manage_course_list')
    template_name = 'manage/course/form.html'

class ManageCourseListView(OwnerCourseMixin,ListView):
    template_name = "manage/course/list.html"

class CourseCreateView(PermissionRequiredMixin,OwnerCourseEditMixin,CreateView):
    permission_required = 'courses.add_course'

class CourseUpdateView(PermissionRequiredMixin,OwnerCourseEditMixin,UpdateView):
    permission_required = 'courses.change_course'

class CourseDeleteView(PermissionRequiredMixin,OwnerCourseMixin,DeleteView):
    permission_required = 'courses.delete_course'
    template_name = 'manage/course/delete.html'
    success_url = reverse_lazy('manage_course_list')

class CourseModuleView(TemplateResponseMixin,View):
    template_name = 'manage/module/formset.html'
    course = None

    def get_formset(self,data = None):
        return ModuleFormSet(instance=self.course,data=data)

    def dispatch(self, request,pk):
        """这个方法是View视图的方法，是一个分发器，http请求进来之后，
        最先执行的是dispatch， 这个方法把小写的http请求的种类分发给同名的方法：
        比如GET请求会被分发到get（）方法"""

        self.course = get_object_or_404(Course,id=pk , owner=request.user)
        return super(CourseModuleView,self).dispatch(request,pk)

    def get(self,request,*args,**kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course':self.course,'formset':formset})

    def post(self,request,*args,**kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response({"course":self.course,'formset':formset})



