#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	fast = list;
	slow = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
} 
