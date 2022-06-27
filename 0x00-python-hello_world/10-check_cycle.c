#include "lists.h"

/**
  * check_cycle - function that checks if a singly linked list has a cycle.
  * @list: pointer to first element.
  *
  * Return: 0 if there is no cycle, 1 if there is a cycle.
  */

int check_cycle(listint_t *list)
{
	listint_t *now, *next_node;

	if (list == NULL)
		return (0);

	now = list;
	next_node = list;

	while (now && next_node && next_node->next)
	{
		now = now->next;
		next_node = next_node->next->next;
		if (now == next_node)
			return (1);
	}
	if (now != next_node)
		return (0);
	return (1);
}
