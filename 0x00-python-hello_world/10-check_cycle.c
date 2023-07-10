#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *lentement = list;
	listint_t *rapidement = list;

	if (!list)
		return (0);

	while (lentement && rapidement && rapidement->next)
	{
		lentement = lentement->next;
		rapidement = rapidement->next->next;
		if (lentement == rapidement)
			return (1);
	}

	return (0);
}
