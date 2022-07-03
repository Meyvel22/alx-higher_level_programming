#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to linked list head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
		int *good;
		listint_t *trend, *nodes;
		unsigned int n, x, gain, y;

		if (head == NULL)
			return (0);

		n = n_listint(*head);
		good = malloc(n * sizeof(int));
		nodes = malloc(n * sizeof(listint_t));
		trend = *head;
		if (trend == NULL)
			return (1);
		x = 0;
		while (trend != NULL)
		{
				gain = trend->n;
				good[x] = gain;
				nodes[x] = *trend;
				trend = trend->next;
				x++;
		}
		x--;
		n = 1;
		y = 0;
		while (x >= n)
		{
				trend = &nodes[x];
				if (trend->n != good[y])
				{
					free(good);
					free(nodes);
					return (0);
				}
				x--;
				y++;
		}
		free(good);
		free(nodes);
		return (1);
}

/**
 * n_listint - counts elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t n_listint(const listint_t *h)
{
		const listint_t *trend;
		unsigned int n; /* number of nodes */

		trend = h;
		n = 0;

		while (trend != NULL)
		{
				trend = trend->next;
				n++;
		}

		return (n);
}
