from django.shortcuts import render,redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import  ListView,FormView,CreateView,UpdateView,DeleteView
from .models import StudentModel
from .forms import StudentForm
from django.contrib import messages

# Create your views here.
class ListStudent(ListView):

    template_name = "stu_list.html"
    queryset = StudentModel.objects.all()


class AddStuden(SuccessMessageMixin,FormView):


    form_class = StudentForm
    template_name = "addstu.html"


    # def get_success_url(self):
    #     from django.contrib import messages
    #     messages.success(self.request, 'Student Added successfully')

    def form_valid(self, form):
        sno=form.cleaned_data['rno']
        first_n=form.cleaned_data['first_name']
        las_n=form.cleaned_data['last_name']
        fname=form.cleaned_data['father_name']
        g=form.cleaned_data[ 'gender']
        c=form.cleaned_data['course']
        add=form.cleaned_data['address']
        #print(sno,'--',first_n,'--',las_n,'--',fname,'--',g,'--',c,'--',add)
        sm=StudentModel(rno=sno,first_name=first_n,last_name=las_n,father_name=fname,gender=g,course=c,address=add)
        sm.save()
        messages.success(self.request, "Added successfully")
        return redirect('main')

        #return render(self.request, 'stu_list.html', self.get_context_data())



class UpdateStudent(SuccessMessageMixin,UpdateView):
    template_name = "update_stu.html"

    model = StudentModel
    fields = "__all__"

    success_url = "/main/"
    success_message = "student Updated successfully"


class DeleteStudent(DeleteView):
    template_name = 'deletestu.html'
    model = StudentModel
    success_url="/main/"
