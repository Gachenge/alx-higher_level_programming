#include "lists.h"

/**
 * check_cycle - check if there is a loop in a list
 * @list: the list
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	s = f = list;
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;

		if (f == s)
			return (1);
	}
	return (0);
}
