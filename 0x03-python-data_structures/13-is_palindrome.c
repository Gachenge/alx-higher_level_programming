#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *temp = *head;
	listint_t *current = *head;
	listint_t *next = NULL;
	listint_t *temp1 = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	temp1 = *head;
	if (temp1->n == temp->n)
		return (1);
	return (0);
}
