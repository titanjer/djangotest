# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext

from forms import MultiInputForm

def multi_input_view(request, ):

    if request.method == 'POST':

        form = MultiInputForm(request.POST)
        if form.is_valid():
            assert False, 'Mobile: %s' % form.cleaned_data['mobile'] 

    else:
        form = MultiInputForm()

    return render_to_response('view.html', {
        'form': form,
    }, context_instance=RequestContext(request))
