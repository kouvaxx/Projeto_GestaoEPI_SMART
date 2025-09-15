from .models import Emprestimo

def recent_emprestimos(request):
    if request.user.is_authenticated:
        recent_emprestimos = Emprestimo.objects.order_by('-data_emprestimo')[:5]
        return {'recent_emprestimos': recent_emprestimos}
    return {}
