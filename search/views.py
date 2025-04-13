from django.views import generic
from .models import Chapter
from .search_engine import bible_search_engine
from django.db.models import Case, When
from django.shortcuts import redirect

# Create your views here.
class ChapterView(generic.DetailView):
    model = Chapter
    template_name = "search/chapter.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_chapter = self.object

        previous_chapter = Chapter.objects.filter(id__lt=current_chapter.id).order_by('-id').first()
        next_chapter = Chapter.objects.filter(id__gt=current_chapter.id).order_by('id').first()
        context['previous_chapter'] = previous_chapter
        context['next_chapter'] = next_chapter

        return context

class SearchView(generic.ListView):
    model = Chapter
    template_name = 'search/main.html'
    context_object_name = 'results'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        if 'page' not in request.GET and 'query_text' in request.GET:
            url = f"{request.path}?query_text={request.GET['query_text']}&page=1"
            return redirect(url)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get('query_text', '').strip()

        if query:
            result_ids = [raw_result["chapterid"] for raw_result in bible_search_engine.search(query)[:50]]
            results = self.model.objects.filter(id__in=result_ids).order_by(
                Case(*[When(id=id, then=pos) for pos, id in enumerate(result_ids)])
            )
        else:
            results = self.model.objects.none()

        return results
