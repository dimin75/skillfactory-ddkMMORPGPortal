from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.views.generic.edit import FormMixin

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect

from .models import MmoRPGAdv, Response
from .forms import CreateAdvForm, CreateResponseForm
from .filters import ResponseFilter

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class AdvList(ListView):
    model = MmoRPGAdv
    template_name = 'mmorpgadvs.html'
    context_object_name = 'advertList'
    # queryset = Advert.objects.order_by('-id_category')
    queryset = MmoRPGAdv.objects.order_by('-created_at')
    paginate_by = 10


class AdvView(FormMixin, DetailView):
    model = MmoRPGAdv
    template_name = 'mmorpgadv.html'
    form_class = CreateResponseForm
    context_object_name = 'advertView'

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        response = Response(
            id_user=request.user,
            id_advert=MmoRPGAdv.objects.get(pk=request.POST['id_advert']),
            text=request.POST['text'],

        )
        response.save()

        return redirect('/advert/' + str(response.id_advert.pk))


class AdvCreateView(LoginRequiredMixin, CreateView):
    template_name = 'new.html'
    form_class = CreateAdvForm

    # def post(self, request, *args, **kwargs):
    #     advert = Advert(
    #         id_user=request.user,
    #         id_category=request.POST['category'],
    #         text=request.POST['text'],
    #         file=request.POST['file']
    #     )
    #     advert.save()

    #     return redirect('/adverts/')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            advert = form.save(commit=False)
            advert.id_user = request.user
            advert.save()
            return redirect('/adverts/')
        return super().post(request, *args, **kwargs)

class AdvUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'modify.html'
    form_class = CreateAdvForm
    success_url = '/adverts/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return MmoRPGAdv.objects.get(pk=id)


class ResponseList(ListView):
    model = Response
    template_name = 'answers.html'
    context_object_name = 'responseList'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_adverts = MmoRPGAdv.objects.filter(id_user=self.request.user)
        query = Response.objects.filter(id_advert__in=user_adverts).order_by('-id_user')
        context['filter'] = ResponseFilter(self.request.GET, queryset=query)
        return context


class ResponseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_answer.html'
    queryset = Response.objects.all()
    success_url = '/adverts/responses'


class ResponseAcceptView(DetailView):
    model = Response
    template_name = 'accept_answer.html'

    def post(self, request, *args, **kwargs):
        response = Response.objects.get(pk=request.POST['id_resp'])
        response.accepted = True
        response.save()

        return redirect('/adverts/responses')