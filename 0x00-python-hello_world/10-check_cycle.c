#include "lists.h"

/**
 * check_cycle - fun
 * @head: pointer
 *
 * Return: pointer
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1 = list;
	listint_t *temp2 = list;

	if (list == NULL)
		return (0);

	while (temp1 && temp2 && temp2->next)
	{
		temp2 = temp2->next->next;
		temp1 = temp1->next;
		if (temp2 == temp1)
		{
			return (1);
		}
	}

	return (0);
}
