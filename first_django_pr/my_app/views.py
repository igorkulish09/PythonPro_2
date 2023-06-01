from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import WeekDay, Note
from django.template import loader
from .forms import NoteForm
from django.views.generic import DetailView, FormView, ListView
from django.urls import reverse


# Create your views here.
def index(request):
    return redirect("my_week")


class DaysList(ListView):
    model = WeekDay
    template_name = "my_app/week.html"
    context_object_name = "days"


def my_week(request):
    template = loader.get_template("my_app/week.html")
    context = {"days": WeekDay.objects.all()}

    return HttpResponse(template.render(context, request))


class DayDetail(DetailView):
    model = WeekDay
    template_name = "my_app/weekday_detail.html"


def my_day(request, week_day_id):
    day = get_object_or_404(WeekDay, pk=week_day_id)
    return render(request, "my_app/weekday_detail.html", {"week_day": day})


class NoteFormView(FormView):
    form_class = NoteForm
    template_name = "my_app/weekday_detail.html"

    def form_valid(self, form):
        week_day = get_object_or_404(WeekDay, pk=self.kwargs["pk"])
        Note.objects.create(
            week_day=week_day,
            title=form.cleaned_data["title"],
            msg=form.cleaned_data["msg"],
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["object"] = get_object_or_404(WeekDay, pk=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse("week_day", kwargs={"pk": self.kwargs["pk"]})


def add_note(request, week_day_id):
    week_day = get_object_or_404(WeekDay, pk=week_day_id)
    form_data = NoteForm(request.POST)
    if form_data.is_valid():
        Note.objects.create(
            week_day=week_day,
            title=form_data.cleaned_data["title"],
            msg=form_data.cleaned_data["msg"],
        )
    return render(
        request,
        "my_app/weekday_detail.html",
        {"week_day": week_day, "error_message": form_data.errors},
    )


# def add_note(request, week_day_id):
#     week_day = get_object_or_404(WeekDay, pk=week_day_id)
#     form_data = NoteForm(request.POST)
#     if form_data.is_valid():
#         note = form_data.save(commit=False)
#         note.week_day = week_day
#         note.save()
#         return redirect('day_detail', pk=week_day_id)
#     return render(request, "my_app/weekday_detail.html", {"week_day": week_day, "error_message": form_data.errors})
