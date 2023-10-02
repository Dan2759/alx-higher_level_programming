#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: is an integer variable.
 * @next: points to the next node
 *
 * Description: Defines the structure of a singly linked list node.
 * for use in Holberton project functions.
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif
