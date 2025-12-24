from django import template
from polls.models import Choice
from polls.models import Question

register = template.Library()

@register.filter(name='get_choice_percentage')
def get_choice_percentage(choice, question):
    all_choice_votes = 0;
    for element in Choice.objects.filter(question=question):
        all_choice_votes += element.votes
    if all_choice_votes == 0:
        return 0
    else:
        return round(100 * choice.votes / all_choice_votes, 1)
