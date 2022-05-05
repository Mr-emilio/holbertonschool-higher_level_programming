#include "lists.h"
/**
 * check_cycle - check if a linked list has a cycle in it
 * @list: linked list
 * Return: 0 if there is not cycle or 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *l1 = list;
	listint_t *l2 = lts;

	while (l1 && l2 && l1->next)
	{
		l2 = l2->next;
		l1 = l1->next->next;
		if (l2 == l1)
			return (1);
	}
	return (0);
}
