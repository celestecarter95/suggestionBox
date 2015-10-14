from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseForbidden

from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import FormView
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from .models import Idea, Profile, Category, Comment

# Create your views here.
class IdeaListView(ListView):
	#template_name is "kaizen/idea_list.html"
	model = Idea

	def get_queryset(self):
		return Idea.objects.order_by('-pub_date')

class IdeaDetailView(DetailView):
	#template_name is "kaizen/idea_detail.html"
	model = Idea

#class IdeaDetailView(View):
#	#template_name is "kaizen/idea_detail.html"
#	
#	def get(self, request, *args, **kwargs):
#		view = IdeaDetailDisplay.as_view()
#		return view(request, *args, **kwargs)
#	
#	def post(self, request, *args, **kwargs):
#		view = CommentOnDetail.as_view()
#		return view(request, *args, **kwargs)
#
#
#	#def form_valid(self, form):
#	#	comment = Comment()
#	#	comment.idea = get_object_or_404(Post, pk=form.cleaned_data["idea_id"]
#	#	comment.comment_text = form.cleaned_data["comment"]
#	#	comment.save()
#	#	return super(CommentOnDetail, self).form_valid(form)
#
#class CommentOnDetailForm(forms.Form):
#	comment = forms.CharField(widget=forms.Textarea)
#	idea_id = forms.IntegerField(widget=forms.HiddenInput)
#	#model = Idea
#
#class IdeaDetailDisplay(DetailView):
#	model = Idea
#	
#	def get_context_data(self, **kwargs):
#		context = super(IdeaDetailDisplay, self).get_context_data(**kwargs)
#        context['form'] = CommentOnDetailForm()
#        return context
#
#class CommentOnDetail(SingleObjectMixin, FormView):
#	template_name = 'kaizen/idea_detail.html'
#	form_class = CommentOnDetailForm
#	model = Idea
#
#	def post(self, request, *args, *kwargs):
#		if not request.user.is_authenticated():
#			return HttpResponseForbidden()
#		self.object = self.get_object()
#		return super(CommentOnDetail, self).post(request, *args, **kwargs)
#
#	def get_success_url(self):
#		return reverse('kaizen:ideadetail', args=(self,object.pk,))
#		#or return reverse('kaizen:ideadetail', kwargs={'pk': self.object.pk})

class SecretView(TemplateView):
    template_name="kaizen/secret.html"

class CreateIdeaView(CreateView):
	#template_name is "kaizen/idea_form.html"
	model = Idea
	fields = ['title', 'description', 'category']
	success_url = reverse_lazy('kaizen:idealist')

	def form_valid(self, form):
		profile = Profile();
		profile.user = self.request.user
		profile.save()
		idea = form.save(commit=False)
		idea.profile = profile
		idea.save()
		return super(CreateIdeaView, self).form_valid(form)

class UpdateIdeaView(UpdateView):
	#template_name is "kaizen/idea_form.html"
	model = Idea
	fields = ['profile', 'title', 'description', 'status', 'category']
	success_url = reverse_lazy('kaizen:idealist')

class DeleteIdeaView(DeleteView):
	#template_name is "kaizen/idea_confirm_delete.html"
	model = Idea
	success_url = reverse_lazy('kaizen:idealist')
