#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *temp = *head;
	listint_t *current = *head;
	listint_t *next = NULL;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	if (*head == temp)
		return (1);
	else
		return (0);
}
