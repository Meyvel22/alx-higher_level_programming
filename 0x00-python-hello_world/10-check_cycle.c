#include "lists.h"

/**
  * check_cycle - function that checks if a singly linked list has a cycle.
  * @list: pointer to first element.
  *
  * Return: 0 if there is no cycle, 1 if there is a cycle.
  */

int check_cycle(listint_t *list)
{
	listint_t *now;
	listint_t *later;

	now = list;
	next_node = list;

	while (list && now && now->next)
	{
		list = list->next;
		now = now->next->next;

		if (list == now)
		{
			list = later;
			later = now;
			while (1)
			{
				now = later;
				while (now->next != list && now->next != later)
				{
					now = now->next;
				}
				if (now->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
